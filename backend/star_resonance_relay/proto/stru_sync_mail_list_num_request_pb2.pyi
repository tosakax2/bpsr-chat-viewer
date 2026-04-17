from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncMailListNumRequest(_message.Message):
    __slots__ = ("normal_num", "important_num", "normal_un_read_list", "important_un_read_list", "collect_num", "collect_un_read_list")
    NORMAL_NUM_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_NUM_FIELD_NUMBER: _ClassVar[int]
    NORMAL_UN_READ_LIST_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_UN_READ_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECT_NUM_FIELD_NUMBER: _ClassVar[int]
    COLLECT_UN_READ_LIST_FIELD_NUMBER: _ClassVar[int]
    normal_num: int
    important_num: int
    normal_un_read_list: _containers.RepeatedScalarFieldContainer[int]
    important_un_read_list: _containers.RepeatedScalarFieldContainer[int]
    collect_num: int
    collect_un_read_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, normal_num: _Optional[int] = ..., important_num: _Optional[int] = ..., normal_un_read_list: _Optional[_Iterable[int]] = ..., important_un_read_list: _Optional[_Iterable[int]] = ..., collect_num: _Optional[int] = ..., collect_un_read_list: _Optional[_Iterable[int]] = ...) -> None: ...
