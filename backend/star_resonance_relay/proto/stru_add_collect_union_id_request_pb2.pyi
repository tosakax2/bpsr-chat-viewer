from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddCollectUnionIdRequest(_message.Message):
    __slots__ = ("union_id",)
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    def __init__(self, union_id: _Optional[int] = ...) -> None: ...
