import asyncio
from datetime import datetime

import aiofiles
import aiocsv
import aiohttp
from rich import print

import blivedm

ROOM_IDS = [ 81004, 730215 ]

live_start_times = {}
csv_write_queues = {}

async def main():
    await listen_to_all()


async def get_live_start_time(room_id, fallback_to_now=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={room_id}") as resp:
            jso = await resp.json()
            live_start_time = jso['data']['room_info']['live_start_time']
            if fallback_to_now and live_start_time == 0:
                live_start_time = int(datetime.now().timestamp())
            return live_start_time


async def csv_writer(room_id, start):
    while True:
        async with aiofiles.open(f"{room_id}_{datetime.fromtimestamp(start).strftime('%Y年%m月%d日%H点')}.csv", mode='w', encoding='utf-8', newline="") as afp:
            writer = aiocsv.AsyncDictWriter(afp, ['time', 't', 'marker', 'symbol'])
            await writer.writeheader()
            await afp.flush()
            queue = asyncio.Queue()
            csv_write_queues[room_id] = queue
            while True:
                to_write = await queue.get()
                if to_write == "RESTART":
                    start = get_live_start_time(room_id, True)
                    queue.task_done()
                    break
                else:
                    await writer.writerow(to_write)
                    await afp.flush()
                    queue.task_done()


async def listen_to_all():
    script_start = int(datetime.now().timestamp())
    clients = {}
    for room_id in ROOM_IDS:
        clients[room_id] = blivedm.BLiveClient(room_id)
        # start time
        start_time_stamp = await get_live_start_time(room_id)
        live_start_times[room_id] = datetime.fromtimestamp(start_time_stamp) if start_time_stamp != 0 else None
        # writer
        asyncio.create_task(csv_writer(room_id, script_start))

    handler = HashMarkHandler()
    print(handler._CMD_CALLBACK_DICT)
    del handler._CMD_CALLBACK_DICT['LIVE']
    del handler._CMD_CALLBACK_DICT['PREPARING']
    handler._CMD_CALLBACK_DICT['WATCHED_CHANGE'] = None
    handler._CMD_CALLBACK_DICT['LIKE_INFO_V3_CLICK'] = None
    handler._CMD_CALLBACK_DICT['LIKE_INFO_V3_UPDATE'] = None

    for client in clients.values():
        client.add_handler(handler)
        client.start()

    try:
        await asyncio.gather(*( client.join() for client in clients.values()))
    finally:
        await asyncio.gather(*( client.stop_and_close() for client in clients.values()))

class HashMarkHandler(blivedm.BaseHandler):
    async def _on_danmaku(self, client, message):
        if message.msg.startswith("#"):
            room_id = client.room_id
            time = datetime.fromtimestamp(message.timestamp/1000)
            marker = message.uname
            symbol = message.msg
            if live_start_times[room_id] is not None:
                t = str(time - live_start_times[room_id])
                print(f"[{room_id}] {symbol} @ {time}({t} from live start) by {marker}")
                await csv_write_queues[room_id].put({'time': time, 't': t, 'marker': marker, 'symbol': symbol})
            else:
                print(f"[{room_id}] {symbol} @ {time} by {marker}")
                await csv_write_queues[room_id].put({'time': time, 't': "", 'marker': marker, 'symbol': symbol})

    # TODO: how to handle live start and live end?


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())