import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_info_pb2 as _stru_union_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqTransferPresidentReply(_message.Message):
    __slots__ = ("info", "president", "err_code")
    INFO_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    info: _stru_union_info_pb2.UnionInfo
    president: str
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, info: _Optional[_Union[_stru_union_info_pb2.UnionInfo, _Mapping]] = ..., president: _Optional[str] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
