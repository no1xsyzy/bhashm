from pydantic import parse_obj_as

from blivedm import models


def test_danmu_msg():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'DANMU_MSG',
            'info': [
                [
                    0, 4, 25, 14893055, 1676125072976, 1676124883, 0, "98095d8b", 0, 0, 5,
                    "#1453BAFF,#4C2263A2,#3353BAFF", 0, "{}", "{}",
                    {
                        "mode": 0, "show_player_type": 0,
                        "extra": "{\"send_from_me\":false,\"mode\":0,\"color\":14893055,\"dm_type\":0,\"font_size\":25,\"player_mode\":4,\"show_player_type\":0,\"content\":\"？\",\"user_hash\":\"2550750603\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":0,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null}"
                    },
                    {"activity_identity": "", "activity_source": 0, "not_show": 0}
                ],
                "？",
                [2351778, "橘枳橼", 0, 0, 0, 10000, 1, "#00D1F1"],
                [13, "降智了", "弱智光环", 8765806, 12478086, "", 0, 12478086, 12478086, 12478086, 0, 1, 531251],
                [23, 0, 5805790, ">50000", 2],
                ["", ""],
                0, 3, None,
                {"ts": 1676125072, "ct": "1E12C41B"},
                0, 0, None, None, 0, 105,
            ],
        }
    )
    assert isinstance(c, models.DanmakuCommand)

    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'DANMU_MSG',
            'info': [
                [
                    0, 1, 25, 16777215, 1676564740293, -793983239, 0, '507d1d44', 0, 0, 0, '', 0, '{}', '{}',
                    {
                        'mode': 0, 'show_player_type': 0,
                        'extra': '{"send_from_me":false,"mode":0,"color":16777215,"dm_type":0,"font_size":25,"player_mode":1,"show_player_type":0,"content":"[妙]","user_hash":"1350376772","emoticon_unique":"","bulge_display":0,"recommend_score":1,"main_state_dm_color":"","objective_state_dm_color":"","direction":0,"pk_direction":0,"quartet_direction":0,"anniversary_crowd":0,"yeah_space_type":"","yeah_space_url":"","jump_to_url":"","space_type":"","space_url":"","animation":{},"emots":{"[妙]":{"emoticon_id":210,"emoji":"[妙]","descript":"[妙]","url":"http://i0.hdslb.com/bfs/live/08f735d950a0fba267dda140673c9ab2edf6410d.png","width":20,"height":20,"emoticon_unique":"emoji_210","count":1}},"is_audited":false}'
                    },
                    {'activity_identity': '', 'activity_source': 0, 'not_show': 0}
                ],
                '[妙]',
                [1753368819, '撸喵日常', 0, 0, 0, 10000, 1, ''],
                [11, '煤球怪', '踏雪寻梅3124', 666816, 9272486, '', 0, 12632256, 12632256, 12632256, 0, 0, 17393811],
                [1, 0, 9868950, '>50000', 0],
                ['', ''],
                0, 0, None,
                {'ts': 1676564740, 'ct': '9571FBCC'},
                0, 0, None, None, 0, 42
            ],
            'dm_v2': 'CPmNs4X9/////wESDzgxMDA0LTc5Mzk4MzIzORgBIBko////BzIINTA3ZDFkNDQ6BVvlppldQMXxrtjlMFD5jbOF/f////8BagB6YwoFW+WmmV0SWgoJZW1vamlfMjEwEklodHRwOi8vaTAuaGRzbGIuY29tL2Jmcy9saXZlLzA4ZjczNWQ5NTBhMGZiYTI2N2RkYTE0MDY3M2M5YWIyZWRmNjQxMGQucG5nMBQ4FJIBAA=='
        }
    )

    assert isinstance(c, models.DanmakuCommand)


