import stru_id_ip_image_pb2 as _stru_id_ip_image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdIpPhoto(_message.Message):
    __slots__ = ("photo_id", "image_list")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    image_list: _containers.RepeatedCompositeFieldContainer[_stru_id_ip_image_pb2.IdIpImage]
    def __init__(self, photo_id: _Optional[int] = ..., image_list: _Optional[_Iterable[_Union[_stru_id_ip_image_pb2.IdIpImage, _Mapping]]] = ...) -> None: ...
