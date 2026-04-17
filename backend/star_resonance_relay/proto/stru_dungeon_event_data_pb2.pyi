import enum_dungeon_event_result_pb2 as _enum_dungeon_event_result_pb2
import enum_dungeon_event_state_pb2 as _enum_dungeon_event_state_pb2
import stru_dungeon_target_data_pb2 as _stru_dungeon_target_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEventData(_message.Message):
    __slots__ = ("event_id", "start_time", "state", "result", "dungeon_target")
    class DungeonTargetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_target_data_pb2.DungeonTargetData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_target_data_pb2.DungeonTargetData, _Mapping]] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_TARGET_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    start_time: int
    state: _enum_dungeon_event_state_pb2.DungeonEventState
    result: _enum_dungeon_event_result_pb2.DungeonEventResult
    dungeon_target: _containers.MessageMap[int, _stru_dungeon_target_data_pb2.DungeonTargetData]
    def __init__(self, event_id: _Optional[int] = ..., start_time: _Optional[int] = ..., state: _Optional[_Union[_enum_dungeon_event_state_pb2.DungeonEventState, str]] = ..., result: _Optional[_Union[_enum_dungeon_event_result_pb2.DungeonEventResult, str]] = ..., dungeon_target: _Optional[_Mapping[int, _stru_dungeon_target_data_pb2.DungeonTargetData]] = ...) -> None: ...
