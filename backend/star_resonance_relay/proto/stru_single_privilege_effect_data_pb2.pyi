from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SinglePrivilegeEffectData(_message.Message):
    __slots__ = ("type", "id", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    value: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
