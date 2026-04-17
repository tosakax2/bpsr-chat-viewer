from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShieldInfo(_message.Message):
    __slots__ = ("uuid", "shield_type", "value", "initial_value", "max_value")
    UUID_FIELD_NUMBER: _ClassVar[int]
    SHIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    shield_type: int
    value: int
    initial_value: int
    max_value: int
    def __init__(self, uuid: _Optional[int] = ..., shield_type: _Optional[int] = ..., value: _Optional[int] = ..., initial_value: _Optional[int] = ..., max_value: _Optional[int] = ...) -> None: ...
