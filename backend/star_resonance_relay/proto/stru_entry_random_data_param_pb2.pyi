from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EntryRandomDataParam(_message.Message):
    __slots__ = ("refresh_cnt", "ids", "obj_uuid", "dead_timestamp")
    REFRESH_CNT_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    refresh_cnt: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    obj_uuid: int
    dead_timestamp: int
    def __init__(self, refresh_cnt: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., obj_uuid: _Optional[int] = ..., dead_timestamp: _Optional[int] = ...) -> None: ...
