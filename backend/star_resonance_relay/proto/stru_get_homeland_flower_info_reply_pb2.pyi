import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandFlowerInfoReply(_message.Message):
    __slots__ = ("err_code", "can_get_num")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    CAN_GET_NUM_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    can_get_num: int
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., can_get_num: _Optional[int] = ...) -> None: ...
