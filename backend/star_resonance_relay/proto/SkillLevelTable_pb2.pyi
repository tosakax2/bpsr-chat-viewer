import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillLevelTableBase(_message.Message):
    __slots__ = ("id", "cost", "extra_cost")
    ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COST_FIELD_NUMBER: _ClassVar[int]
    id: int
    cost: _table_basic_pb2.int_table
    extra_cost: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., extra_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class SkillLevelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SkillLevelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SkillLevelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SkillLevelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SkillLevelTableBase]] = ...) -> None: ...
