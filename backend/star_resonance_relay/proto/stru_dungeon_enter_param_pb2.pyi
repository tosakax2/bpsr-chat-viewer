from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEnterParam(_message.Message):
    __slots__ = ("play_type", "dungeon_id", "room_id", "affix", "select_type", "hero_key_item_uuid", "master_mode_diff")
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    SELECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HERO_KEY_ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    MASTER_MODE_DIFF_FIELD_NUMBER: _ClassVar[int]
    play_type: int
    dungeon_id: int
    room_id: int
    affix: _containers.RepeatedScalarFieldContainer[int]
    select_type: int
    hero_key_item_uuid: int
    master_mode_diff: int
    def __init__(self, play_type: _Optional[int] = ..., dungeon_id: _Optional[int] = ..., room_id: _Optional[int] = ..., affix: _Optional[_Iterable[int]] = ..., select_type: _Optional[int] = ..., hero_key_item_uuid: _Optional[int] = ..., master_mode_diff: _Optional[int] = ...) -> None: ...
