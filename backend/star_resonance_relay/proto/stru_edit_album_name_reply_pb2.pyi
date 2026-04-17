import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditAlbumNameReply(_message.Message):
    __slots__ = ("album_id", "name", "err_code")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    name: str
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, album_id: _Optional[int] = ..., name: _Optional[str] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
