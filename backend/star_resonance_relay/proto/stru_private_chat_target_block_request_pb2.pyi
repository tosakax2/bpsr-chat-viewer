from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateChatTargetBlockRequest(_message.Message):
    __slots__ = ("target_id", "set_block")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SET_BLOCK_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    set_block: bool
    def __init__(self, target_id: _Optional[int] = ..., set_block: bool = ...) -> None: ...
