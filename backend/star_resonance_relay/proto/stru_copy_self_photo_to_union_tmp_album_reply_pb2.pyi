import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CopySelfPhotoToUnionTmpAlbumReply(_message.Message):
    __slots__ = ("cur_upload_times", "err_code")
    CUR_UPLOAD_TIMES_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    cur_upload_times: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, cur_upload_times: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
