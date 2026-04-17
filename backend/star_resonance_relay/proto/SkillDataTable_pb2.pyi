import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillDataTableBase(_message.Message):
    __slots__ = ("s_kill_level_id", "action_array", "event_array", "effect_array", "camera_array", "material_array", "audio_array", "bullet_array", "time_scale_array")
    S_KILL_LEVEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ARRAY_FIELD_NUMBER: _ClassVar[int]
    EVENT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ARRAY_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ARRAY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BULLET_ARRAY_FIELD_NUMBER: _ClassVar[int]
    TIME_SCALE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    s_kill_level_id: int
    action_array: _table_basic_pb2.int64_array
    event_array: _table_basic_pb2.int64_array
    effect_array: _table_basic_pb2.int64_array
    camera_array: _table_basic_pb2.int64_array
    material_array: _table_basic_pb2.int64_array
    audio_array: _table_basic_pb2.int64_array
    bullet_array: _table_basic_pb2.int64_array
    time_scale_array: _table_basic_pb2.int64_array
    def __init__(self, s_kill_level_id: _Optional[int] = ..., action_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., event_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., effect_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., camera_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., material_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., audio_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., bullet_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., time_scale_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ...) -> None: ...

class SkillDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SkillDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SkillDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SkillDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SkillDataTableBase]] = ...) -> None: ...
