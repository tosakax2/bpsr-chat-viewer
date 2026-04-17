import enum_e_dungeon_state_pb2 as _enum_e_dungeon_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonFlowInfo(_message.Message):
    __slots__ = ("state", "active_time", "ready_time", "play_time", "end_time", "settlement_time", "dungeon_times", "result")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    READY_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAY_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_TIMES_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    state: _enum_e_dungeon_state_pb2.EDungeonState
    active_time: int
    ready_time: int
    play_time: int
    end_time: int
    settlement_time: int
    dungeon_times: int
    result: int
    def __init__(self, state: _Optional[_Union[_enum_e_dungeon_state_pb2.EDungeonState, str]] = ..., active_time: _Optional[int] = ..., ready_time: _Optional[int] = ..., play_time: _Optional[int] = ..., end_time: _Optional[int] = ..., settlement_time: _Optional[int] = ..., dungeon_times: _Optional[int] = ..., result: _Optional[int] = ...) -> None: ...
