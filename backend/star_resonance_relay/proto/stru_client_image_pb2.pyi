import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientImage(_message.Message):
    __slots__ = ("name", "type", "size", "extra_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _enum_e_picture_type_pb2.EPictureType
    size: int
    extra_info: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., size: _Optional[int] = ..., extra_info: _Optional[str] = ...) -> None: ...
