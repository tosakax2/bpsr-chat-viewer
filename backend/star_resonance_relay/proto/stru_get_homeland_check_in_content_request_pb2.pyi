from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandCheckInContentRequest(_message.Message):
    __slots__ = ("community_id", "homeland_id")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ...) -> None: ...
