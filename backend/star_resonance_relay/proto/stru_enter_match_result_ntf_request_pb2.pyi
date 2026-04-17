import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_match_info_pb2 as _stru_match_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnterMatchResultNtfRequest(_message.Message):
    __slots__ = ("err_code", "match_info", "is_re_enter")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_RE_ENTER_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    match_info: _stru_match_info_pb2.MatchInfo
    is_re_enter: bool
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., match_info: _Optional[_Union[_stru_match_info_pb2.MatchInfo, _Mapping]] = ..., is_re_enter: bool = ...) -> None: ...
