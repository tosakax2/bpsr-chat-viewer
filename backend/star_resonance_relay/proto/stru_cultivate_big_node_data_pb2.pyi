from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CultivateBigNodeData(_message.Message):
    __slots__ = ("fantasy_id",)
    FANTASY_ID_FIELD_NUMBER: _ClassVar[int]
    fantasy_id: int
    def __init__(self, fantasy_id: _Optional[int] = ...) -> None: ...
