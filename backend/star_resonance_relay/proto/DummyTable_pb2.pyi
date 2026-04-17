import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DummyTableBase(_message.Message):
    __slots__ = ("id", "name", "skill_id", "walk_speed", "run_speed", "skill_ids", "ai_table_reference", "is_initiative", "is_flying", "birth_effect", "dead_effect", "birth_audio", "dead_audio", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    WALK_SPEED_FIELD_NUMBER: _ClassVar[int]
    RUN_SPEED_FIELD_NUMBER: _ClassVar[int]
    SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    AI_TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    IS_INITIATIVE_FIELD_NUMBER: _ClassVar[int]
    IS_FLYING_FIELD_NUMBER: _ClassVar[int]
    BIRTH_EFFECT_FIELD_NUMBER: _ClassVar[int]
    DEAD_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BIRTH_AUDIO_FIELD_NUMBER: _ClassVar[int]
    DEAD_AUDIO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    skill_id: int
    walk_speed: float
    run_speed: float
    skill_ids: _table_basic_pb2.int_array
    ai_table_reference: int
    is_initiative: bool
    is_flying: bool
    birth_effect: str
    dead_effect: str
    birth_audio: str
    dead_audio: str
    tags: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., skill_id: _Optional[int] = ..., walk_speed: _Optional[float] = ..., run_speed: _Optional[float] = ..., skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., ai_table_reference: _Optional[int] = ..., is_initiative: bool = ..., is_flying: bool = ..., birth_effect: _Optional[str] = ..., dead_effect: _Optional[str] = ..., birth_audio: _Optional[str] = ..., dead_audio: _Optional[str] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class DummyTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DummyTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DummyTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DummyTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DummyTableBase]] = ...) -> None: ...
