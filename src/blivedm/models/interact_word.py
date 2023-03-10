from ._base import *


class FansMedal(BaseModel):
    anchor_roomid: int
    guard_level: int
    icon_id: int
    is_lighted: int
    medal_color: Color
    medal_color_border: Color
    medal_color_end: Color
    medal_color_start: Color
    medal_level: int
    medal_name: str
    score: int
    special: str
    target_id: int


class Contribution(BaseModel):
    grade: int


class InteractWordData(BaseModel):
    contribution: Contribution
    core_user_type: int
    dmscore: int
    fans_medal: FansMedal
    identities: list[int]
    is_spread: int
    msg_type: int
    """1=进入，2=关注，3=分享，4=特别关注，5=互相关注"""
    privilege_type: int
    score: datetime
    spread_desc: str
    spread_info: str
    tail_icon: int
    timestamp: datetime
    trigger_time: datetime
    uid: int
    uname: str
    uname_color: str


class InteractWordCommand(CommandModel):
    cmd: Literal['INTERACT_WORD']
    data: InteractWordData

    def summarize(self):
        msg = {
            1: '进入',
            2: '关注',
            3: '分享',
            4: '特别关注',
            5: '互相关注',
        }.get(self.data.msg_type, "msg_type=" + str(self.data.msg_type))

        return Summary(
            t=self.data.timestamp,
            msg=msg,
            user=(self.data.uid, self.data.uname),
            raw=self,
        )
