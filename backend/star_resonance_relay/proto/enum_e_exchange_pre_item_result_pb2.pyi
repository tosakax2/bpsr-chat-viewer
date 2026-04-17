from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EExchangePreItemResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExchangePreItemResultNone: _ClassVar[EExchangePreItemResult]
    ExchangePreItemResultSuccess: _ClassVar[EExchangePreItemResult]
    ExchangePreItemResultFail: _ClassVar[EExchangePreItemResult]
ExchangePreItemResultNone: EExchangePreItemResult
ExchangePreItemResultSuccess: EExchangePreItemResult
ExchangePreItemResultFail: EExchangePreItemResult
