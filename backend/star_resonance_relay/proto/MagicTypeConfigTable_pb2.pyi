import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagicTypeConfigTableBase(_message.Message):
    __slots__ = ("id", "name", "enum_type_name", "enum_names", "indexs", "descs")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUM_NAMES_FIELD_NUMBER: _ClassVar[int]
    INDEXS_FIELD_NUMBER: _ClassVar[int]
    DESCS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    enum_type_name: str
    enum_names: _table_basic_pb2.string_array
    indexs: _table_basic_pb2.int_array
    descs: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., enum_type_name: _Optional[str] = ..., enum_names: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., indexs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., descs: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class MagicTypeConfigTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MagicTypeConfigTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MagicTypeConfigTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MagicTypeConfigTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MagicTypeConfigTableBase]] = ...) -> None: ...
