import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InteractBtnTableBase(_message.Message):
    __slots__ = ("id", "name", "icon_path", "function_order")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_PATH_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon_path: str
    function_order: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon_path: _Optional[str] = ..., function_order: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class InteractBtnTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InteractBtnTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InteractBtnTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InteractBtnTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InteractBtnTableBase]] = ...) -> None: ...
