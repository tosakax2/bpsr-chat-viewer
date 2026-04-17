import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadPhotoSuccessfulData(_message.Message):
    __slots__ = ("picture_type", "picture_size", "version", "picture_url")
    PICTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    picture_type: _enum_e_picture_type_pb2.EPictureType
    picture_size: int
    version: int
    picture_url: str
    def __init__(self, picture_type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., picture_size: _Optional[int] = ..., version: _Optional[int] = ..., picture_url: _Optional[str] = ...) -> None: ...
