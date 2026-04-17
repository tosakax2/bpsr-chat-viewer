import stru_client_image_pb2 as _stru_client_image_pb2
import enum_e_platform_func_type_pb2 as _enum_e_platform_func_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPhotoUpTokenRequest(_message.Message):
    __slots__ = ("photo_id", "render_info", "album_id", "images_info", "photo_desc", "func_type", "owner_id", "text")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_INFO_FIELD_NUMBER: _ClassVar[int]
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_INFO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_DESC_FIELD_NUMBER: _ClassVar[int]
    FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    render_info: str
    album_id: int
    images_info: _containers.RepeatedCompositeFieldContainer[_stru_client_image_pb2.ClientImage]
    photo_desc: str
    func_type: _enum_e_platform_func_type_pb2.EPlatformFuncType
    owner_id: int
    text: str
    def __init__(self, photo_id: _Optional[int] = ..., render_info: _Optional[str] = ..., album_id: _Optional[int] = ..., images_info: _Optional[_Iterable[_Union[_stru_client_image_pb2.ClientImage, _Mapping]]] = ..., photo_desc: _Optional[str] = ..., func_type: _Optional[_Union[_enum_e_platform_func_type_pb2.EPlatformFuncType, str]] = ..., owner_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
