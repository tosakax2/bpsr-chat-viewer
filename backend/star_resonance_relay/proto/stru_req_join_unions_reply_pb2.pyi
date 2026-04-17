import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_ret_pb2 as _stru_union_ret_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqJoinUnionsReply(_message.Message):
    __slots__ = ("unions_ret", "next_join_time", "err_code")
    UNIONS_RET_FIELD_NUMBER: _ClassVar[int]
    NEXT_JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    unions_ret: _containers.RepeatedCompositeFieldContainer[_stru_union_ret_pb2.UnionRet]
    next_join_time: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, unions_ret: _Optional[_Iterable[_Union[_stru_union_ret_pb2.UnionRet, _Mapping]]] = ..., next_join_time: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
