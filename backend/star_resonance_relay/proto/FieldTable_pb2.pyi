import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FieldTableBase(_message.Message):
    __slots__ = ("id", "name", "skill_id", "size", "model_id", "min_body", "attribute_id", "be_hit_effect", "birth_effect", "death_effect", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_BODY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    BE_HIT_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BIRTH_EFFECT_FIELD_NUMBER: _ClassVar[int]
    DEATH_EFFECT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    skill_id: int
    size: _table_basic_pb2.vector2
    model_id: int
    min_body: int
    attribute_id: int
    be_hit_effect: str
    birth_effect: str
    death_effect: str
    tags: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., skill_id: _Optional[int] = ..., size: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., model_id: _Optional[int] = ..., min_body: _Optional[int] = ..., attribute_id: _Optional[int] = ..., be_hit_effect: _Optional[str] = ..., birth_effect: _Optional[str] = ..., death_effect: _Optional[str] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class FieldTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FieldTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FieldTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FieldTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FieldTableBase]] = ...) -> None: ...
