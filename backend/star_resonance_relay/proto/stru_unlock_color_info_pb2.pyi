from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockColorInfo(_message.Message):
    __slots__ = ("color_info_map", "color_block_info_map")
    class ColorInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ColorBlockInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    COLOR_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    COLOR_BLOCK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    color_info_map: _containers.ScalarMap[int, bool]
    color_block_info_map: _containers.ScalarMap[int, bool]
    def __init__(self, color_info_map: _Optional[_Mapping[int, bool]] = ..., color_block_info_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...
