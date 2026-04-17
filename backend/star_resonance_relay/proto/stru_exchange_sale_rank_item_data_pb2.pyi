from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleRankItemData(_message.Message):
    __slots__ = ("rank_idx", "rate")
    RANK_IDX_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    rank_idx: int
    rate: int
    def __init__(self, rank_idx: _Optional[int] = ..., rate: _Optional[int] = ...) -> None: ...
