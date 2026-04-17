import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapStickerTaskTableBase(_message.Message):
    __slots__ = ("id", "target_id", "title", "des", "target_num")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_id: _table_basic_pb2.int_array
    title: _table_basic_pb2.mlstring
    des: _table_basic_pb2.mlstring
    target_num: int
    def __init__(self, id: _Optional[int] = ..., target_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., target_num: _Optional[int] = ...) -> None: ...

class MapStickerTaskTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapStickerTaskTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapStickerTaskTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MapStickerTaskTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MapStickerTaskTableBase]] = ...) -> None: ...
