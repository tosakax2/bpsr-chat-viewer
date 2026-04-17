from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishRecord(_message.Message):
    __slots__ = ("fish_id", "first_flag", "size", "millisecond", "research", "count", "min_size", "min_sizemillisecond", "star_cnts")
    class StarCntsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_FLAG_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MILLISECOND_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_SIZEMILLISECOND_FIELD_NUMBER: _ClassVar[int]
    STAR_CNTS_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    first_flag: bool
    size: int
    millisecond: int
    research: int
    count: int
    min_size: int
    min_sizemillisecond: int
    star_cnts: _containers.ScalarMap[int, int]
    def __init__(self, fish_id: _Optional[int] = ..., first_flag: bool = ..., size: _Optional[int] = ..., millisecond: _Optional[int] = ..., research: _Optional[int] = ..., count: _Optional[int] = ..., min_size: _Optional[int] = ..., min_sizemillisecond: _Optional[int] = ..., star_cnts: _Optional[_Mapping[int, int]] = ...) -> None: ...
