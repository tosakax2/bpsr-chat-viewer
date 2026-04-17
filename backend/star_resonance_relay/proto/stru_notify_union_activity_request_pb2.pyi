from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionActivityRequest(_message.Message):
    __slots__ = ("activity_id", "notify_type")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_TYPE_FIELD_NUMBER: _ClassVar[int]
    activity_id: int
    notify_type: int
    def __init__(self, activity_id: _Optional[int] = ..., notify_type: _Optional[int] = ...) -> None: ...
