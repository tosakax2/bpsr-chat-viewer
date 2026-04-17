from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyRefuseBeTransferLeaderRequest(_message.Message):
    __slots__ = ("mem_id",)
    MEM_ID_FIELD_NUMBER: _ClassVar[int]
    mem_id: int
    def __init__(self, mem_id: _Optional[int] = ...) -> None: ...
