import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraShowDataTableBase(_message.Message):
    __slots__ = ("id", "start", "duration", "end", "is_attacker", "state_id", "group_id", "camera_effect_type", "frequency", "amplitude", "frequency_curve", "amplitude_curve", "only_caster", "max_distance", "distance_curve", "intensity", "intensity_curve", "threshold", "is_random", "extra_parms")
    ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    AMPLITUDE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_CURVE_FIELD_NUMBER: _ClassVar[int]
    AMPLITUDE_CURVE_FIELD_NUMBER: _ClassVar[int]
    ONLY_CASTER_FIELD_NUMBER: _ClassVar[int]
    MAX_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_CURVE_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_CURVE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    EXTRA_PARMS_FIELD_NUMBER: _ClassVar[int]
    id: int
    start: float
    duration: float
    end: float
    is_attacker: bool
    state_id: int
    group_id: int
    camera_effect_type: int
    frequency: float
    amplitude: _table_basic_pb2.vector3
    frequency_curve: _table_basic_pb2.number_table
    amplitude_curve: _table_basic_pb2.number_table
    only_caster: bool
    max_distance: float
    distance_curve: _table_basic_pb2.number_table
    intensity: float
    intensity_curve: _table_basic_pb2.number_table
    threshold: float
    is_random: bool
    extra_parms: _table_basic_pb2.number_array
    def __init__(self, id: _Optional[int] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., end: _Optional[float] = ..., is_attacker: bool = ..., state_id: _Optional[int] = ..., group_id: _Optional[int] = ..., camera_effect_type: _Optional[int] = ..., frequency: _Optional[float] = ..., amplitude: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., frequency_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., amplitude_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., only_caster: bool = ..., max_distance: _Optional[float] = ..., distance_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., intensity: _Optional[float] = ..., intensity_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., threshold: _Optional[float] = ..., is_random: bool = ..., extra_parms: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ...) -> None: ...

class CameraShowDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CameraShowDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CameraShowDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CameraShowDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CameraShowDataTableBase]] = ...) -> None: ...
