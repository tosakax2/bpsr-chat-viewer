import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapBookTableBase(_message.Message):
    __slots__ = ("id", "scene_id", "sort_id", "model", "award_id", "sticker_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    STICKER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    scene_id: int
    sort_id: int
    model: str
    award_id: int
    sticker_id: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., scene_id: _Optional[int] = ..., sort_id: _Optional[int] = ..., model: _Optional[str] = ..., award_id: _Optional[int] = ..., sticker_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class MapBookTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapBookTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapBookTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MapBookTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MapBookTableBase]] = ...) -> None: ...
