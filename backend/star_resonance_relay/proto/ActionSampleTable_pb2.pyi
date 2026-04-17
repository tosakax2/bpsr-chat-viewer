import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionSampleTableBase(_message.Message):
    __slots__ = ("id", "name", "motion_info", "has_motion")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MOTION_INFO_FIELD_NUMBER: _ClassVar[int]
    HAS_MOTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    motion_info: _table_basic_pb2.number_table
    has_motion: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., motion_info: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., has_motion: bool = ...) -> None: ...

class ActionSampleTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ActionSampleTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ActionSampleTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ActionSampleTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ActionSampleTableBase]] = ...) -> None: ...
