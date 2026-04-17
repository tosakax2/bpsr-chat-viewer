from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipSuitInfo(_message.Message):
    __slots__ = ("suit_attr", "attr_type")
    class SuitAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SUIT_ATTR_FIELD_NUMBER: _ClassVar[int]
    ATTR_TYPE_FIELD_NUMBER: _ClassVar[int]
    suit_attr: _containers.ScalarMap[int, int]
    attr_type: int
    def __init__(self, suit_attr: _Optional[_Mapping[int, int]] = ..., attr_type: _Optional[int] = ...) -> None: ...
