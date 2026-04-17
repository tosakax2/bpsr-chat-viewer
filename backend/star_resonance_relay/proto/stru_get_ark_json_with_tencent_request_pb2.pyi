from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetArkJsonWithTencentRequest(_message.Message):
    __slots__ = ("selef_open_id", "selef_token")
    SELEF_OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    SELEF_TOKEN_FIELD_NUMBER: _ClassVar[int]
    selef_open_id: str
    selef_token: str
    def __init__(self, selef_open_id: _Optional[str] = ..., selef_token: _Optional[str] = ...) -> None: ...
