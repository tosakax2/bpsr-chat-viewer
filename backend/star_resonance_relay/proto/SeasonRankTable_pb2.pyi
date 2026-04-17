import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonRankTableBase(_message.Message):
    __slots__ = ("id", "rank_id", "des", "name", "star_level", "icon_big", "icon_min", "season_id", "conditions", "echo_points", "reward_id", "core_reward_id", "final_reward_id", "promotion_type", "back_rank_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    RANK_ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STAR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ICON_BIG_FIELD_NUMBER: _ClassVar[int]
    ICON_MIN_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ECHO_POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACK_RANK_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    rank_id: int
    des: str
    name: _table_basic_pb2.mlstring
    star_level: int
    icon_big: str
    icon_min: str
    season_id: int
    conditions: _table_basic_pb2.int_table
    echo_points: _table_basic_pb2.int_table
    reward_id: int
    core_reward_id: _table_basic_pb2.int_table
    final_reward_id: _table_basic_pb2.int_table
    promotion_type: int
    back_rank_id: int
    def __init__(self, id: _Optional[int] = ..., rank_id: _Optional[int] = ..., des: _Optional[str] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., star_level: _Optional[int] = ..., icon_big: _Optional[str] = ..., icon_min: _Optional[str] = ..., season_id: _Optional[int] = ..., conditions: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., echo_points: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., reward_id: _Optional[int] = ..., core_reward_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., final_reward_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., promotion_type: _Optional[int] = ..., back_rank_id: _Optional[int] = ...) -> None: ...

class SeasonRankTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonRankTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonRankTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonRankTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonRankTableBase]] = ...) -> None: ...
