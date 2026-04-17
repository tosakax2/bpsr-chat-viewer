from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonRankInfo(_message.Message):
    __slots__ = ("cur_ran_k_star", "received_rank_star")
    CUR_RAN_K_STAR_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_RANK_STAR_FIELD_NUMBER: _ClassVar[int]
    cur_ran_k_star: int
    received_rank_star: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, cur_ran_k_star: _Optional[int] = ..., received_rank_star: _Optional[_Iterable[int]] = ...) -> None: ...
