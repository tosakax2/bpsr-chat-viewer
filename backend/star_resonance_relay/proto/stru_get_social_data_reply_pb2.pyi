import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_social_data_pb2 as _stru_social_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSocialDataReply(_message.Message):
    __slots__ = ("mask", "data", "err_code")
    MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mask: int
    data: _stru_social_data_pb2.SocialData
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mask: _Optional[int] = ..., data: _Optional[_Union[_stru_social_data_pb2.SocialData, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
