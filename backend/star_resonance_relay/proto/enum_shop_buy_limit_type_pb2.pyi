from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ShopBuyLimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ShopBuyLimitNone: _ClassVar[ShopBuyLimitType]
    ShopBuyLimitLevel: _ClassVar[ShopBuyLimitType]
ShopBuyLimitNone: ShopBuyLimitType
ShopBuyLimitLevel: ShopBuyLimitType
