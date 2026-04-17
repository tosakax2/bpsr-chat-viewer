import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelSpecialTableBase(_message.Message):
    __slots__ = ("model_prefab_id", "model_prefab_desc", "skeleton", "anim_template", "weapon", "use_head_ik", "look_at_angle", "look_at_speed", "look_at_distance")
    MODEL_PREFAB_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PREFAB_DESC_FIELD_NUMBER: _ClassVar[int]
    SKELETON_FIELD_NUMBER: _ClassVar[int]
    ANIM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    USE_HEAD_IK_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_SPEED_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    model_prefab_id: int
    model_prefab_desc: str
    skeleton: str
    anim_template: str
    weapon: _table_basic_pb2.string_array
    use_head_ik: bool
    look_at_angle: int
    look_at_speed: int
    look_at_distance: int
    def __init__(self, model_prefab_id: _Optional[int] = ..., model_prefab_desc: _Optional[str] = ..., skeleton: _Optional[str] = ..., anim_template: _Optional[str] = ..., weapon: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., use_head_ik: bool = ..., look_at_angle: _Optional[int] = ..., look_at_speed: _Optional[int] = ..., look_at_distance: _Optional[int] = ...) -> None: ...

class ModelSpecialTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModelSpecialTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModelSpecialTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModelSpecialTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModelSpecialTableBase]] = ...) -> None: ...
