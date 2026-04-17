import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeTableBase(_message.Message):
    __slots__ = ("id", "shop_name", "system_id", "npc", "show_type", "currency_display")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOP_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    shop_name: _table_basic_pb2.mlstring
    system_id: int
    npc: str
    show_type: int
    currency_display: str
    def __init__(self, id: _Optional[int] = ..., shop_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., system_id: _Optional[int] = ..., npc: _Optional[str] = ..., show_type: _Optional[int] = ..., currency_display: _Optional[str] = ...) -> None: ...

class ExchangeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ExchangeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ExchangeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ExchangeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ExchangeTableBase]] = ...) -> None: ...
