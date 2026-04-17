import stru_compensation_record_pb2 as _stru_compensation_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompensationSeasonStatistics(_message.Message):
    __slots__ = ("week_data", "compensation", "max_climb_up_layer_id", "raid_boss_ids", "raid_boss_kill_time")
    class WeekDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_compensation_record_pb2.CompensationRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_compensation_record_pb2.CompensationRecord, _Mapping]] = ...) -> None: ...
    class CompensationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RaidBossKillTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    WEEK_DATA_FIELD_NUMBER: _ClassVar[int]
    COMPENSATION_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIMB_UP_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    RAID_BOSS_IDS_FIELD_NUMBER: _ClassVar[int]
    RAID_BOSS_KILL_TIME_FIELD_NUMBER: _ClassVar[int]
    week_data: _containers.MessageMap[int, _stru_compensation_record_pb2.CompensationRecord]
    compensation: _containers.ScalarMap[int, int]
    max_climb_up_layer_id: int
    raid_boss_ids: _containers.RepeatedScalarFieldContainer[int]
    raid_boss_kill_time: _containers.ScalarMap[int, int]
    def __init__(self, week_data: _Optional[_Mapping[int, _stru_compensation_record_pb2.CompensationRecord]] = ..., compensation: _Optional[_Mapping[int, int]] = ..., max_climb_up_layer_id: _Optional[int] = ..., raid_boss_ids: _Optional[_Iterable[int]] = ..., raid_boss_kill_time: _Optional[_Mapping[int, int]] = ...) -> None: ...
