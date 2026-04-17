import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TempAttrTableBase(_message.Message):
    __slots__ = ("id", "name", "desc", "attr_type", "logic_type", "attr_params", "lower_limit", "upper_limit", "is_sync_client")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    ATTR_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_SYNC_CLIENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    desc: str
    attr_type: int
    logic_type: int
    attr_params: _table_basic_pb2.int_array
    lower_limit: int
    upper_limit: int
    is_sync_client: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., attr_type: _Optional[int] = ..., logic_type: _Optional[int] = ..., attr_params: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., lower_limit: _Optional[int] = ..., upper_limit: _Optional[int] = ..., is_sync_client: bool = ...) -> None: ...

class TempAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TempAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TempAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TempAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TempAttrTableBase]] = ...) -> None: ...
