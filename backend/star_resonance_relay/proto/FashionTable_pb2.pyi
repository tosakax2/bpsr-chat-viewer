import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FashionTableBase(_message.Message):
    __slots__ = ("id", "type", "sort_id", "model", "model2", "model_id", "fashion_type", "hide_part", "hair_id", "default_color", "color_part", "color_group_id", "is_hide", "arm_length", "arm_width", "waist_length", "waist_width", "leg_length", "leg_width", "switch_name", "headwear_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL2_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    FASHION_TYPE_FIELD_NUMBER: _ClassVar[int]
    HIDE_PART_FIELD_NUMBER: _ClassVar[int]
    HAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COLOR_FIELD_NUMBER: _ClassVar[int]
    COLOR_PART_FIELD_NUMBER: _ClassVar[int]
    COLOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_HIDE_FIELD_NUMBER: _ClassVar[int]
    ARM_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ARM_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WAIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    WAIST_WIDTH_FIELD_NUMBER: _ClassVar[int]
    LEG_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LEG_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SWITCH_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADWEAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    sort_id: int
    model: str
    model2: _table_basic_pb2.string_table
    model_id: str
    fashion_type: int
    hide_part: _table_basic_pb2.int_array
    hair_id: _table_basic_pb2.int_array
    default_color: _table_basic_pb2.int_table
    color_part: _table_basic_pb2.int_array
    color_group_id: int
    is_hide: int
    arm_length: int
    arm_width: int
    waist_length: int
    waist_width: int
    leg_length: int
    leg_width: int
    switch_name: str
    headwear_type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., sort_id: _Optional[int] = ..., model: _Optional[str] = ..., model2: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., model_id: _Optional[str] = ..., fashion_type: _Optional[int] = ..., hide_part: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., hair_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., default_color: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., color_part: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., color_group_id: _Optional[int] = ..., is_hide: _Optional[int] = ..., arm_length: _Optional[int] = ..., arm_width: _Optional[int] = ..., waist_length: _Optional[int] = ..., waist_width: _Optional[int] = ..., leg_length: _Optional[int] = ..., leg_width: _Optional[int] = ..., switch_name: _Optional[str] = ..., headwear_type: _Optional[int] = ...) -> None: ...

class FashionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FashionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FashionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FashionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FashionTableBase]] = ...) -> None: ...
