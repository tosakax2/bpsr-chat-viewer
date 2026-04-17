import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BodyPartsTableBase(_message.Message):
    __slots__ = ("id", "model_id", "body_parts_desc", "type", "radius", "height", "direction", "rotate", "offset", "bone", "shader_index", "be_hit_anim_mask", "max_hp", "not_hit", "not_choose", "on_can_hit_target_weight", "on_no_hit_target_weight", "basic_fleshy_type", "is_lock_collider_idx", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    BODY_PARTS_DESC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BONE_FIELD_NUMBER: _ClassVar[int]
    SHADER_INDEX_FIELD_NUMBER: _ClassVar[int]
    BE_HIT_ANIM_MASK_FIELD_NUMBER: _ClassVar[int]
    MAX_HP_FIELD_NUMBER: _ClassVar[int]
    NOT_HIT_FIELD_NUMBER: _ClassVar[int]
    NOT_CHOOSE_FIELD_NUMBER: _ClassVar[int]
    ON_CAN_HIT_TARGET_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ON_NO_HIT_TARGET_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BASIC_FLESHY_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_LOCK_COLLIDER_IDX_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    model_id: int
    body_parts_desc: str
    type: int
    radius: _table_basic_pb2.number_array
    height: _table_basic_pb2.number_array
    direction: _table_basic_pb2.vector3_array
    rotate: _table_basic_pb2.vector3_array
    offset: _table_basic_pb2.vector3_array
    bone: _table_basic_pb2.string_array
    shader_index: int
    be_hit_anim_mask: str
    max_hp: int
    not_hit: bool
    not_choose: bool
    on_can_hit_target_weight: float
    on_no_hit_target_weight: float
    basic_fleshy_type: int
    is_lock_collider_idx: int
    tags: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., model_id: _Optional[int] = ..., body_parts_desc: _Optional[str] = ..., type: _Optional[int] = ..., radius: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., height: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., direction: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., rotate: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., offset: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., bone: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., shader_index: _Optional[int] = ..., be_hit_anim_mask: _Optional[str] = ..., max_hp: _Optional[int] = ..., not_hit: bool = ..., not_choose: bool = ..., on_can_hit_target_weight: _Optional[float] = ..., on_no_hit_target_weight: _Optional[float] = ..., basic_fleshy_type: _Optional[int] = ..., is_lock_collider_idx: _Optional[int] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class BodyPartsTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BodyPartsTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BodyPartsTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BodyPartsTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BodyPartsTableBase]] = ...) -> None: ...
