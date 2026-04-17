import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicAttrEffectTableBase(_message.Message):
    __slots__ = ("id", "attr_strength_table", "attr_strength_max", "attr_vitality_table", "attr_vitality_max", "attr_dexterity_table", "attr_dexterity_max", "attr_intelligence_table", "attr_intelligence_max", "attr_mind_table", "attr_mind_max", "attr_observe_table", "attr_observe_max", "attr_introduction")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_STRENGTH_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_STRENGTH_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_VITALITY_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_VITALITY_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_DEXTERITY_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_DEXTERITY_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_INTELLIGENCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_INTELLIGENCE_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_MIND_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_MIND_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_OBSERVE_TABLE_FIELD_NUMBER: _ClassVar[int]
    ATTR_OBSERVE_MAX_FIELD_NUMBER: _ClassVar[int]
    ATTR_INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    attr_strength_table: _table_basic_pb2.number_table
    attr_strength_max: int
    attr_vitality_table: _table_basic_pb2.number_table
    attr_vitality_max: int
    attr_dexterity_table: _table_basic_pb2.number_table
    attr_dexterity_max: int
    attr_intelligence_table: _table_basic_pb2.number_table
    attr_intelligence_max: int
    attr_mind_table: _table_basic_pb2.number_table
    attr_mind_max: int
    attr_observe_table: _table_basic_pb2.number_table
    attr_observe_max: int
    attr_introduction: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., attr_strength_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_strength_max: _Optional[int] = ..., attr_vitality_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_vitality_max: _Optional[int] = ..., attr_dexterity_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_dexterity_max: _Optional[int] = ..., attr_intelligence_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_intelligence_max: _Optional[int] = ..., attr_mind_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_mind_max: _Optional[int] = ..., attr_observe_table: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., attr_observe_max: _Optional[int] = ..., attr_introduction: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class BasicAttrEffectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BasicAttrEffectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BasicAttrEffectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BasicAttrEffectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BasicAttrEffectTableBase]] = ...) -> None: ...
