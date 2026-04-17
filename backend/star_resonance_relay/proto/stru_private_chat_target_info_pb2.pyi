import stru_chit_chat_msg_pb2 as _stru_chit_chat_msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateChatTargetInfo(_message.Message):
    __slots__ = ("char_id", "max_read_msg_id", "is_top", "latest_msg")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_READ_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TOP_FIELD_NUMBER: _ClassVar[int]
    LATEST_MSG_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    max_read_msg_id: int
    is_top: bool
    latest_msg: _stru_chit_chat_msg_pb2.ChitChatMsg
    def __init__(self, char_id: _Optional[int] = ..., max_read_msg_id: _Optional[int] = ..., is_top: bool = ..., latest_msg: _Optional[_Union[_stru_chit_chat_msg_pb2.ChitChatMsg, _Mapping]] = ...) -> None: ...
