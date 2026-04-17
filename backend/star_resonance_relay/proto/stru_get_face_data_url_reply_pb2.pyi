import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFaceDataUrlReply(_message.Message):
    __slots__ = ("face_data_url", "err_code")
    FACE_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    face_data_url: str
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, face_data_url: _Optional[str] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
