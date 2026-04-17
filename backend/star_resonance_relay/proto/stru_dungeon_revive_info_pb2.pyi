from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonReviveInfo(_message.Message):
    __slots__ = ("revive_ids", "revive_map")
    class ReviveMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    REVIVE_IDS_FIELD_NUMBER: _ClassVar[int]
    REVIVE_MAP_FIELD_NUMBER: _ClassVar[int]
    revive_ids: _containers.RepeatedScalarFieldContainer[int]
    revive_map: _containers.ScalarMap[int, int]
    def __init__(self, revive_ids: _Optional[_Iterable[int]] = ..., revive_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
