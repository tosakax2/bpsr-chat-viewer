import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementTableBase(_message.Message):
    __slots__ = ("id", "name", "main_type", "sub_type", "desc", "show", "time_limit", "award", "icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    main_type: int
    sub_type: int
    desc: str
    show: int
    time_limit: int
    award: _table_basic_pb2.int_table
    icon: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., main_type: _Optional[int] = ..., sub_type: _Optional[int] = ..., desc: _Optional[str] = ..., show: _Optional[int] = ..., time_limit: _Optional[int] = ..., award: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., icon: _Optional[str] = ...) -> None: ...

class AchievementTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AchievementTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AchievementTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AchievementTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AchievementTableBase]] = ...) -> None: ...
