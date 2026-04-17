from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetTeamTargetInfoRequest(_message.Message):
    __slots__ = ("target_id", "show", "auto_match", "desc")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    AUTO_MATCH_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    show: bool
    auto_match: bool
    desc: str
    def __init__(self, target_id: _Optional[int] = ..., show: bool = ..., auto_match: bool = ..., desc: _Optional[str] = ...) -> None: ...
