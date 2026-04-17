from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassAwardInfo(_message.Message):
    __slots__ = ("free_award", "paid_award")
    FREE_AWARD_FIELD_NUMBER: _ClassVar[int]
    PAID_AWARD_FIELD_NUMBER: _ClassVar[int]
    free_award: bool
    paid_award: bool
    def __init__(self, free_award: bool = ..., paid_award: bool = ...) -> None: ...
