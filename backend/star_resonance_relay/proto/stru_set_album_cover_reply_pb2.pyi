import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_image_info_pb2 as _stru_image_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetAlbumCoverReply(_message.Message):
    __slots__ = ("album_id", "cover_photo_id", "cover_thumbnail_info", "err_code")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    COVER_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    COVER_THUMBNAIL_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    cover_photo_id: int
    cover_thumbnail_info: _stru_image_info_pb2.ImageInfo
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, album_id: _Optional[int] = ..., cover_photo_id: _Optional[int] = ..., cover_thumbnail_info: _Optional[_Union[_stru_image_info_pb2.ImageInfo, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
