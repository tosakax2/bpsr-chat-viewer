import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PivotTableBase(_message.Message):
    __slots__ = ("id", "name", "map_id", "area_name", "setting_off_num", "circulate_award", "pivot_pic", "pivot_area", "camera_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    AREA_NAME_FIELD_NUMBER: _ClassVar[int]
    SETTING_OFF_NUM_FIELD_NUMBER: _ClassVar[int]
    CIRCULATE_AWARD_FIELD_NUMBER: _ClassVar[int]
    PIVOT_PIC_FIELD_NUMBER: _ClassVar[int]
    PIVOT_AREA_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    map_id: int
    area_name: _table_basic_pb2.mlstring
    setting_off_num: _table_basic_pb2.int_array
    circulate_award: _table_basic_pb2.int_array
    pivot_pic: str
    pivot_area: int
    camera_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., map_id: _Optional[int] = ..., area_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., setting_off_num: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., circulate_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pivot_pic: _Optional[str] = ..., pivot_area: _Optional[int] = ..., camera_id: _Optional[int] = ...) -> None: ...

class PivotTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PivotTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PivotTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PivotTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PivotTableBase]] = ...) -> None: ...
