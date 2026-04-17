import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AffixPoolTableBase(_message.Message):
    __slots__ = ("id", "name", "description", "affix", "affix_quantity", "effect_type_limit", "target_type_limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    AFFIX_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    affix: _table_basic_pb2.int_table
    affix_quantity: int
    effect_type_limit: _table_basic_pb2.int_table
    target_type_limit: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., affix: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., affix_quantity: _Optional[int] = ..., effect_type_limit: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., target_type_limit: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class AffixPoolTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AffixPoolTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AffixPoolTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AffixPoolTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AffixPoolTableBase]] = ...) -> None: ...
