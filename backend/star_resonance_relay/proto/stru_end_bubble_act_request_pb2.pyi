from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EndBubbleActRequest(_message.Message):
    __slots__ = ("bubble_act_id",)
    BUBBLE_ACT_ID_FIELD_NUMBER: _ClassVar[int]
    bubble_act_id: int
    def __init__(self, bubble_act_id: _Optional[int] = ...) -> None: ...
