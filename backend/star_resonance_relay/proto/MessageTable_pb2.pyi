import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageTableBase(_message.Message):
    __slots__ = ("id", "content", "type", "duration_time", "chat_name", "delay", "repeat_play", "show_channel", "filter_rule", "is_show_in_chat", "typewriter_effect", "interrupt", "audio")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    REPEAT_PLAY_FIELD_NUMBER: _ClassVar[int]
    SHOW_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FILTER_RULE_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_IN_CHAT_FIELD_NUMBER: _ClassVar[int]
    TYPEWRITER_EFFECT_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    id: int
    content: _table_basic_pb2.mlstring
    type: int
    duration_time: float
    chat_name: _table_basic_pb2.mlstring
    delay: float
    repeat_play: _table_basic_pb2.int_array
    show_channel: _table_basic_pb2.int_array
    filter_rule: bool
    is_show_in_chat: bool
    typewriter_effect: bool
    interrupt: int
    audio: str
    def __init__(self, id: _Optional[int] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type: _Optional[int] = ..., duration_time: _Optional[float] = ..., chat_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., delay: _Optional[float] = ..., repeat_play: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., show_channel: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., filter_rule: bool = ..., is_show_in_chat: bool = ..., typewriter_effect: bool = ..., interrupt: _Optional[int] = ..., audio: _Optional[str] = ...) -> None: ...

class MessageTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MessageTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MessageTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MessageTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MessageTableBase]] = ...) -> None: ...
