import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportChat(_message.Message):
    __slots__ = ("chat_channel_type", "channel_id", "chat_id", "chat_content")
    CHAT_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    chat_channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    channel_id: str
    chat_id: int
    chat_content: str
    def __init__(self, chat_channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., channel_id: _Optional[str] = ..., chat_id: _Optional[int] = ..., chat_content: _Optional[str] = ...) -> None: ...
