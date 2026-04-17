import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapStickerTableBase(_message.Message):
    __slots__ = ("id", "name", "icon", "number", "sort_id", "des", "task_id", "award_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon: str
    number: int
    sort_id: int
    des: _table_basic_pb2.mlstring
    task_id: _table_basic_pb2.int_array
    award_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., number: _Optional[int] = ..., sort_id: _Optional[int] = ..., des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., task_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., award_id: _Optional[int] = ...) -> None: ...

class MapStickerTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapStickerTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapStickerTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MapStickerTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MapStickerTableBase]] = ...) -> None: ...
