from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EExchangeItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExchangeItemTypeNone: _ClassVar[EExchangeItemType]
    ExchangeItemTypeShopItem: _ClassVar[EExchangeItemType]
    ExchangeItemTypeNoticeShopItem: _ClassVar[EExchangeItemType]
ExchangeItemTypeNone: EExchangeItemType
ExchangeItemTypeShopItem: EExchangeItemType
ExchangeItemTypeNoticeShopItem: EExchangeItemType
