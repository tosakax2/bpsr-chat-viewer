from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransferLeaderRequest(_message.Message):
    __slots__ = ("new_leader_id",)
    NEW_LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    new_leader_id: int
    def __init__(self, new_leader_id: _Optional[int] = ...) -> None: ...
