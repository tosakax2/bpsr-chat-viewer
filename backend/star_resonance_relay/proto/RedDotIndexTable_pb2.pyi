import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedDotIndexTableBase(_message.Message):
    __slots__ = ("id", "red_sign_key", "function_id", "close_check", "lose_check", "children_id", "show_type", "picture_path", "effect_path", "off_set", "size", "server_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    RED_SIGN_KEY_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSE_CHECK_FIELD_NUMBER: _ClassVar[int]
    LOSE_CHECK_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_PATH_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PATH_FIELD_NUMBER: _ClassVar[int]
    OFF_SET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    red_sign_key: str
    function_id: int
    close_check: _table_basic_pb2.int_array
    lose_check: _table_basic_pb2.int_array
    children_id: _table_basic_pb2.int_array
    show_type: _table_basic_pb2.int_array
    picture_path: str
    effect_path: str
    off_set: _table_basic_pb2.int_array
    size: _table_basic_pb2.int_array
    server_type: int
    def __init__(self, id: _Optional[int] = ..., red_sign_key: _Optional[str] = ..., function_id: _Optional[int] = ..., close_check: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., lose_check: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., children_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., show_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., picture_path: _Optional[str] = ..., effect_path: _Optional[str] = ..., off_set: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., size: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., server_type: _Optional[int] = ...) -> None: ...

class RedDotIndexTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RedDotIndexTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RedDotIndexTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, RedDotIndexTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, RedDotIndexTableBase]] = ...) -> None: ...
