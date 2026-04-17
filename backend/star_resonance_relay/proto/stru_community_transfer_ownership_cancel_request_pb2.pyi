from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityTransferOwnershipCancelRequest(_message.Message):
    __slots__ = ("homeland_id",)
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    homeland_id: int
    def __init__(self, homeland_id: _Optional[int] = ...) -> None: ...
