from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetTeamTargetQuickSayRequest(_message.Message):
    __slots__ = ("desc", "quick_say_id")
    DESC_FIELD_NUMBER: _ClassVar[int]
    QUICK_SAY_ID_FIELD_NUMBER: _ClassVar[int]
    desc: str
    quick_say_id: int
    def __init__(self, desc: _Optional[str] = ..., quick_say_id: _Optional[int] = ...) -> None: ...
