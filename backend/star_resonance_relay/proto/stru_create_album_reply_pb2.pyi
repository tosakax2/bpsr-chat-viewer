import stru_album_show_pb2 as _stru_album_show_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAlbumReply(_message.Message):
    __slots__ = ("album_info", "err_code")
    ALBUM_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    album_info: _stru_album_show_pb2.AlbumShow
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, album_info: _Optional[_Union[_stru_album_show_pb2.AlbumShow, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
