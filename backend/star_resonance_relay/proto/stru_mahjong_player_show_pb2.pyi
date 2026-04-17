import stru_mahjong_open_meld_pb2 as _stru_mahjong_open_meld_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongPlayerShow(_message.Message):
    __slots__ = ("player_id", "player_index", "coin", "self_wind", "lizhi", "drop_cards", "open_melds", "cards_len", "is_last_draw", "cards", "furtin", "show_data")
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    SELF_WIND_FIELD_NUMBER: _ClassVar[int]
    LIZHI_FIELD_NUMBER: _ClassVar[int]
    DROP_CARDS_FIELD_NUMBER: _ClassVar[int]
    OPEN_MELDS_FIELD_NUMBER: _ClassVar[int]
    CARDS_LEN_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_DRAW_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    FURTIN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DATA_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    player_index: int
    coin: int
    self_wind: int
    lizhi: int
    drop_cards: _containers.RepeatedScalarFieldContainer[int]
    open_melds: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_open_meld_pb2.MahjongOpenMeld]
    cards_len: int
    is_last_draw: bool
    cards: _containers.RepeatedScalarFieldContainer[int]
    furtin: int
    show_data: bytes
    def __init__(self, player_id: _Optional[int] = ..., player_index: _Optional[int] = ..., coin: _Optional[int] = ..., self_wind: _Optional[int] = ..., lizhi: _Optional[int] = ..., drop_cards: _Optional[_Iterable[int]] = ..., open_melds: _Optional[_Iterable[_Union[_stru_mahjong_open_meld_pb2.MahjongOpenMeld, _Mapping]]] = ..., cards_len: _Optional[int] = ..., is_last_draw: bool = ..., cards: _Optional[_Iterable[int]] = ..., furtin: _Optional[int] = ..., show_data: _Optional[bytes] = ...) -> None: ...
