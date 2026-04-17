import stru_chit_chat_msg_pb2 as _stru_chit_chat_msg_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendChitChatMsgReply(_message.Message):
    __slots__ = ("show_msg", "cd_end_time", "err_code")
    SHOW_MSG_FIELD_NUMBER: _ClassVar[int]
    CD_END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    show_msg: _stru_chit_chat_msg_pb2.ChitChatMsg
    cd_end_time: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, show_msg: _Optional[_Union[_stru_chit_chat_msg_pb2.ChitChatMsg, _Mapping]] = ..., cd_end_time: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
