import enum_e_dungeon_timer_direction_pb2 as _enum_e_dungeon_timer_direction_pb2
import enum_e_dungeon_timer_effect_type_pb2 as _enum_e_dungeon_timer_effect_type_pb2
import enum_e_dungeon_timer_timer_look_type_pb2 as _enum_e_dungeon_timer_timer_look_type_pb2
import enum_e_dungeon_timer_type_pb2 as _enum_e_dungeon_timer_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTimerInfo(_message.Message):
    __slots__ = ("type", "start_time", "dungeon_times", "direction", "index", "change_time", "effect_type", "pause_time", "pause_total_time", "out_look_type", "cur_pause_timestamp")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_TIMES_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_TIME_FIELD_NUMBER: _ClassVar[int]
    PAUSE_TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
    OUT_LOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUR_PAUSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_dungeon_timer_type_pb2.EDungeonTimerType
    start_time: int
    dungeon_times: int
    direction: _enum_e_dungeon_timer_direction_pb2.EDungeonTimerDirection
    index: int
    change_time: int
    effect_type: _enum_e_dungeon_timer_effect_type_pb2.EDungeonTimerEffectType
    pause_time: int
    pause_total_time: int
    out_look_type: _enum_e_dungeon_timer_timer_look_type_pb2.EDungeonTimerTimerLookType
    cur_pause_timestamp: int
    def __init__(self, type: _Optional[_Union[_enum_e_dungeon_timer_type_pb2.EDungeonTimerType, str]] = ..., start_time: _Optional[int] = ..., dungeon_times: _Optional[int] = ..., direction: _Optional[_Union[_enum_e_dungeon_timer_direction_pb2.EDungeonTimerDirection, str]] = ..., index: _Optional[int] = ..., change_time: _Optional[int] = ..., effect_type: _Optional[_Union[_enum_e_dungeon_timer_effect_type_pb2.EDungeonTimerEffectType, str]] = ..., pause_time: _Optional[int] = ..., pause_total_time: _Optional[int] = ..., out_look_type: _Optional[_Union[_enum_e_dungeon_timer_timer_look_type_pb2.EDungeonTimerTimerLookType, str]] = ..., cur_pause_timestamp: _Optional[int] = ...) -> None: ...
