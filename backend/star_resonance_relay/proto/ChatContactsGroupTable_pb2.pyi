import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatContactsGroupTableBase(_message.Message):
    __slots__ = ("id", "group_name", "sequence")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_name: _table_basic_pb2.mlstring
    sequence: int
    def __init__(self, id: _Optional[int] = ..., group_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., sequence: _Optional[int] = ...) -> None: ...

class ChatContactsGroupTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChatContactsGroupTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChatContactsGroupTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChatContactsGroupTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChatContactsGroupTableBase]] = ...) -> None: ...
