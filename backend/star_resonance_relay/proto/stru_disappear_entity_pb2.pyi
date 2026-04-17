import enum_e_disappear_type_pb2 as _enum_e_disappear_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisappearEntity(_message.Message):
    __slots__ = ("uuid", "type")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    type: _enum_e_disappear_type_pb2.EDisappearType
    def __init__(self, uuid: _Optional[int] = ..., type: _Optional[_Union[_enum_e_disappear_type_pb2.EDisappearType, str]] = ...) -> None: ...
