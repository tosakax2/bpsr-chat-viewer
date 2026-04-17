import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleRecord(_message.Message):
    __slots__ = ("num", "rate", "money", "time", "item_info")
    NUM_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    num: int
    rate: int
    money: int
    time: int
    item_info: _stru_item_pb2.Item
    def __init__(self, num: _Optional[int] = ..., rate: _Optional[int] = ..., money: _Optional[int] = ..., time: _Optional[int] = ..., item_info: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
