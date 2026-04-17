import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_gasha_record_pb2 as _stru_gasha_record_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GashaRecordReply(_message.Message):
    __slots__ = ("gasha_record_datas", "start_id", "count", "total_count", "err_code")
    GASHA_RECORD_DATAS_FIELD_NUMBER: _ClassVar[int]
    START_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    gasha_record_datas: _stru_gasha_record_pb2.GashaRecord
    start_id: int
    count: int
    total_count: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, gasha_record_datas: _Optional[_Union[_stru_gasha_record_pb2.GashaRecord, _Mapping]] = ..., start_id: _Optional[int] = ..., count: _Optional[int] = ..., total_count: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
