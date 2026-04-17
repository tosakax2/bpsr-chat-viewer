import stru_chit_chat_msg_pb2 as _stru_chit_chat_msg_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetChipChatRecordsReply(_message.Message):
    __slots__ = ("is_end", "max_read_msg_id", "multi_msg_list", "err_code")
    IS_END_FIELD_NUMBER: _ClassVar[int]
    MAX_READ_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    MULTI_MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    is_end: bool
    max_read_msg_id: int
    multi_msg_list: _containers.RepeatedCompositeFieldContainer[_stru_chit_chat_msg_pb2.ChitChatMsg]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, is_end: bool = ..., max_read_msg_id: _Optional[int] = ..., multi_msg_list: _Optional[_Iterable[_Union[_stru_chit_chat_msg_pb2.ChitChatMsg, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
