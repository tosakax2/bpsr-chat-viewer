from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReqTransferPresidentRequest(_message.Message):
    __slots__ = ("union_id", "v_new_president_id")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    V_NEW_PRESIDENT_ID_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    v_new_president_id: int
    def __init__(self, union_id: _Optional[int] = ..., v_new_president_id: _Optional[int] = ...) -> None: ...
