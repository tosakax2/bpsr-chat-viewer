import stru_basic_show_info_pb2 as _stru_basic_show_info_pb2
import stru_chat_msg_info_pb2 as _stru_chat_msg_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChitChatMsg(_message.Message):
    __slots__ = ("msg_id", "send_char_info", "timestamp", "msg_info")
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_CHAR_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MSG_INFO_FIELD_NUMBER: _ClassVar[int]
    msg_id: int
    send_char_info: _stru_basic_show_info_pb2.BasicShowInfo
    timestamp: int
    msg_info: _stru_chat_msg_info_pb2.ChatMsgInfo
    def __init__(self, msg_id: _Optional[int] = ..., send_char_info: _Optional[_Union[_stru_basic_show_info_pb2.BasicShowInfo, _Mapping]] = ..., timestamp: _Optional[int] = ..., msg_info: _Optional[_Union[_stru_chat_msg_info_pb2.ChatMsgInfo, _Mapping]] = ...) -> None: ...
