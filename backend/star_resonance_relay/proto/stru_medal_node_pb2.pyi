from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MedalNode(_message.Message):
    __slots__ = ("node_id", "node_level", "choose", "slot")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    node_level: int
    choose: bool
    slot: int
    def __init__(self, node_id: _Optional[int] = ..., node_level: _Optional[int] = ..., choose: bool = ..., slot: _Optional[int] = ...) -> None: ...
