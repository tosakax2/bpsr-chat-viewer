import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StaticInteractiveObjectTableBase(_message.Message):
    __slots__ = ("id", "position", "roty", "class_id", "radius", "trigger_position", "interaction_template", "interaction_event", "source_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTY_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_POSITION_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    position: _table_basic_pb2.number_array
    roty: _table_basic_pb2.number_array
    class_id: int
    radius: _table_basic_pb2.number_array
    trigger_position: _table_basic_pb2.number_array
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    source_type: int
    def __init__(self, id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., roty: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., class_id: _Optional[int] = ..., radius: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., trigger_position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., source_type: _Optional[int] = ...) -> None: ...

class StaticInteractiveObjectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StaticInteractiveObjectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StaticInteractiveObjectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, StaticInteractiveObjectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, StaticInteractiveObjectTableBase]] = ...) -> None: ...
