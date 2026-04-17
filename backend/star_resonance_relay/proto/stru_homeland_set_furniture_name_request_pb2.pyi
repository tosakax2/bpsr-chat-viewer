from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandSetFurnitureNameRequest(_message.Message):
    __slots__ = ("structure_uuid", "name", "is_outer")
    STRUCTURE_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    structure_uuid: int
    name: str
    is_outer: bool
    def __init__(self, structure_uuid: _Optional[int] = ..., name: _Optional[str] = ..., is_outer: bool = ...) -> None: ...
