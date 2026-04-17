from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FriendlinessExpLevel(_message.Message):
    __slots__ = ("friend_id", "level", "cur_exp", "today_add_exps")
    FRIEND_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_EXP_FIELD_NUMBER: _ClassVar[int]
    TODAY_ADD_EXPS_FIELD_NUMBER: _ClassVar[int]
    friend_id: int
    level: int
    cur_exp: int
    today_add_exps: int
    def __init__(self, friend_id: _Optional[int] = ..., level: _Optional[int] = ..., cur_exp: _Optional[int] = ..., today_add_exps: _Optional[int] = ...) -> None: ...
