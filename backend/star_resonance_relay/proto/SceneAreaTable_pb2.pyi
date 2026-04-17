import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAreaTableBase(_message.Message):
    __slots__ = ("id", "name", "station", "region", "bgm_event", "name_position")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    BGM_EVENT_FIELD_NUMBER: _ClassVar[int]
    NAME_POSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    station: _table_basic_pb2.int_array
    region: int
    bgm_event: str
    name_position: _table_basic_pb2.number_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., station: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., region: _Optional[int] = ..., bgm_event: _Optional[str] = ..., name_position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ...) -> None: ...

class SceneAreaTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneAreaTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneAreaTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneAreaTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneAreaTableBase]] = ...) -> None: ...
