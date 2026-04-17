from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EExchangeItemState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExchangeItemStateNone: _ClassVar[EExchangeItemState]
    ExchangeItemStatePublic: _ClassVar[EExchangeItemState]
ExchangeItemStateNone: EExchangeItemState
ExchangeItemStatePublic: EExchangeItemState
