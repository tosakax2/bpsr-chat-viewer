import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementDateTableBase(_message.Message):
    __slots__ = ("id", "name", "target_id", "condition", "pre_achievement", "reward_id", "des", "type_icon", "season_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRE_ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    TYPE_ICON_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    target_id: _table_basic_pb2.int_array
    condition: _table_basic_pb2.int_table
    pre_achievement: int
    reward_id: int
    des: str
    type_icon: str
    season_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., target_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., pre_achievement: _Optional[int] = ..., reward_id: _Optional[int] = ..., des: _Optional[str] = ..., type_icon: _Optional[str] = ..., season_id: _Optional[int] = ...) -> None: ...

class AchievementDateTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AchievementDateTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AchievementDateTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AchievementDateTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AchievementDateTableBase]] = ...) -> None: ...
