import enum_e_album_right_pb2 as _enum_e_album_right_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditAlbumRightReply(_message.Message):
    __slots__ = ("album_id", "access", "err_code")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    access: _enum_e_album_right_pb2.EAlbumRight
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, album_id: _Optional[int] = ..., access: _Optional[_Union[_enum_e_album_right_pb2.EAlbumRight, str]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
