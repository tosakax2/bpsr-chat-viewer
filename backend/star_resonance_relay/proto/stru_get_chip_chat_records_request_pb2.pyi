import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetChipChatRecordsRequest(_message.Message):
    __slots__ = ("channel_type", "desc_msg_id", "record_num", "target_id")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESC_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_NUM_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    desc_msg_id: int
    record_num: int
    target_id: int
    def __init__(self, channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., desc_msg_id: _Optional[int] = ..., record_num: _Optional[int] = ..., target_id: _Optional[int] = ...) -> None: ...
