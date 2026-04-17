import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FantasyTableBase(_message.Message):
    __slots__ = ("id", "name", "fantasy_type", "fantasy_art", "fantasy_tips", "res_template_id", "buff_value_key", "buff_par", "is_only")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FANTASY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FANTASY_ART_FIELD_NUMBER: _ClassVar[int]
    FANTASY_TIPS_FIELD_NUMBER: _ClassVar[int]
    RES_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_VALUE_KEY_FIELD_NUMBER: _ClassVar[int]
    BUFF_PAR_FIELD_NUMBER: _ClassVar[int]
    IS_ONLY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    fantasy_type: int
    fantasy_art: str
    fantasy_tips: str
    res_template_id: _table_basic_pb2.int_table
    buff_value_key: _table_basic_pb2.string_table
    buff_par: _table_basic_pb2.int_table
    is_only: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., fantasy_type: _Optional[int] = ..., fantasy_art: _Optional[str] = ..., fantasy_tips: _Optional[str] = ..., res_template_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_value_key: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., buff_par: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., is_only: bool = ...) -> None: ...

class FantasyTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FantasyTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FantasyTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FantasyTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FantasyTableBase]] = ...) -> None: ...
