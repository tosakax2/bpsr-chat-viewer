from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EQueryBalanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EQueryBalanceTypeNull: _ClassVar[EQueryBalanceType]
    EQueryBalanceTypeLeft: _ClassVar[EQueryBalanceType]
    EQueryBalanceTypeMonthCard: _ClassVar[EQueryBalanceType]
EQueryBalanceTypeNull: EQueryBalanceType
EQueryBalanceTypeLeft: EQueryBalanceType
EQueryBalanceTypeMonthCard: EQueryBalanceType
