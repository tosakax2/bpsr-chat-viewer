from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffChange(_message.Message):
    __slots__ = ("layer", "duration", "create_time")
    LAYER_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    layer: int
    duration: int
    create_time: int
    def __init__(self, layer: _Optional[int] = ..., duration: _Optional[int] = ..., create_time: _Optional[int] = ...) -> None: ...
