from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RechargeData(_message.Message):
    __slots__ = ("accumulate_amount", "last_recharge_time", "last_recharge_amount", "last_diamond_amount")
    ACCUMULATE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_RECHARGE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_RECHARGE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_DIAMOND_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    accumulate_amount: int
    last_recharge_time: int
    last_recharge_amount: int
    last_diamond_amount: int
    def __init__(self, accumulate_amount: _Optional[int] = ..., last_recharge_time: _Optional[int] = ..., last_recharge_amount: _Optional[int] = ..., last_diamond_amount: _Optional[int] = ...) -> None: ...
