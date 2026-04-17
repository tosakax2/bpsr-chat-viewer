from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityCleanlinessUpdateRequest(_message.Message):
    __slots__ = ("new_cleanliness", "new_last_subtract_cleanliness_sec", "old_cleanliness", "actual_subtract")
    NEW_CLEANLINESS_FIELD_NUMBER: _ClassVar[int]
    NEW_LAST_SUBTRACT_CLEANLINESS_SEC_FIELD_NUMBER: _ClassVar[int]
    OLD_CLEANLINESS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_SUBTRACT_FIELD_NUMBER: _ClassVar[int]
    new_cleanliness: int
    new_last_subtract_cleanliness_sec: int
    old_cleanliness: int
    actual_subtract: int
    def __init__(self, new_cleanliness: _Optional[int] = ..., new_last_subtract_cleanliness_sec: _Optional[int] = ..., old_cleanliness: _Optional[int] = ..., actual_subtract: _Optional[int] = ...) -> None: ...
