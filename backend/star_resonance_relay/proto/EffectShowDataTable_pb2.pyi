import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EffectShowDataTableBase(_message.Message):
    __slots__ = ("id", "start", "duration", "end", "is_attacker", "state_id", "group_id", "fx_path", "fx_name", "attach", "end_attach", "fadeout_time", "scale", "rotate", "offset", "bind_bone", "bind_position", "break_clear", "is_target_pos", "bind_target")
    ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    FX_PATH_FIELD_NUMBER: _ClassVar[int]
    FX_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACH_FIELD_NUMBER: _ClassVar[int]
    END_ATTACH_FIELD_NUMBER: _ClassVar[int]
    FADEOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BIND_BONE_FIELD_NUMBER: _ClassVar[int]
    BIND_POSITION_FIELD_NUMBER: _ClassVar[int]
    BREAK_CLEAR_FIELD_NUMBER: _ClassVar[int]
    IS_TARGET_POS_FIELD_NUMBER: _ClassVar[int]
    BIND_TARGET_FIELD_NUMBER: _ClassVar[int]
    id: int
    start: float
    duration: float
    end: float
    is_attacker: bool
    state_id: int
    group_id: int
    fx_path: str
    fx_name: str
    attach: str
    end_attach: str
    fadeout_time: float
    scale: _table_basic_pb2.vector3
    rotate: _table_basic_pb2.vector3
    offset: _table_basic_pb2.vector3
    bind_bone: bool
    bind_position: bool
    break_clear: bool
    is_target_pos: bool
    bind_target: bool
    def __init__(self, id: _Optional[int] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., end: _Optional[float] = ..., is_attacker: bool = ..., state_id: _Optional[int] = ..., group_id: _Optional[int] = ..., fx_path: _Optional[str] = ..., fx_name: _Optional[str] = ..., attach: _Optional[str] = ..., end_attach: _Optional[str] = ..., fadeout_time: _Optional[float] = ..., scale: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., rotate: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., offset: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., bind_bone: bool = ..., bind_position: bool = ..., break_clear: bool = ..., is_target_pos: bool = ..., bind_target: bool = ...) -> None: ...

class EffectShowDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EffectShowDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EffectShowDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EffectShowDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EffectShowDataTableBase]] = ...) -> None: ...
