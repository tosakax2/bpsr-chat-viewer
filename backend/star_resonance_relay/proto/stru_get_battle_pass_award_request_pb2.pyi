from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetBattlePassAwardRequest(_message.Message):
    __slots__ = ("onekey", "level", "unlock", "id")
    ONEKEY_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    onekey: bool
    level: int
    unlock: bool
    id: int
    def __init__(self, onekey: bool = ..., level: _Optional[int] = ..., unlock: bool = ..., id: _Optional[int] = ...) -> None: ...
