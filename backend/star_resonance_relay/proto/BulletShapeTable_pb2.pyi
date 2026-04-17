import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BulletShapeTableBase(_message.Message):
    __slots__ = ("id", "shape_type", "shape_data", "scale_curve", "scale_curve_sample")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHAPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_DATA_FIELD_NUMBER: _ClassVar[int]
    SCALE_CURVE_FIELD_NUMBER: _ClassVar[int]
    SCALE_CURVE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    shape_type: int
    shape_data: _table_basic_pb2.number_array
    scale_curve: _table_basic_pb2.number_table
    scale_curve_sample: _table_basic_pb2.number_table
    def __init__(self, id: _Optional[int] = ..., shape_type: _Optional[int] = ..., shape_data: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., scale_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., scale_curve_sample: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ...) -> None: ...

class BulletShapeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BulletShapeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BulletShapeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BulletShapeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BulletShapeTableBase]] = ...) -> None: ...
