from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionEvent(_message.Message):
    __slots__ = ("event_id", "event_time", "event_param")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_PARAM_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_time: int
    event_param: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event_id: _Optional[int] = ..., event_time: _Optional[int] = ..., event_param: _Optional[_Iterable[str]] = ...) -> None: ...
