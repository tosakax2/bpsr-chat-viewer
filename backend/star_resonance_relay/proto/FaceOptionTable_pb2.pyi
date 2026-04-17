import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceOptionTableBase(_message.Message):
    __slots__ = ("id", "option", "color_group", "random", "random_type", "tab")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    COLOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    RANDOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAB_FIELD_NUMBER: _ClassVar[int]
    id: int
    option: int
    color_group: int
    random: int
    random_type: _table_basic_pb2.int_table
    tab: int
    def __init__(self, id: _Optional[int] = ..., option: _Optional[int] = ..., color_group: _Optional[int] = ..., random: _Optional[int] = ..., random_type: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., tab: _Optional[int] = ...) -> None: ...

class FaceOptionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FaceOptionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FaceOptionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FaceOptionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FaceOptionTableBase]] = ...) -> None: ...
