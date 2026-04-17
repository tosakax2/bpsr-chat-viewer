import stru_exchange_data_pb2 as _stru_exchange_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeInfo(_message.Message):
    __slots__ = ("id", "exchange_data")
    class ExchangeDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_exchange_data_pb2.ExchangeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_exchange_data_pb2.ExchangeData, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_DATA_FIELD_NUMBER: _ClassVar[int]
    id: int
    exchange_data: _containers.MessageMap[int, _stru_exchange_data_pb2.ExchangeData]
    def __init__(self, id: _Optional[int] = ..., exchange_data: _Optional[_Mapping[int, _stru_exchange_data_pb2.ExchangeData]] = ...) -> None: ...
