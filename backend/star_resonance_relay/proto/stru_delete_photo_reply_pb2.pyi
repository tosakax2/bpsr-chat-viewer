import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeletePhotoReply(_message.Message):
    __slots__ = ("photo_id", "album_id", "err_code")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    album_id: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, photo_id: _Optional[int] = ..., album_id: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
