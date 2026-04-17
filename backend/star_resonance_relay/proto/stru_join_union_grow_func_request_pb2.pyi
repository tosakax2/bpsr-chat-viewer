from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JoinUnionGrowFuncRequest(_message.Message):
    __slots__ = ("union_id", "grow_func_pos")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    GROW_FUNC_POS_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    grow_func_pos: int
    def __init__(self, union_id: _Optional[int] = ..., grow_func_pos: _Optional[int] = ...) -> None: ...
