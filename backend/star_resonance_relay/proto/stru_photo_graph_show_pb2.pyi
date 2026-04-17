import stru_image_info_pb2 as _stru_image_info_pb2
import stru_photo_owner_data_pb2 as _stru_photo_owner_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoGraphShow(_message.Message):
    __slots__ = ("photo_id", "images", "render_info", "photo_desc", "owner_info")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    RENDER_INFO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_DESC_FIELD_NUMBER: _ClassVar[int]
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    images: _containers.RepeatedCompositeFieldContainer[_stru_image_info_pb2.ImageInfo]
    render_info: str
    photo_desc: str
    owner_info: _stru_photo_owner_data_pb2.PhotoOwnerData
    def __init__(self, photo_id: _Optional[int] = ..., images: _Optional[_Iterable[_Union[_stru_image_info_pb2.ImageInfo, _Mapping]]] = ..., render_info: _Optional[str] = ..., photo_desc: _Optional[str] = ..., owner_info: _Optional[_Union[_stru_photo_owner_data_pb2.PhotoOwnerData, _Mapping]] = ...) -> None: ...
