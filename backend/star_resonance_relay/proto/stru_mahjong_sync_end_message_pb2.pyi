import stru_mahjong_operation_pb2 as _stru_mahjong_operation_pb2
import stru_mahjong_player_show_pb2 as _stru_mahjong_player_show_pb2
import stru_mahjong_settle_pb2 as _stru_mahjong_settle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongSyncEndMessage(_message.Message):
    __slots__ = ("doras", "in_doras", "current_index", "card_index", "final_players", "final_settles", "operations")
    DORAS_FIELD_NUMBER: _ClassVar[int]
    IN_DORAS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINAL_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_SETTLES_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[int]
    in_doras: _containers.RepeatedScalarFieldContainer[int]
    current_index: int
    card_index: int
    final_players: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_player_show_pb2.MahjongPlayerShow]
    final_settles: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_settle_pb2.MahjongSettle]
    operations: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_operation_pb2.MahjongOperation]
    def __init__(self, doras: _Optional[_Iterable[int]] = ..., in_doras: _Optional[_Iterable[int]] = ..., current_index: _Optional[int] = ..., card_index: _Optional[int] = ..., final_players: _Optional[_Iterable[_Union[_stru_mahjong_player_show_pb2.MahjongPlayerShow, _Mapping]]] = ..., final_settles: _Optional[_Iterable[_Union[_stru_mahjong_settle_pb2.MahjongSettle, _Mapping]]] = ..., operations: _Optional[_Iterable[_Union[_stru_mahjong_operation_pb2.MahjongOperation, _Mapping]]] = ...) -> None: ...
