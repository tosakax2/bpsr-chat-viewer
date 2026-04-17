from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongOpenMeld(_message.Message):
    __slots__ = ("meld_type", "cards", "card", "from_player_index")
    MELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    meld_type: int
    cards: _containers.RepeatedScalarFieldContainer[int]
    card: int
    from_player_index: int
    def __init__(self, meld_type: _Optional[int] = ..., cards: _Optional[_Iterable[int]] = ..., card: _Optional[int] = ..., from_player_index: _Optional[int] = ...) -> None: ...
