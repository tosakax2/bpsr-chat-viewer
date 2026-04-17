from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KickOutRequest(_message.Message):
    __slots__ = ("v_mem_id",)
    V_MEM_ID_FIELD_NUMBER: _ClassVar[int]
    v_mem_id: int
    def __init__(self, v_mem_id: _Optional[int] = ...) -> None: ...
