import stru_dungeon_event_data_pb2 as _stru_dungeon_event_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEvent(_message.Message):
    __slots__ = ("dungeon_event_data",)
    class DungeonEventDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_event_data_pb2.DungeonEventData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_event_data_pb2.DungeonEventData, _Mapping]] = ...) -> None: ...
    DUNGEON_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    dungeon_event_data: _containers.MessageMap[int, _stru_dungeon_event_data_pb2.DungeonEventData]
    def __init__(self, dungeon_event_data: _Optional[_Mapping[int, _stru_dungeon_event_data_pb2.DungeonEventData]] = ...) -> None: ...
