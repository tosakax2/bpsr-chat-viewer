from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TotalFriendliness(_message.Message):
    __slots__ = ("level", "cur_exp", "update_time_stamp", "today_total_add_exps", "got_level_awards")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_EXP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    TODAY_TOTAL_ADD_EXPS_FIELD_NUMBER: _ClassVar[int]
    GOT_LEVEL_AWARDS_FIELD_NUMBER: _ClassVar[int]
    level: int
    cur_exp: int
    update_time_stamp: int
    today_total_add_exps: int
    got_level_awards: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, level: _Optional[int] = ..., cur_exp: _Optional[int] = ..., update_time_stamp: _Optional[int] = ..., today_total_add_exps: _Optional[int] = ..., got_level_awards: _Optional[_Iterable[int]] = ...) -> None: ...
