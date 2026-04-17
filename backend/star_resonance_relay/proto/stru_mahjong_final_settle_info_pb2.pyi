from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongFinalSettleInfo(_message.Message):
    __slots__ = ("player_id", "coin", "scoring_point", "rank_score", "coin_change")
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    SCORING_POINT_FIELD_NUMBER: _ClassVar[int]
    RANK_SCORE_FIELD_NUMBER: _ClassVar[int]
    COIN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    coin: int
    scoring_point: int
    rank_score: int
    coin_change: int
    def __init__(self, player_id: _Optional[int] = ..., coin: _Optional[int] = ..., scoring_point: _Optional[int] = ..., rank_score: _Optional[int] = ..., coin_change: _Optional[int] = ...) -> None: ...
