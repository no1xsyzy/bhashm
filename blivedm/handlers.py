# -*- coding: utf-8 -*-
import logging
from typing import *

from rich import print
from pydantic import parse_obj_as, ValidationError

from . import client as client_
from . import models

__all__ = (
    'HandlerInterface',
    'BaseHandler',
)

logger = logging.getLogger('blivedm')

# 常见可忽略的cmd
IGNORED_CMDS = (
    'COMBO_SEND',
    'ENTRY_EFFECT',
    'GUARD_HONOR_THOUSAND',
    'HOT_RANK_CHANGED',
    'HOT_RANK_CHANGED_V2',
    'INTERACT_WORD',
    'LIKE_INFO_V3_CLICK',
    'LIKE_INFO_V3_UPDATE',
    'LIVE_INTERACTIVE_GAME',
    'NOTICE_MSG',
    'ONLINE_RANK_COUNT',
    'ONLINE_RANK_TOP3',
    'ONLINE_RANK_V2',
    'PK_BATTLE_END',
    'PK_BATTLE_FINAL_PROCESS',
    'PK_BATTLE_PROCESS',
    'PK_BATTLE_PROCESS_NEW',
    'PK_BATTLE_SETTLE',
    'PK_BATTLE_SETTLE_USER',
    'PK_BATTLE_SETTLE_V2',
    'ROOM_BLOCK_MSG',
    'ROOM_REAL_TIME_MESSAGE_UPDATE',
    'STOP_LIVE_ROOM_LIST',
    'SUPER_CHAT_MESSAGE_JPN',
    'USER_TOAST_MSG',
    'WATCHED_CHANGE',
    'WIDGET_BANNER',
)

# 已打日志的未知cmd
logged_unknown_cmds = set()


class HandlerInterface(Protocol):
    """直播消息处理器接口"""
    async def handle(self, client: client_.BLiveClient, command: dict):
        raise NotImplementedError


class BaseHandler:
    """
    一个简单的消息处理器实现，带消息分发和消息类型转换。继承并重写_on_xxx方法即可实现自己的处理器
    """

    def __heartbeat_callback(self, client: client_.BLiveClient, command: dict):
        return self._on_heartbeat(client, models.HeartbeatMessage.from_command(command['data']))

    def __danmu_msg_callback(self, client: client_.BLiveClient, command: dict):
        return self._on_danmaku(client, models.DanmakuMessage.from_command(command['info']))

    def __init__(self):
        self._cmd_callbacks = {
            '_HEARTBEAT': self.__heartbeat_callback,
            'DANMU_MSG': self.__danmu_msg_callback,
        }
        for ignore in IGNORED_CMDS:
            self._cmd_callbacks[ignore] = None

    async def handle(self, client: client_.BLiveClient, command: dict):
        cmd = command.get('cmd', '')
        pos = cmd.find(':')  # 2019-5-29 B站弹幕升级新增了参数
        if pos != -1:
            cmd = cmd[:pos]

        try:
            model: models.CommandModel = parse_obj_as(Union[tuple(models.CommandModel.__subclasses__())], command)
            if hasattr(self, "_on_" + model.cmd.lower()):
                return await getattr(self, "_on_" + model.cmd.lower())(client, model)
            else:
                # correctly parsed but no _on_* method, skip.
                return
        except ValidationError:
            if cmd in self._cmd_callbacks:
                callback = self._cmd_callbacks[cmd]
                if callback is not None:
                    await callback(client, command)
            else:
                self._cmd_callbacks[cmd] = None  # ignores
                print("[%d] unknown cmd `%s`", client.room_id, cmd)
                print(command)
                from rich.console import Console
                console = Console()
                console.print_exception()

    async def _on_heartbeat(self, client: client_.BLiveClient, message: models.HeartbeatMessage):
        """收到心跳包（人气值）"""

    async def _on_danmaku(self, client: client_.BLiveClient, message: models.DanmakuMessage):
        """收到弹幕"""

    async def _on_gift(self, client: client_.BLiveClient, message: models.GiftMessage):
        """收到礼物"""

    async def _on_buy_guard(self, client: client_.BLiveClient, message: models.GuardBuyMessage):
        """有人上舰"""

    async def _on_super_chat(self, client: client_.BLiveClient, message: models.SuperChatMessage):
        """醒目留言"""

    async def _on_super_chat_delete(self, client: client_.BLiveClient, message: models.SuperChatDeleteMessage):
        """删除醒目留言"""

    async def _on_room_change(self, client: client_.BLiveClient, message: models.RoomChangeMessage):
        """房间信息改变"""

    async def _on_live(self, client: client_.BLiveClient, message: models.LiveCommand):
        """开始直播"""

    async def _on_preparing(self, client: client_.BLiveClient, message: models.PreparingCommand):
        """直播准备中"""
