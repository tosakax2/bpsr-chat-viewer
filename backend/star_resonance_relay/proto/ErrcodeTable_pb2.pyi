import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrcodeTableBase(_message.Message):
    __slots__ = ("id", "errcode", "content", "message_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    errcode: str
    content: _table_basic_pb2.mlstring
    message_id: int
    def __init__(self, id: _Optional[int] = ..., errcode: _Optional[str] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., message_id: _Optional[int] = ...) -> None: ...

class ErrcodeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ErrcodeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ErrcodeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ErrcodeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ErrcodeTableBase]] = ...) -> None: ...
