import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelTableBase(_message.Message):
    __slots__ = ("id", "type", "channel_name", "channel_style", "function_id", "sub_function_id", "sort", "channel_func")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STYLE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FUNC_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    channel_name: _table_basic_pb2.mlstring
    channel_style: str
    function_id: int
    sub_function_id: _table_basic_pb2.int_array
    sort: int
    channel_func: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., channel_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., channel_style: _Optional[str] = ..., function_id: _Optional[int] = ..., sub_function_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., sort: _Optional[int] = ..., channel_func: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class ChannelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChannelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChannelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChannelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChannelTableBase]] = ...) -> None: ...
