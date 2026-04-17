from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchStrategyNull: _ClassVar[EMatchStrategy]
    EMatchStrategyTeam: _ClassVar[EMatchStrategy]
    EMatchStrategyFreeFrom: _ClassVar[EMatchStrategy]
EMatchStrategyNull: EMatchStrategy
EMatchStrategyTeam: EMatchStrategy
EMatchStrategyFreeFrom: EMatchStrategy
