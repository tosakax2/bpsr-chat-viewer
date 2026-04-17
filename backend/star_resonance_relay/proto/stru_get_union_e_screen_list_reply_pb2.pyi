import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_e_screen_info_pb2 as _stru_union_e_screen_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUnionEScreenListReply(_message.Message):
    __slots__ = ("e_screen_list", "cur_set_times", "max_set_times", "err_code")
    E_SCREEN_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_SET_TIMES_FIELD_NUMBER: _ClassVar[int]
    MAX_SET_TIMES_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    e_screen_list: _containers.RepeatedCompositeFieldContainer[_stru_union_e_screen_info_pb2.UnionEScreenInfo]
    cur_set_times: int
    max_set_times: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, e_screen_list: _Optional[_Iterable[_Union[_stru_union_e_screen_info_pb2.UnionEScreenInfo, _Mapping]]] = ..., cur_set_times: _Optional[int] = ..., max_set_times: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
