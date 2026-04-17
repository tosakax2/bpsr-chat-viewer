import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageCosKey(_message.Message):
    __slots__ = ("type", "cos_key", "extra_info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COS_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_picture_type_pb2.EPictureType
    cos_key: str
    extra_info: str
    def __init__(self, type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., cos_key: _Optional[str] = ..., extra_info: _Optional[str] = ...) -> None: ...
