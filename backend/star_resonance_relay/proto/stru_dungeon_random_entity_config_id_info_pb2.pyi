from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonRandomEntityConfigIdInfo(_message.Message):
    __slots__ = ("random_entity_map",)
    class RandomEntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    RANDOM_ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    random_entity_map: _containers.ScalarMap[int, int]
    def __init__(self, random_entity_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
