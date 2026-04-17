import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailManagerReply(_message.Message):
    __slots__ = ("normal_num", "normal_un_read_list", "collect_num", "collect_un_read_list", "err_code")
    NORMAL_NUM_FIELD_NUMBER: _ClassVar[int]
    NORMAL_UN_READ_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECT_NUM_FIELD_NUMBER: _ClassVar[int]
    COLLECT_UN_READ_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    normal_num: int
    normal_un_read_list: _containers.RepeatedScalarFieldContainer[int]
    collect_num: int
    collect_un_read_list: _containers.RepeatedScalarFieldContainer[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, normal_num: _Optional[int] = ..., normal_un_read_list: _Optional[_Iterable[int]] = ..., collect_num: _Optional[int] = ..., collect_un_read_list: _Optional[_Iterable[int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
