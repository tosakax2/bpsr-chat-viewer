import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
import stru_chit_chat_msg_pb2 as _stru_chit_chat_msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyNewestChitChatMsgsRequest(_message.Message):
    __slots__ = ("channel_type", "chat_msg")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_MSG_FIELD_NUMBER: _ClassVar[int]
    channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    chat_msg: _stru_chit_chat_msg_pb2.ChitChatMsg
    def __init__(self, channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., chat_msg: _Optional[_Union[_stru_chit_chat_msg_pb2.ChitChatMsg, _Mapping]] = ...) -> None: ...
