from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelWpNpcTableBase(_message.Message):
    __slots__ = ("model_prefab_id", "model_prefab_desc", "sex", "skeleton", "anim_template", "emo_prefix", "head", "anim_head_template", "hair", "anim_hair_template", "headwear", "back", "weaponl", "weaponr", "tail", "weapon_idle_anim", "pinch_config")
    MODEL_PREFAB_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PREFAB_DESC_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    SKELETON_FIELD_NUMBER: _ClassVar[int]
    ANIM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EMO_PREFIX_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ANIM_HEAD_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HAIR_FIELD_NUMBER: _ClassVar[int]
    ANIM_HAIR_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HEADWEAR_FIELD_NUMBER: _ClassVar[int]
    BACK_FIELD_NUMBER: _ClassVar[int]
    WEAPONL_FIELD_NUMBER: _ClassVar[int]
    WEAPONR_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    WEAPON_IDLE_ANIM_FIELD_NUMBER: _ClassVar[int]
    PINCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    model_prefab_id: int
    model_prefab_desc: str
    sex: int
    skeleton: str
    anim_template: str
    emo_prefix: str
    head: str
    anim_head_template: str
    hair: str
    anim_hair_template: str
    headwear: str
    back: str
    weaponl: str
    weaponr: str
    tail: str
    weapon_idle_anim: str
    pinch_config: str
    def __init__(self, model_prefab_id: _Optional[int] = ..., model_prefab_desc: _Optional[str] = ..., sex: _Optional[int] = ..., skeleton: _Optional[str] = ..., anim_template: _Optional[str] = ..., emo_prefix: _Optional[str] = ..., head: _Optional[str] = ..., anim_head_template: _Optional[str] = ..., hair: _Optional[str] = ..., anim_hair_template: _Optional[str] = ..., headwear: _Optional[str] = ..., back: _Optional[str] = ..., weaponl: _Optional[str] = ..., weaponr: _Optional[str] = ..., tail: _Optional[str] = ..., weapon_idle_anim: _Optional[str] = ..., pinch_config: _Optional[str] = ...) -> None: ...

class ModelWpNpcTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModelWpNpcTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModelWpNpcTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModelWpNpcTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModelWpNpcTableBase]] = ...) -> None: ...