def test_super_chat_message():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'SUPER_CHAT_MESSAGE',
            'data': {
                "background_bottom_color": "#2A60B2",
                "background_color": "#EDF5FF",
                "background_color_end": "#405D85",
                "background_color_start": "#3171D2",
                "background_icon": "",
                "background_image": "https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png",
                "background_price_color": "#7497CD",
                "color_point": 0.7,
                "dmscore": 120,
                "end_time": 1676124994,
                "gift": {
                    "gift_id": 12000,
                    "gift_name": "醒目留言",
                    "num": 1
                },
                "id": 6419133,
                "is_ranked": 1,
                "is_send_audit": 0,
                "medal_info": {
                    "anchor_roomid": 8765806,
                    "anchor_uname": "弱智光环",
                    "guard_level": 0,
                    "icon_id": 0,
                    "is_lighted": 1,
                    "medal_color": "#be6686",
                    "medal_color_border": 12478086,
                    "medal_color_end": 12478086,
                    "medal_color_start": 12478086,
                    "medal_level": 13,
                    "medal_name": "降智了",
                    "special": "",
                    "target_id": 531251
                },
                "message": "因为TCP的设计，上行和下行在接近极限的时候会相互卡住的，不过通常不会触到这个点",
                "message_font_color": "#A3F6FF",
                "message_trans": "",
                "price": 30,
                "rate": 1000,
                "start_time": 1676124934,
                "time": 59,
                "token": "30EB0101",
                "trans_mark": 0,
                "ts": 1676124935,
                "uid": 2351778,
                "user_info": {
                    "face": "https://i0.hdslb.com/bfs/face/757b6263c974aba03784fdbbe0d37c782f4c2045.jpg",
                    "face_frame": "https://i0.hdslb.com/bfs/live/80f732943cc3367029df65e267960d56736a82ee.png",
                    "guard_level": 3,
                    "is_main_vip": 1,
                    "is_svip": 0, "is_vip": 0, "level_color": "#5896de", "manager": 0, "name_color": "#00D1F1",
                    "title": "0", "uname": "橘枳橼", "user_level": 23
                }
            },
            'roomid': 81004
        }
    )
    assert isinstance(c, models.SuperChatCommand)


def test_live_multi_view_change():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'LIVE_MULTI_VIEW_CHANGE',
            'data': {
                'scatter': {
                    'max': 120,
                    'min': 5
                }
            }
        }
    )
    assert isinstance(c, models.LiveMultiViewChangeCommand)


def test_anchor_lot_start():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'ANCHOR_LOT_START',
            'data': {
                'asset_icon': 'https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png',
                'asset_icon_webp': 'https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp',
                'award_image': '',
                'award_name': '白象方便面整箱',
                'award_num': 1,
                'award_type': 0,
                'cur_gift_num': 0,
                'current_time': 1677154113,
                'danmu': '不是白象我不吃',
                'danmu_new': [{
                    'danmu': '不是白象我不吃',
                    'danmu_view': '',
                    'reject': False
                }],
                'danmu_type': 0,
                'gift_id': 0,
                'gift_name': '',
                'gift_num': 1,
                'gift_price': 0,
                'goaway_time': 180,
                'goods_id': -99998,
                'id': 3940775,
                'is_broadcast': 1,
                'join_type': 0,
                'lot_status': 0,
                'max_time': 300,
                'require_text': '至少成为主播的舰长',
                'require_type': 3,
                'require_value': 3,
                'room_id': 81004,
                'send_gift_ensure': 0,
                'show_panel': 1,
                'start_dont_popup': 0,
                'status': 1,
                'time': 299,
                'url': 'https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1',
                'web_url': 'https://live.bilibili.com/p/html/live-lottery/anchor-join.html'
            }
        }

    )
    assert isinstance(c, models.AnchorLotStartCommand)


def test_anchor_lot_award():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'ANCHOR_LOT_AWARD',
            'data': {
                'award_dont_popup': 1,
                'award_image': '',
                'award_name': '白象方便面整箱',
                'award_num': 1,
                'award_type': 0,
                'award_users': [{
                    'uid': 1728860,
                    'uname': '街巷角落の黑猫',
                    'face': 'https://i2.hdslb.com/bfs/face/fd3055766c289a77d83d036457a8f886a70bbbed.jpg',
                    'level': 46,
                    'color': 16746162,
                    'num': 1
                }],
                'id': 3940775,
                'lot_status': 2,
                'url': 'https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1',
                'web_url': 'https://live.bilibili.com/p/html/live-lottery/anchor-join.html'
            }
        }
    )
    assert isinstance(c, models.AnchorLotAwardCommand)


def test_anchor_lot_end():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'ANCHOR_LOT_END',
            'data': {
                'id': 3940879
            }
        }
    )
    assert isinstance(c, models.AnchorLotEndCommand)


def test_anchor_lot_checkstatus():
    c = parse_obj_as(
        models.AnnotatedCommandModel,
        {
            'cmd': 'ANCHOR_LOT_CHECKSTATUS',
            'data': {
                'id': 3941001,
                'status': 4,
                'uid': 1521415
            }
        }
    )
    assert isinstance(c, models.AnchorLotCheckStatusCommand)
