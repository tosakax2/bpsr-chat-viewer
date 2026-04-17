import enum_e_match_cancel_type_pb2 as _enum_e_match_cancel_type_pb2
import stru_match_info_pb2 as _stru_match_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelMatchResultNtfRequest(_message.Message):
    __slots__ = ("cancel_type", "match_info")
    CANCEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_INFO_FIELD_NUMBER: _ClassVar[int]
    cancel_type: _enum_e_match_cancel_type_pb2.EMatchCancelType
    match_info: _stru_match_info_pb2.MatchInfo
    def __init__(self, cancel_type: _Optional[_Union[_enum_e_match_cancel_type_pb2.EMatchCancelType, str]] = ..., match_info: _Optional[_Union[_stru_match_info_pb2.MatchInfo, _Mapping]] = ...) -> None: ...
