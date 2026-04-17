import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamTargetTableBase(_message.Message):
    __slots__ = ("id", "name", "has_father_type", "belong_type", "time_cycle", "time", "function_id", "relative_dungeon_id", "member_count_stop_match", "sort", "icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_FATHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    BELONG_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_CYCLE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_STOP_MATCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    has_father_type: bool
    belong_type: int
    time_cycle: str
    time: str
    function_id: int
    relative_dungeon_id: int
    member_count_stop_match: int
    sort: int
    icon: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., has_father_type: bool = ..., belong_type: _Optional[int] = ..., time_cycle: _Optional[str] = ..., time: _Optional[str] = ..., function_id: _Optional[int] = ..., relative_dungeon_id: _Optional[int] = ..., member_count_stop_match: _Optional[int] = ..., sort: _Optional[int] = ..., icon: _Optional[str] = ...) -> None: ...

class TeamTargetTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TeamTargetTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TeamTargetTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TeamTargetTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TeamTargetTableBase]] = ...) -> None: ...
