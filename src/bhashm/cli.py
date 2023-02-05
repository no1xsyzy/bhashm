import asyncio
import logging
import sys

import toml
from rich.logging import RichHandler

from blivedm.handlers import ctx_client
from . import listen_to_all


class InjectingFilter(logging.Filter):
    def filter(self, record):
        client = ctx_client.get(None)
        if client is None:
            record.room_id = 'NO_ROOM'
        else:
            record.room_id = client.room_id
        return True


def main():
    rich_handler = RichHandler(rich_tracebacks=True)
    rich_handler.addFilter(InjectingFilter())
    logging.basicConfig(
        level="NOTSET",
        format="[%(room_id)s] %(message)s",
        datefmt="[%Y-%m-%d %H:%M:%S]",
        handlers=[rich_handler],
    )

    argi = iter(sys.argv)

    _ = next(argi)

    room_ids = []
    famous_people = []

    for arg in argi:
        if arg in ['-c', '--config']:
            with open(next(argi), 'r') as f:
                cfg = toml.load(f)
                room_ids = cfg['room_ids']
                famous_people = cfg['famous_people']
        elif arg in ['-r', '--room']:
            for room_id in (int(sri) for sri in next(argi).split(",")):
                if room_id < 0:
                    room_ids.remove(-room_id)
                elif room_id not in room_ids:
                    room_ids.append(room_id)
        elif arg in ['-f', '--famous']:
            for fuid in (int(suid) for suid in next(argi).split(",")):
                if fuid < 0:
                    famous_people.remove(-fuid)
                elif fuid not in famous_people:
                    famous_people.append(fuid)
        else:
            raise ValueError()
    if not room_ids:
        sys.exit("no room_ids, this may be due to a config mistake")

    try:
        asyncio.get_event_loop().run_until_complete(listen_to_all(room_ids, famous_people))
    except KeyboardInterrupt:
        print("keyboard interrupt", file=sys.stdout)
