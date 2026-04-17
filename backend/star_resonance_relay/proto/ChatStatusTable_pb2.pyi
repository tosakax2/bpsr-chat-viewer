import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatStatusTableBase(_message.Message):
    __slots__ = ("id", "status_name", "res", "status_switch", "sequence", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    STATUS_SWITCH_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: int
    status_name: _table_basic_pb2.mlstring
    res: str
    status_switch: bool
    sequence: int
    priority: int
    def __init__(self, id: _Optional[int] = ..., status_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., res: _Optional[str] = ..., status_switch: bool = ..., sequence: _Optional[int] = ..., priority: _Optional[int] = ...) -> None: ...

class ChatStatusTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChatStatusTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChatStatusTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChatStatusTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChatStatusTableBase]] = ...) -> None: ...
