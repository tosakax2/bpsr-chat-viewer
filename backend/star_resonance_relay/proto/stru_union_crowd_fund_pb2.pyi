from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionCrowdFund(_message.Message):
    __slots__ = ("fund_begin_time", "fund_pos_char_id", "build_end_time", "building_finished", "fund_has_begin")
    class FundPosCharIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FUND_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    FUND_POS_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_END_TIME_FIELD_NUMBER: _ClassVar[int]
    BUILDING_FINISHED_FIELD_NUMBER: _ClassVar[int]
    FUND_HAS_BEGIN_FIELD_NUMBER: _ClassVar[int]
    fund_begin_time: int
    fund_pos_char_id: _containers.ScalarMap[int, int]
    build_end_time: int
    building_finished: bool
    fund_has_begin: bool
    def __init__(self, fund_begin_time: _Optional[int] = ..., fund_pos_char_id: _Optional[_Mapping[int, int]] = ..., build_end_time: _Optional[int] = ..., building_finished: bool = ..., fund_has_begin: bool = ...) -> None: ...
