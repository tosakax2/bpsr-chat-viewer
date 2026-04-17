from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetStructureGroupInfoRequest(_message.Message):
    __slots__ = ("is_outer",)
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    is_outer: bool
    def __init__(self, is_outer: bool = ...) -> None: ...
