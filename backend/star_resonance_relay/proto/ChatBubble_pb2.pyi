import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatBubbleBase(_message.Message):
    __slots__ = ("id", "content", "plot_characters_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    content: _table_basic_pb2.mlstring
    plot_characters_id: int
    def __init__(self, id: _Optional[int] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., plot_characters_id: _Optional[int] = ...) -> None: ...

class ChatBubbleMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChatBubbleBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChatBubbleBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChatBubbleBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChatBubbleBase]] = ...) -> None: ...
