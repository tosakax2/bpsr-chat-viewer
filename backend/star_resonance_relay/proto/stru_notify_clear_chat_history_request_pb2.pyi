import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyClearChatHistoryRequest(_message.Message):
    __slots__ = ("channel_type", "target_id")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    target_id: str
    def __init__(self, channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., target_id: _Optional[str] = ...) -> None: ...
