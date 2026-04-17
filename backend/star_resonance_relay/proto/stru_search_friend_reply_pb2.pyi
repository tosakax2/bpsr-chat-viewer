import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_personal_data_pb2 as _stru_personal_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchFriendReply(_message.Message):
    __slots__ = ("data", "err_code")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_stru_personal_data_pb2.PersonalData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, data: _Optional[_Iterable[_Union[_stru_personal_data_pb2.PersonalData, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
