import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteAlbumReply(_message.Message):
    __slots__ = ("album_id", "del_photo_ids", "err_code")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    DEL_PHOTO_IDS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    del_photo_ids: _containers.RepeatedScalarFieldContainer[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, album_id: _Optional[int] = ..., del_photo_ids: _Optional[_Iterable[int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
