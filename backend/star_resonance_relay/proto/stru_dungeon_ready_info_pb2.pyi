import stru_dungeon_ready_buffer_info_pb2 as _stru_dungeon_ready_buffer_info_pb2
import stru_dungeon_ready_item_info_pb2 as _stru_dungeon_ready_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonReadyInfo(_message.Message):
    __slots__ = ("is_ready", "buffs", "medicaments", "items")
    IS_READY_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    MEDICAMENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    is_ready: bool
    buffs: _containers.RepeatedCompositeFieldContainer[_stru_dungeon_ready_buffer_info_pb2.DungeonReadyBufferInfo]
    medicaments: _containers.RepeatedCompositeFieldContainer[_stru_dungeon_ready_item_info_pb2.DungeonReadyItemInfo]
    items: _containers.RepeatedCompositeFieldContainer[_stru_dungeon_ready_item_info_pb2.DungeonReadyItemInfo]
    def __init__(self, is_ready: bool = ..., buffs: _Optional[_Iterable[_Union[_stru_dungeon_ready_buffer_info_pb2.DungeonReadyBufferInfo, _Mapping]]] = ..., medicaments: _Optional[_Iterable[_Union[_stru_dungeon_ready_item_info_pb2.DungeonReadyItemInfo, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_stru_dungeon_ready_item_info_pb2.DungeonReadyItemInfo, _Mapping]]] = ...) -> None: ...
