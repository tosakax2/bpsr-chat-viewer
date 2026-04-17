import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_life_profession_work_info_pb2 as _stru_life_profession_work_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionWorkHistoryInfo(_message.Message):
    __slots__ = ("work_infos", "err_code")
    WORK_INFOS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    work_infos: _containers.RepeatedCompositeFieldContainer[_stru_life_profession_work_info_pb2.LifeProfessionWorkInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, work_infos: _Optional[_Iterable[_Union[_stru_life_profession_work_info_pb2.LifeProfessionWorkInfo, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
