import enum_e_album_right_pb2 as _enum_e_album_right_pb2
import stru_image_info_pb2 as _stru_image_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlbumShow(_message.Message):
    __slots__ = ("album_id", "name", "can_access", "access", "cover_photo_id", "cover_thumbnail_info", "photo_ids")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    COVER_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    COVER_THUMBNAIL_INFO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_IDS_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    name: str
    can_access: bool
    access: _enum_e_album_right_pb2.EAlbumRight
    cover_photo_id: int
    cover_thumbnail_info: _stru_image_info_pb2.ImageInfo
    photo_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, album_id: _Optional[int] = ..., name: _Optional[str] = ..., can_access: bool = ..., access: _Optional[_Union[_enum_e_album_right_pb2.EAlbumRight, str]] = ..., cover_photo_id: _Optional[int] = ..., cover_thumbnail_info: _Optional[_Union[_stru_image_info_pb2.ImageInfo, _Mapping]] = ..., photo_ids: _Optional[_Iterable[int]] = ...) -> None: ...
