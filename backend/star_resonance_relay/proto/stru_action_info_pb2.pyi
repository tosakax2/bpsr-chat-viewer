from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActionInfo(_message.Message):
    __slots__ = ("action_id", "period", "percent")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    period: int
    percent: float
    def __init__(self, action_id: _Optional[int] = ..., period: _Optional[int] = ..., percent: _Optional[float] = ...) -> None: ...
