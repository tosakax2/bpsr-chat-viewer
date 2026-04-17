import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetUnionEScreenPhotoReply(_message.Message):
    __slots__ = ("cur_set_times", "max_set_times", "err_code")
    CUR_SET_TIMES_FIELD_NUMBER: _ClassVar[int]
    MAX_SET_TIMES_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    cur_set_times: int
    max_set_times: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, cur_set_times: _Optional[int] = ..., max_set_times: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
