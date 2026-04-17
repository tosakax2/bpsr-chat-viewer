from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NewbieBackflowTargetData(_message.Message):
    __slots__ = ("id", "target_num", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_num: int
    state: int
    def __init__(self, id: _Optional[int] = ..., target_num: _Optional[int] = ..., state: _Optional[int] = ...) -> None: ...
