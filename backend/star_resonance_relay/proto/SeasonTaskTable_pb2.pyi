import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonTaskTableBase(_message.Message):
    __slots__ = ("target_id", "major_type", "open_day", "target_group", "target", "award_id", "show_week", "quick_jump_type", "quick_jump_param", "desc")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MAJOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPEN_DAY_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_WEEK_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_PARAM_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    major_type: int
    open_day: int
    target_group: int
    target: int
    award_id: int
    show_week: int
    quick_jump_type: int
    quick_jump_param: _table_basic_pb2.int_array
    desc: str
    def __init__(self, target_id: _Optional[int] = ..., major_type: _Optional[int] = ..., open_day: _Optional[int] = ..., target_group: _Optional[int] = ..., target: _Optional[int] = ..., award_id: _Optional[int] = ..., show_week: _Optional[int] = ..., quick_jump_type: _Optional[int] = ..., quick_jump_param: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., desc: _Optional[str] = ...) -> None: ...

class SeasonTaskTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonTaskTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonTaskTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonTaskTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonTaskTableBase]] = ...) -> None: ...
