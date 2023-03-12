from ._base import *


class FullNotice(BaseModel):
    background: str
    color: str
    highlight: str

    head_icon: str
    head_icon_fa: str
    head_icon_fan: int

    tail_icon: str
    tail_icon_fa: str
    tail_icon_fan: int

    time: int


class HalfNotice(BaseModel):
    background: str
    color: str
    highlight: str

    head_icon: str
    tail_icon: str

    time: int


class SideNotice(BaseModel):
    background: str
    border: str
    color: str
    highlight: str

    head_icon: str


class NoticeMsgCommandBase(CommandModel):
    cmd: Literal['NOTICE_MSG']
    msg_type: int


class NoticeMsgCommand1(NoticeMsgCommandBase):
    msg_type: Literal[1]


class NoticeMsgCommand2(NoticeMsgCommandBase):
    msg_type: Literal[2]

    msg_common: str
    msg_self: str
    roomid: int
    real_roomid: int
    notice_type: int
    shield_uid: int
    id: int
    name: str
    business_id: int
    marquee_id: int

    side: SideNotice
    full: FullNotice
    half: HalfNotice

    scatter: Scatter


class NoticeMsgCommand6(NoticeMsgCommandBase):
    msg_type: Literal[6]

    msg_common: str
    msg_self: str

    roomid: int
    real_roomid: int
    link_url: str

    full: FullNotice
    half: HalfNotice

    def summarize(self) -> Summary:
        return Summary(
            t=self.ct,
            msg=self.msg_common.strip() or self.msg_self.strip() or repr(self),
            room_id=self.real_roomid,
            raw=self,
        )


NoticeMsgCommand = Annotated[Union[
    NoticeMsgCommand1, NoticeMsgCommand2, NoticeMsgCommand6
], Field(discriminator='msg_type')]
