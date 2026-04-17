from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahJongHandleMessage(_message.Message):
    __slots__ = ("Handle_", "handle_card", "cards", "discard_index")
    HANDLE__FIELD_NUMBER: _ClassVar[int]
    HANDLE_CARD_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    DISCARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    Handle_: int
    handle_card: int
    cards: _containers.RepeatedScalarFieldContainer[int]
    discard_index: int
    def __init__(self, Handle_: _Optional[int] = ..., handle_card: _Optional[int] = ..., cards: _Optional[_Iterable[int]] = ..., discard_index: _Optional[int] = ...) -> None: ...
