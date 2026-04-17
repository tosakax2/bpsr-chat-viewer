import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementEntryTableBase(_message.Message):
    __slots__ = ("id", "achievement_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    achievement_list: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., achievement_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class AchievementEntryTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AchievementEntryTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AchievementEntryTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AchievementEntryTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AchievementEntryTableBase]] = ...) -> None: ...
