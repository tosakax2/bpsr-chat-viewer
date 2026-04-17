import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JumpTableBase(_message.Message):
    __slots__ = ("id", "default_speed", "operate_speed", "re_operate_default_speed", "wind_drag_coefficient", "amended_gravity", "jump_time", "prepare_time", "jump_break_time", "move_path", "shader_brightness", "shader_length", "shader_is_breath", "energy_consume")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SPEED_FIELD_NUMBER: _ClassVar[int]
    OPERATE_SPEED_FIELD_NUMBER: _ClassVar[int]
    RE_OPERATE_DEFAULT_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_DRAG_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    AMENDED_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    JUMP_TIME_FIELD_NUMBER: _ClassVar[int]
    PREPARE_TIME_FIELD_NUMBER: _ClassVar[int]
    JUMP_BREAK_TIME_FIELD_NUMBER: _ClassVar[int]
    MOVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHADER_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    SHADER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SHADER_IS_BREATH_FIELD_NUMBER: _ClassVar[int]
    ENERGY_CONSUME_FIELD_NUMBER: _ClassVar[int]
    id: int
    default_speed: float
    operate_speed: float
    re_operate_default_speed: float
    wind_drag_coefficient: _table_basic_pb2.number_array
    amended_gravity: float
    jump_time: _table_basic_pb2.number_array
    prepare_time: _table_basic_pb2.number_array
    jump_break_time: _table_basic_pb2.number_array
    move_path: str
    shader_brightness: _table_basic_pb2.number_array
    shader_length: _table_basic_pb2.number_array
    shader_is_breath: _table_basic_pb2.int_array
    energy_consume: _table_basic_pb2.number_array
    def __init__(self, id: _Optional[int] = ..., default_speed: _Optional[float] = ..., operate_speed: _Optional[float] = ..., re_operate_default_speed: _Optional[float] = ..., wind_drag_coefficient: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., amended_gravity: _Optional[float] = ..., jump_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., prepare_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., jump_break_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., move_path: _Optional[str] = ..., shader_brightness: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., shader_length: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., shader_is_breath: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., energy_consume: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ...) -> None: ...

class JumpTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: JumpTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[JumpTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, JumpTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, JumpTableBase]] = ...) -> None: ...
