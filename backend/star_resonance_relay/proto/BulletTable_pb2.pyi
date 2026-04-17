import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BulletTableBase(_message.Message):
    __slots__ = ("id", "name", "start", "duration", "model_id", "boom_count", "boom_interval", "damage_interval", "bullet_attr_id", "tags", "dead_show_stage_id", "bullet_count", "damage_weight", "damage_weight_type", "fake_bullet")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    BOOM_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOOM_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    BULLET_ATTR_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DEAD_SHOW_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BULLET_COUNT_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_WEIGHT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAKE_BULLET_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    start: float
    duration: float
    model_id: int
    boom_count: int
    boom_interval: int
    damage_interval: int
    bullet_attr_id: int
    tags: _table_basic_pb2.int_array
    dead_show_stage_id: int
    bullet_count: int
    damage_weight: _table_basic_pb2.vector2
    damage_weight_type: int
    fake_bullet: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., model_id: _Optional[int] = ..., boom_count: _Optional[int] = ..., boom_interval: _Optional[int] = ..., damage_interval: _Optional[int] = ..., bullet_attr_id: _Optional[int] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., dead_show_stage_id: _Optional[int] = ..., bullet_count: _Optional[int] = ..., damage_weight: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., damage_weight_type: _Optional[int] = ..., fake_bullet: bool = ...) -> None: ...

class BulletTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BulletTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BulletTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BulletTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BulletTableBase]] = ...) -> None: ...
