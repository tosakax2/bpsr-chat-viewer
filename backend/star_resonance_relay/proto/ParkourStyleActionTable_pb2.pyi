import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParkourStyleActionTableBase(_message.Message):
    __slots__ = ("id", "name", "level", "energy_value", "wait_time", "dot")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENERGY_VALUE_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    DOT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    level: int
    energy_value: int
    wait_time: float
    dot: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., level: _Optional[int] = ..., energy_value: _Optional[int] = ..., wait_time: _Optional[float] = ..., dot: _Optional[int] = ...) -> None: ...

class ParkourStyleActionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ParkourStyleActionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ParkourStyleActionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ParkourStyleActionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ParkourStyleActionTableBase]] = ...) -> None: ...
