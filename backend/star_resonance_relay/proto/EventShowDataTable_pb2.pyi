import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventShowDataTableBase(_message.Message):
    __slots__ = ("id", "start", "duration", "end", "is_attacker", "state_id", "group_id", "event_type", "param_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    start: float
    duration: float
    end: float
    is_attacker: bool
    state_id: int
    group_id: int
    event_type: int
    param_list: _table_basic_pb2.string_table
    def __init__(self, id: _Optional[int] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., end: _Optional[float] = ..., is_attacker: bool = ..., state_id: _Optional[int] = ..., group_id: _Optional[int] = ..., event_type: _Optional[int] = ..., param_list: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ...) -> None: ...

class EventShowDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EventShowDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EventShowDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EventShowDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EventShowDataTableBase]] = ...) -> None: ...
