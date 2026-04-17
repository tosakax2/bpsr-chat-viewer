from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ArkShareWithTencentRequest(_message.Message):
    __slots__ = ("target_char_id", "selef_open_id", "selef_token")
    TARGET_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SELEF_OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    SELEF_TOKEN_FIELD_NUMBER: _ClassVar[int]
    target_char_id: int
    selef_open_id: str
    selef_token: str
    def __init__(self, target_char_id: _Optional[int] = ..., selef_open_id: _Optional[str] = ..., selef_token: _Optional[str] = ...) -> None: ...
