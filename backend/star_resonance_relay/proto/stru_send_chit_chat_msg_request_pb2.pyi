import stru_chat_msg_info_pb2 as _stru_chat_msg_info_pb2
import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendChitChatMsgRequest(_message.Message):
    __slots__ = ("channel_type", "same_rate", "msg_info", "send_to_me")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAME_RATE_FIELD_NUMBER: _ClassVar[int]
    MSG_INFO_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_ME_FIELD_NUMBER: _ClassVar[int]
    channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    same_rate: int
    msg_info: _stru_chat_msg_info_pb2.ChatMsgInfo
    send_to_me: bool
    def __init__(self, channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., same_rate: _Optional[int] = ..., msg_info: _Optional[_Union[_stru_chat_msg_info_pb2.ChatMsgInfo, _Mapping]] = ..., send_to_me: bool = ...) -> None: ...
