import stru_mahjong_operation_pb2 as _stru_mahjong_operation_pb2
import stru_mahjong_player_self_pb2 as _stru_mahjong_player_self_pb2
import stru_mahjong_player_show_pb2 as _stru_mahjong_player_show_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongSyncMessage(_message.Message):
    __slots__ = ("dealer_index", "wind", "wait_time", "doras", "operations", "current_index", "card_index", "players", "player_self", "lizhi_count", "honba_counter", "zhuang_counter", "force_refresh", "mahjong_table_guid")
    DEALER_INDEX_FIELD_NUMBER: _ClassVar[int]
    WIND_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    DORAS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SELF_FIELD_NUMBER: _ClassVar[int]
    LIZHI_COUNT_FIELD_NUMBER: _ClassVar[int]
    HONBA_COUNTER_FIELD_NUMBER: _ClassVar[int]
    ZHUANG_COUNTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    MAHJONG_TABLE_GUID_FIELD_NUMBER: _ClassVar[int]
    dealer_index: int
    wind: int
    wait_time: int
    doras: _containers.RepeatedScalarFieldContainer[int]
    operations: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_operation_pb2.MahjongOperation]
    current_index: int
    card_index: int
    players: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_player_show_pb2.MahjongPlayerShow]
    player_self: _stru_mahjong_player_self_pb2.MahjongPlayerSelf
    lizhi_count: int
    honba_counter: int
    zhuang_counter: int
    force_refresh: bool
    mahjong_table_guid: str
    def __init__(self, dealer_index: _Optional[int] = ..., wind: _Optional[int] = ..., wait_time: _Optional[int] = ..., doras: _Optional[_Iterable[int]] = ..., operations: _Optional[_Iterable[_Union[_stru_mahjong_operation_pb2.MahjongOperation, _Mapping]]] = ..., current_index: _Optional[int] = ..., card_index: _Optional[int] = ..., players: _Optional[_Iterable[_Union[_stru_mahjong_player_show_pb2.MahjongPlayerShow, _Mapping]]] = ..., player_self: _Optional[_Union[_stru_mahjong_player_self_pb2.MahjongPlayerSelf, _Mapping]] = ..., lizhi_count: _Optional[int] = ..., honba_counter: _Optional[int] = ..., zhuang_counter: _Optional[int] = ..., force_refresh: bool = ..., mahjong_table_guid: _Optional[str] = ...) -> None: ...
