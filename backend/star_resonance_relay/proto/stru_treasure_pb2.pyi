import stru_treasure_item_row_pb2 as _stru_treasure_item_row_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Treasure(_message.Message):
    __slots__ = ("rows", "history_rows", "flag", "refresh_time", "selected_reward", "season_id", "last_season_id", "last_refresh_time")
    class RowsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_treasure_item_row_pb2.TreasureItemRow
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_treasure_item_row_pb2.TreasureItemRow, _Mapping]] = ...) -> None: ...
    class HistoryRowsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_treasure_item_row_pb2.TreasureItemRow
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_treasure_item_row_pb2.TreasureItemRow, _Mapping]] = ...) -> None: ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ROWS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_REWARD_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.MessageMap[int, _stru_treasure_item_row_pb2.TreasureItemRow]
    history_rows: _containers.MessageMap[int, _stru_treasure_item_row_pb2.TreasureItemRow]
    flag: bool
    refresh_time: int
    selected_reward: _containers.RepeatedScalarFieldContainer[int]
    season_id: int
    last_season_id: int
    last_refresh_time: int
    def __init__(self, rows: _Optional[_Mapping[int, _stru_treasure_item_row_pb2.TreasureItemRow]] = ..., history_rows: _Optional[_Mapping[int, _stru_treasure_item_row_pb2.TreasureItemRow]] = ..., flag: bool = ..., refresh_time: _Optional[int] = ..., selected_reward: _Optional[_Iterable[int]] = ..., season_id: _Optional[int] = ..., last_season_id: _Optional[int] = ..., last_refresh_time: _Optional[int] = ...) -> None: ...
