import stru_dungeon_area_data_pb2 as _stru_dungeon_area_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonAreaInfo(_message.Message):
    __slots__ = ("dungeon_area_data_map",)
    class DungeonAreaDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_area_data_pb2.DungeonAreaData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_area_data_pb2.DungeonAreaData, _Mapping]] = ...) -> None: ...
    DUNGEON_AREA_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    dungeon_area_data_map: _containers.MessageMap[int, _stru_dungeon_area_data_pb2.DungeonAreaData]
    def __init__(self, dungeon_area_data_map: _Optional[_Mapping[int, _stru_dungeon_area_data_pb2.DungeonAreaData]] = ...) -> None: ...
