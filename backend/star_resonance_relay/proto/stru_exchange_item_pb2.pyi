import stru_exchange_info_pb2 as _stru_exchange_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeItem(_message.Message):
    __slots__ = ("exchange_info",)
    class ExchangeInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_exchange_info_pb2.ExchangeInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_exchange_info_pb2.ExchangeInfo, _Mapping]] = ...) -> None: ...
    EXCHANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_info: _containers.MessageMap[int, _stru_exchange_info_pb2.ExchangeInfo]
    def __init__(self, exchange_info: _Optional[_Mapping[int, _stru_exchange_info_pb2.ExchangeInfo]] = ...) -> None: ...
