import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoParamTableBase(_message.Message):
    __slots__ = ("id", "des", "point_id", "distance_take", "distance_hint", "angle", "target_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TAKE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_HINT_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: _table_basic_pb2.mlstring
    point_id: int
    distance_take: _table_basic_pb2.vector2
    distance_hint: _table_basic_pb2.vector2
    angle: _table_basic_pb2.vector2
    target_id: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., point_id: _Optional[int] = ..., distance_take: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., distance_hint: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., angle: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., target_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class PhotoParamTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PhotoParamTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PhotoParamTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PhotoParamTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PhotoParamTableBase]] = ...) -> None: ...
