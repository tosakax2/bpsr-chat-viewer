import stru_album_show_pb2 as _stru_album_show_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllAlbumsReply(_message.Message):
    __slots__ = ("char_id", "all_albums", "err_code")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_ALBUMS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    all_albums: _containers.RepeatedCompositeFieldContainer[_stru_album_show_pb2.AlbumShow]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, char_id: _Optional[int] = ..., all_albums: _Optional[_Iterable[_Union[_stru_album_show_pb2.AlbumShow, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
