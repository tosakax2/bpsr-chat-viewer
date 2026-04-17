from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipAttrSet(_message.Message):
    __slots__ = ("basic_attr", "advance_attr", "recast_attr", "rare_quality_attr")
    class BasicAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AdvanceAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RecastAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RareQualityAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASIC_ATTR_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_ATTR_FIELD_NUMBER: _ClassVar[int]
    RECAST_ATTR_FIELD_NUMBER: _ClassVar[int]
    RARE_QUALITY_ATTR_FIELD_NUMBER: _ClassVar[int]
    basic_attr: _containers.ScalarMap[int, int]
    advance_attr: _containers.ScalarMap[int, int]
    recast_attr: _containers.ScalarMap[int, int]
    rare_quality_attr: _containers.ScalarMap[int, int]
    def __init__(self, basic_attr: _Optional[_Mapping[int, int]] = ..., advance_attr: _Optional[_Mapping[int, int]] = ..., recast_attr: _Optional[_Mapping[int, int]] = ..., rare_quality_attr: _Optional[_Mapping[int, int]] = ...) -> None: ...
