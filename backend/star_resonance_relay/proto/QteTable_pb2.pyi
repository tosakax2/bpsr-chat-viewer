import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QteTableBase(_message.Message):
    __slots__ = ("id", "name", "qte_type", "ui_type", "max_time", "time_quantum", "trigger_count", "trigger_time", "play_skill", "buff_id_when_success", "buff_id_when_failure", "qte_show_skill_id", "event_params", "function_id", "impact_function_id", "impact_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UI_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_QUANTUM_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAY_SKILL_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_WHEN_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_WHEN_FAILURE_FIELD_NUMBER: _ClassVar[int]
    QTE_SHOW_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    IMPACT_FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    IMPACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    qte_type: int
    ui_type: int
    max_time: float
    time_quantum: _table_basic_pb2.number_table
    trigger_count: _table_basic_pb2.int_array
    trigger_time: _table_basic_pb2.number_table
    play_skill: _table_basic_pb2.int_table
    buff_id_when_success: _table_basic_pb2.int_table
    buff_id_when_failure: _table_basic_pb2.int_array
    qte_show_skill_id: int
    event_params: _table_basic_pb2.number_table
    function_id: int
    impact_function_id: _table_basic_pb2.int_array
    impact_type: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., qte_type: _Optional[int] = ..., ui_type: _Optional[int] = ..., max_time: _Optional[float] = ..., time_quantum: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., trigger_count: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., trigger_time: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., play_skill: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_id_when_success: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_id_when_failure: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., qte_show_skill_id: _Optional[int] = ..., event_params: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., function_id: _Optional[int] = ..., impact_function_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., impact_type: _Optional[int] = ...) -> None: ...

class QteTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QteTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QteTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QteTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QteTableBase]] = ...) -> None: ...
