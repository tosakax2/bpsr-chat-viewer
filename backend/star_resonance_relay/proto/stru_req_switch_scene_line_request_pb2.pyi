from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReqSwitchSceneLineRequest(_message.Message):
    __slots__ = ("line_id", "target_char_id")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: int
    target_char_id: int
    def __init__(self, line_id: _Optional[int] = ..., target_char_id: _Optional[int] = ...) -> None: ...
