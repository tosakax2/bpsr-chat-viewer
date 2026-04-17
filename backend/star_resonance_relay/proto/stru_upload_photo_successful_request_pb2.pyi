import enum_e_platform_func_type_pb2 as _enum_e_platform_func_type_pb2
import stru_upload_photo_successful_data_pb2 as _stru_upload_photo_successful_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadPhotoSuccessfulRequest(_message.Message):
    __slots__ = ("char_id", "picture_id", "func_type", "data", "owner_id")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    PICTURE_ID_FIELD_NUMBER: _ClassVar[int]
    FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    picture_id: int
    func_type: _enum_e_platform_func_type_pb2.EPlatformFuncType
    data: _containers.RepeatedCompositeFieldContainer[_stru_upload_photo_successful_data_pb2.UploadPhotoSuccessfulData]
    owner_id: int
    def __init__(self, char_id: _Optional[int] = ..., picture_id: _Optional[int] = ..., func_type: _Optional[_Union[_enum_e_platform_func_type_pb2.EPlatformFuncType, str]] = ..., data: _Optional[_Iterable[_Union[_stru_upload_photo_successful_data_pb2.UploadPhotoSuccessfulData, _Mapping]]] = ..., owner_id: _Optional[int] = ...) -> None: ...
