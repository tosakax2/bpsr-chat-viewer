import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceTableBase(_message.Message):
    __slots__ = ("id", "type", "sex", "model", "sort_id", "icon", "resource", "unlock", "create", "is_hide", "weight", "face_shape_id", "number")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    IS_HIDE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    FACE_SHAPE_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    sex: int
    model: _table_basic_pb2.int_array
    sort_id: int
    icon: str
    resource: str
    unlock: _table_basic_pb2.int_table
    create: int
    is_hide: int
    weight: int
    face_shape_id: int
    number: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., sex: _Optional[int] = ..., model: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., sort_id: _Optional[int] = ..., icon: _Optional[str] = ..., resource: _Optional[str] = ..., unlock: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., create: _Optional[int] = ..., is_hide: _Optional[int] = ..., weight: _Optional[int] = ..., face_shape_id: _Optional[int] = ..., number: _Optional[int] = ...) -> None: ...

class FaceTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FaceTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FaceTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FaceTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FaceTableBase]] = ...) -> None: ...
