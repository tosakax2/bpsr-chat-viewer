import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelNpcTableBase(_message.Message):
    __slots__ = ("model_prefab_id", "model_prefab_desc", "sex", "model", "skin", "skeleton", "anim_template", "skeleton_color", "emo_prefix", "head", "anim_head_template", "eye_color", "hair", "hair_color", "headwear", "headwear_color", "mask", "mask_color", "back", "back_color", "hand_object", "hand_object_color", "weaponl", "weaponr", "weapon_idle_anim")
    MODEL_PREFAB_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PREFAB_DESC_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    SKELETON_FIELD_NUMBER: _ClassVar[int]
    ANIM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SKELETON_COLOR_FIELD_NUMBER: _ClassVar[int]
    EMO_PREFIX_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ANIM_HEAD_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EYE_COLOR_FIELD_NUMBER: _ClassVar[int]
    HAIR_FIELD_NUMBER: _ClassVar[int]
    HAIR_COLOR_FIELD_NUMBER: _ClassVar[int]
    HEADWEAR_FIELD_NUMBER: _ClassVar[int]
    HEADWEAR_COLOR_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    MASK_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACK_FIELD_NUMBER: _ClassVar[int]
    BACK_COLOR_FIELD_NUMBER: _ClassVar[int]
    HAND_OBJECT_FIELD_NUMBER: _ClassVar[int]
    HAND_OBJECT_COLOR_FIELD_NUMBER: _ClassVar[int]
    WEAPONL_FIELD_NUMBER: _ClassVar[int]
    WEAPONR_FIELD_NUMBER: _ClassVar[int]
    WEAPON_IDLE_ANIM_FIELD_NUMBER: _ClassVar[int]
    model_prefab_id: int
    model_prefab_desc: str
    sex: int
    model: int
    skin: _table_basic_pb2.vector3
    skeleton: str
    anim_template: str
    skeleton_color: _table_basic_pb2.vector3_array
    emo_prefix: str
    head: str
    anim_head_template: str
    eye_color: _table_basic_pb2.vector3_array
    hair: str
    hair_color: _table_basic_pb2.vector3_array
    headwear: str
    headwear_color: _table_basic_pb2.vector3_array
    mask: str
    mask_color: _table_basic_pb2.vector3_array
    back: str
    back_color: _table_basic_pb2.vector3_array
    hand_object: str
    hand_object_color: _table_basic_pb2.vector3_array
    weaponl: str
    weaponr: str
    weapon_idle_anim: str
    def __init__(self, model_prefab_id: _Optional[int] = ..., model_prefab_desc: _Optional[str] = ..., sex: _Optional[int] = ..., model: _Optional[int] = ..., skin: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., skeleton: _Optional[str] = ..., anim_template: _Optional[str] = ..., skeleton_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., emo_prefix: _Optional[str] = ..., head: _Optional[str] = ..., anim_head_template: _Optional[str] = ..., eye_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., hair: _Optional[str] = ..., hair_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., headwear: _Optional[str] = ..., headwear_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., mask: _Optional[str] = ..., mask_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., back: _Optional[str] = ..., back_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., hand_object: _Optional[str] = ..., hand_object_color: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., weaponl: _Optional[str] = ..., weaponr: _Optional[str] = ..., weapon_idle_anim: _Optional[str] = ...) -> None: ...

class ModelNpcTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModelNpcTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModelNpcTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModelNpcTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModelNpcTableBase]] = ...) -> None: ...
