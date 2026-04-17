from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityTransferOwnershipRequest(_message.Message):
    __slots__ = ("homeland_id", "new_owner_char_id")
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    homeland_id: int
    new_owner_char_id: int
    def __init__(self, homeland_id: _Optional[int] = ..., new_owner_char_id: _Optional[int] = ...) -> None: ...
