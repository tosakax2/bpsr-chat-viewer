from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionData(_message.Message):
    __slots__ = ("unionid", "name", "union_hunt_rank")
    UNIONID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_HUNT_RANK_FIELD_NUMBER: _ClassVar[int]
    unionid: int
    name: str
    union_hunt_rank: int
    def __init__(self, unionid: _Optional[int] = ..., name: _Optional[str] = ..., union_hunt_rank: _Optional[int] = ...) -> None: ...
