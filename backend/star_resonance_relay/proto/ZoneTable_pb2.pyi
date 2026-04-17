import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneTableBase(_message.Message):
    __slots__ = ("id", "name", "model_id", "effect_path", "status_info", "status_transition", "default_state", "interaction_template", "interaction_event", "show_status_info", "show_status_transition")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    model_id: int
    effect_path: str
    status_info: _table_basic_pb2.int_table
    status_transition: _table_basic_pb2.int_table
    default_state: int
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    show_status_info: _table_basic_pb2.int_table
    show_status_transition: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., model_id: _Optional[int] = ..., effect_path: _Optional[str] = ..., status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., default_state: _Optional[int] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., show_status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., show_status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ZoneTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ZoneTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ZoneTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ZoneTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ZoneTableBase]] = ...) -> None: ...
