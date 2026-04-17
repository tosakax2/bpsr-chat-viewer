import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferTableBase(_message.Message):
    __slots__ = ("id", "name", "pivot_id", "transfer_dec", "scene_point", "award_id", "is_on", "scene_tag")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PIVOT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_DEC_FIELD_NUMBER: _ClassVar[int]
    SCENE_POINT_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ON_FIELD_NUMBER: _ClassVar[int]
    SCENE_TAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    pivot_id: int
    transfer_dec: _table_basic_pb2.mlstring
    scene_point: int
    award_id: _table_basic_pb2.int_array
    is_on: bool
    scene_tag: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., pivot_id: _Optional[int] = ..., transfer_dec: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., scene_point: _Optional[int] = ..., award_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_on: bool = ..., scene_tag: _Optional[int] = ...) -> None: ...

class TransferTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TransferTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TransferTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TransferTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TransferTableBase]] = ...) -> None: ...
