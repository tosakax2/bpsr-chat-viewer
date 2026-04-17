import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldEventTableBase(_message.Message):
    __slots__ = ("event_id", "name", "event_type", "score", "timer_id", "notice_time", "cycle", "last_time", "event_form", "count", "alert", "award", "full_award", "start_message", "phase_time")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TIME_FIELD_NUMBER: _ClassVar[int]
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FORM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    FULL_AWARD_FIELD_NUMBER: _ClassVar[int]
    START_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PHASE_TIME_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    name: str
    event_type: int
    score: int
    timer_id: int
    notice_time: int
    cycle: int
    last_time: int
    event_form: _table_basic_pb2.int_array
    count: int
    alert: int
    award: int
    full_award: _table_basic_pb2.int_table
    start_message: int
    phase_time: str
    def __init__(self, event_id: _Optional[int] = ..., name: _Optional[str] = ..., event_type: _Optional[int] = ..., score: _Optional[int] = ..., timer_id: _Optional[int] = ..., notice_time: _Optional[int] = ..., cycle: _Optional[int] = ..., last_time: _Optional[int] = ..., event_form: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., count: _Optional[int] = ..., alert: _Optional[int] = ..., award: _Optional[int] = ..., full_award: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., start_message: _Optional[int] = ..., phase_time: _Optional[str] = ...) -> None: ...

class WorldEventTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WorldEventTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WorldEventTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WorldEventTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WorldEventTableBase]] = ...) -> None: ...
