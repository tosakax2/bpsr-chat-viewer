from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyMahjongActionRequest(_message.Message):
    __slots__ = ("action_id", "action_param", "data")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    action_param: int
    data: bytes
    def __init__(self, action_id: _Optional[int] = ..., action_param: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
