import stru_exchange_filter_pb2 as _stru_exchange_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeNoticeDetailRequest(_message.Message):
    __slots__ = ("config_id", "filter", "page")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    filter: _containers.RepeatedCompositeFieldContainer[_stru_exchange_filter_pb2.ExchangeFilter]
    page: int
    def __init__(self, config_id: _Optional[int] = ..., filter: _Optional[_Iterable[_Union[_stru_exchange_filter_pb2.ExchangeFilter, _Mapping]]] = ..., page: _Optional[int] = ...) -> None: ...
