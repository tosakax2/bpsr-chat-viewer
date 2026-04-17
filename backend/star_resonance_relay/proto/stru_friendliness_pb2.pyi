from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Friendliness(_message.Message):
    __slots__ = ("level", "cur_exp", "update_time_stamp", "today_total_add_exps", "today_part_add_exps", "got_level_awards")
    class TodayPartAddExpsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_EXP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    TODAY_TOTAL_ADD_EXPS_FIELD_NUMBER: _ClassVar[int]
    TODAY_PART_ADD_EXPS_FIELD_NUMBER: _ClassVar[int]
    GOT_LEVEL_AWARDS_FIELD_NUMBER: _ClassVar[int]
    level: int
    cur_exp: int
    update_time_stamp: int
    today_total_add_exps: int
    today_part_add_exps: _containers.ScalarMap[int, int]
    got_level_awards: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, level: _Optional[int] = ..., cur_exp: _Optional[int] = ..., update_time_stamp: _Optional[int] = ..., today_total_add_exps: _Optional[int] = ..., today_part_add_exps: _Optional[_Mapping[int, int]] = ..., got_level_awards: _Optional[_Iterable[int]] = ...) -> None: ...
