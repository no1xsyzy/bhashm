# -*- coding: utf-8 -*-

from ._base import *
from .anchor_lot import AnchorLotStartCommand, AnchorLotCheckStatusCommand, AnchorLotEndCommand, AnchorLotAwardCommand
from .area_rank_changed import AreaRankChangedCommand
from .combo_send import ComboSendCommand
from .common_notice_danmaku import CommonNoticeDanmakuCommand
from .danmu_aggregation import DanmuAggregationCommand
from .danmu_msg import DanmakuCommand
from .entry_effect import EntryEffectCommand
from .gift_star_process import GiftStarProcessCommand
from .guard_buy import GuardBuyCommand
from .guard_honor_thousand import GuardHonorThousandCommand
from .heartbeat import HeartbeatCommand
from .hot_rank_settlement import HotRankSettlementCommand, HotRankSettlementV2Command
from .interact_word import InteractWordCommand
from .live import LiveCommand
from .live_multi_view_change import LiveMultiViewChangeCommand
from .notice_msg import NoticeMsgCommand
from .online_rank_count import OnlineRankCountCommand
from .preparing import PreparingCommand
from .ring_status_change import RingStatusChangeCommand, RingStatusChangeCommandV2
from .room_admin_entrace import RoomAdminEntranceCommand
from .room_admins import RoomAdminsCommand
from .room_block_msg import RoomBlockCommand
from .room_change import RoomChangeCommand
from .room_skin_msg import RoomSkinCommand
from .send_gift import GiftCommand
from .special_gift import SpecialGiftCommand
from .stop_live_room_list import StopLiveRoomListCommand
from .super_chat_entrance import SuperChatEntranceCommand
from .super_chat_message import SuperChatCommand
from .super_chat_message_delete import SuperChatDeleteCommand
from .sys_msg import SysMsgCommand
from .trading_score import TradingScoreCommand
from .user_toast_msg import UserToastMsgCommand
from .warning import WarningCommand
from .watched_change import WatchedChangeCommand
from .widget_gift_star_process import WidgetGiftStarProcessCommand

AnnotatedCommandModel = Annotated[Union[
    AnchorLotStartCommand, AnchorLotCheckStatusCommand, AnchorLotEndCommand, AnchorLotAwardCommand,
    AreaRankChangedCommand,
    ComboSendCommand,
    CommonNoticeDanmakuCommand,
    DanmuAggregationCommand,
    DanmakuCommand,
    EntryEffectCommand,
    GiftStarProcessCommand,
    GuardBuyCommand,
    GuardHonorThousandCommand,
    HeartbeatCommand,
    HotRankSettlementCommand, HotRankSettlementV2Command,
    InteractWordCommand,
    LiveCommand,
    LiveMultiViewChangeCommand,
    NoticeMsgCommand,
    OnlineRankCountCommand,
    PreparingCommand,
    RingStatusChangeCommand, RingStatusChangeCommandV2,
    RoomAdminEntranceCommand,
    RoomAdminsCommand,
    RoomBlockCommand,
    RoomChangeCommand,
    RoomSkinCommand,
    GiftCommand,
    SpecialGiftCommand,
    StopLiveRoomListCommand,
    SuperChatEntranceCommand,
    SuperChatCommand,
    SuperChatDeleteCommand,
    SysMsgCommand,
    TradingScoreCommand,
    UserToastMsgCommand,
    WarningCommand,
    WatchedChangeCommand,
    WidgetGiftStarProcessCommand
], Field(discriminator='cmd')]

__all__ = (
    'AnchorLotStartCommand', 'AnchorLotCheckStatusCommand', 'AnchorLotEndCommand', 'AnchorLotAwardCommand',
    'AreaRankChangedCommand',
    'ComboSendCommand',
    'CommonNoticeDanmakuCommand',
    'DanmuAggregationCommand',
    'DanmakuCommand',
    'EntryEffectCommand',
    'GiftStarProcessCommand',
    'GuardBuyCommand',
    'GuardHonorThousandCommand',
    'HeartbeatCommand',
    'HotRankSettlementCommand', 'HotRankSettlementV2Command',
    'InteractWordCommand',
    'LiveCommand',
    'LiveMultiViewChangeCommand',
    'NoticeMsgCommand',
    'OnlineRankCountCommand',
    'PreparingCommand',
    'RingStatusChangeCommand', 'RingStatusChangeCommandV2',
    'RoomAdminEntranceCommand',
    'RoomAdminsCommand',
    'RoomBlockCommand',
    'RoomChangeCommand',
    'RoomSkinCommand',
    'GiftCommand',
    'SpecialGiftCommand',
    'StopLiveRoomListCommand',
    'SuperChatEntranceCommand',
    'SuperChatCommand',
    'SuperChatDeleteCommand',
    'SysMsgCommand',
    'TradingScoreCommand',
    'UserToastMsgCommand',
    'WarningCommand',
    'WatchedChangeCommand',
    'WidgetGiftStarProcessCommand',
    'AnnotatedCommandModel', 'Summary', 'Summarizer', 'CommandModel',
)
