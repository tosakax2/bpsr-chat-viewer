from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientCustomEventParams(_message.Message):
    __slots__ = ("custom_event_id",)
    CUSTOM_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    custom_event_id: int
    def __init__(self, custom_event_id: _Optional[int] = ...) -> None: ...
