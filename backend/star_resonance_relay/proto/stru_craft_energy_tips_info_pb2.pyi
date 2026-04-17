from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CraftEnergyTipsInfo(_message.Message):
    __slots__ = ("consume_value", "residue")
    CONSUME_VALUE_FIELD_NUMBER: _ClassVar[int]
    RESIDUE_FIELD_NUMBER: _ClassVar[int]
    consume_value: int
    residue: int
    def __init__(self, consume_value: _Optional[int] = ..., residue: _Optional[int] = ...) -> None: ...
