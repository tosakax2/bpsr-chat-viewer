import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceStickerTableBase(_message.Message):
    __slots__ = ("id", "default_color", "color_id", "back", "move", "rotate", "scale", "default_scale", "default_position", "default_rotate")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COLOR_FIELD_NUMBER: _ClassVar[int]
    COLOR_ID_FIELD_NUMBER: _ClassVar[int]
    BACK_FIELD_NUMBER: _ClassVar[int]
    MOVE_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCALE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROTATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    default_color: _table_basic_pb2.int_array
    color_id: int
    back: int
    move: int
    rotate: int
    scale: int
    default_scale: _table_basic_pb2.vector3
    default_position: _table_basic_pb2.vector2
    default_rotate: float
    def __init__(self, id: _Optional[int] = ..., default_color: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., color_id: _Optional[int] = ..., back: _Optional[int] = ..., move: _Optional[int] = ..., rotate: _Optional[int] = ..., scale: _Optional[int] = ..., default_scale: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., default_position: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., default_rotate: _Optional[float] = ...) -> None: ...

class FaceStickerTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FaceStickerTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FaceStickerTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FaceStickerTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FaceStickerTableBase]] = ...) -> None: ...
