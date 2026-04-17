import stru_mahjong_operation_pb2 as _stru_mahjong_operation_pb2
import stru_mahjong_player_self_pb2 as _stru_mahjong_player_self_pb2
import stru_mahjong_player_show_pb2 as _stru_mahjong_player_show_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongSyncOpMessage(_message.Message):
    __slots__ = ("operation", "doras", "current_index", "lizhi_count", "honba_counter", "card_index", "players", "player_self")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DORAS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    LIZHI_COUNT_FIELD_NUMBER: _ClassVar[int]
    HONBA_COUNTER_FIELD_NUMBER: _ClassVar[int]
    CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SELF_FIELD_NUMBER: _ClassVar[int]
    operation: _stru_mahjong_operation_pb2.MahjongOperation
    doras: _containers.RepeatedScalarFieldContainer[int]
    current_index: int
    lizhi_count: int
    honba_counter: int
    card_index: int
    players: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_player_show_pb2.MahjongPlayerShow]
    player_self: _stru_mahjong_player_self_pb2.MahjongPlayerSelf
    def __init__(self, operation: _Optional[_Union[_stru_mahjong_operation_pb2.MahjongOperation, _Mapping]] = ..., doras: _Optional[_Iterable[int]] = ..., current_index: _Optional[int] = ..., lizhi_count: _Optional[int] = ..., honba_counter: _Optional[int] = ..., card_index: _Optional[int] = ..., players: _Optional[_Iterable[_Union[_stru_mahjong_player_show_pb2.MahjongPlayerShow, _Mapping]]] = ..., player_self: _Optional[_Union[_stru_mahjong_player_self_pb2.MahjongPlayerSelf, _Mapping]] = ...) -> None: ...
