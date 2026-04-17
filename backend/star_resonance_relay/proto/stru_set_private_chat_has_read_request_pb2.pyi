from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPrivateChatHasReadRequest(_message.Message):
    __slots__ = ("target_id", "max_read_msg_id")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_READ_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    max_read_msg_id: int
    def __init__(self, target_id: _Optional[int] = ..., max_read_msg_id: _Optional[int] = ...) -> None: ...
