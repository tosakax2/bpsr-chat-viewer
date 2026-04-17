import enum_place_holder_type_pb2 as _enum_place_holder_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolder(_message.Message):
    __slots__ = ("type", "bytes_content")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTES_CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: _enum_place_holder_type_pb2.PlaceHolderType
    bytes_content: bytes
    def __init__(self, type: _Optional[_Union[_enum_place_holder_type_pb2.PlaceHolderType, str]] = ..., bytes_content: _Optional[bytes] = ...) -> None: ...
