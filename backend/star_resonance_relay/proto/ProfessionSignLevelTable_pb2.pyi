import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionSignLevelTableBase(_message.Message):
    __slots__ = ("id", "sign_item_id", "level_id", "effect_para")
    ID_FIELD_NUMBER: _ClassVar[int]
    SIGN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PARA_FIELD_NUMBER: _ClassVar[int]
    id: int
    sign_item_id: int
    level_id: int
    effect_para: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., sign_item_id: _Optional[int] = ..., level_id: _Optional[int] = ..., effect_para: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ProfessionSignLevelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfessionSignLevelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfessionSignLevelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfessionSignLevelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfessionSignLevelTableBase]] = ...) -> None: ...
