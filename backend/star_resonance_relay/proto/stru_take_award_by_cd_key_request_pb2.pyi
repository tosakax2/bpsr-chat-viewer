from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeAwardByCdKeyRequest(_message.Message):
    __slots__ = ("cd_key",)
    CD_KEY_FIELD_NUMBER: _ClassVar[int]
    cd_key: str
    def __init__(self, cd_key: _Optional[str] = ...) -> None: ...
