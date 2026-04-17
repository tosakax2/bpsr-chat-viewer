import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEventTableBase(_message.Message):
    __slots__ = ("id", "name", "target_list", "difficult", "complete_action", "time")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    DIFFICULT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    target_list: _table_basic_pb2.int_array
    difficult: int
    complete_action: _table_basic_pb2.int_table
    time: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., target_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., difficult: _Optional[int] = ..., complete_action: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., time: _Optional[int] = ...) -> None: ...

class SceneEventTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneEventTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneEventTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneEventTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneEventTableBase]] = ...) -> None: ...
