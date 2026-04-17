import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageInfo(_message.Message):
    __slots__ = ("type", "size", "version", "cos_url", "extra_info", "review_start_time")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COS_URL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    REVIEW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_picture_type_pb2.EPictureType
    size: int
    version: int
    cos_url: str
    extra_info: str
    review_start_time: int
    def __init__(self, type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., size: _Optional[int] = ..., version: _Optional[int] = ..., cos_url: _Optional[str] = ..., extra_info: _Optional[str] = ..., review_start_time: _Optional[int] = ...) -> None: ...
