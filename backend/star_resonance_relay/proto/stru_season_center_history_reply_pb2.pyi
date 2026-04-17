import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_season_center_history_pb2 as _stru_season_center_history_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonCenterHistoryReply(_message.Message):
    __slots__ = ("history", "err_code")
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    history: _stru_season_center_history_pb2.SeasonCenterHistory
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, history: _Optional[_Union[_stru_season_center_history_pb2.SeasonCenterHistory, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
