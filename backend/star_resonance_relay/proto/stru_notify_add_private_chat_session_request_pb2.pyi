import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_private_chat_target_info_pb2 as _stru_private_chat_target_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyAddPrivateChatSessionRequest(_message.Message):
    __slots__ = ("err_code", "add_target_info", "del_target_id")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ADD_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    DEL_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    add_target_info: _stru_private_chat_target_info_pb2.PrivateChatTargetInfo
    del_target_id: int
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., add_target_info: _Optional[_Union[_stru_private_chat_target_info_pb2.PrivateChatTargetInfo, _Mapping]] = ..., del_target_id: _Optional[int] = ...) -> None: ...
