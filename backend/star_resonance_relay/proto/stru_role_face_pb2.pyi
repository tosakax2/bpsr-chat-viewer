from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoleFace(_message.Message):
    __slots__ = ("unlock_item_map", "save_need_consume", "unlock_voice_ids")
    class UnlockItemMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    UNLOCK_ITEM_MAP_FIELD_NUMBER: _ClassVar[int]
    SAVE_NEED_CONSUME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_VOICE_IDS_FIELD_NUMBER: _ClassVar[int]
    unlock_item_map: _containers.ScalarMap[int, bool]
    save_need_consume: bool
    unlock_voice_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlock_item_map: _Optional[_Mapping[int, bool]] = ..., save_need_consume: bool = ..., unlock_voice_ids: _Optional[_Iterable[int]] = ...) -> None: ...
