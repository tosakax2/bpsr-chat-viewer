import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionSignTableBase(_message.Message):
    __slots__ = ("id", "name", "sign_type", "card", "item_tips", "effect_type", "effect_id", "effectkey")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    ITEM_TIPS_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTKEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    sign_type: _table_basic_pb2.int_array
    card: str
    item_tips: str
    effect_type: _table_basic_pb2.int_array
    effect_id: _table_basic_pb2.int_array
    effectkey: _table_basic_pb2.string_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., sign_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., card: _Optional[str] = ..., item_tips: _Optional[str] = ..., effect_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., effect_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., effectkey: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ...) -> None: ...

class ProfessionSignTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfessionSignTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfessionSignTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfessionSignTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfessionSignTableBase]] = ...) -> None: ...
