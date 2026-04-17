from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECompareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENone: _ClassVar[ECompareType]
    EEqual: _ClassVar[ECompareType]
    EUnequal: _ClassVar[ECompareType]
    EGreater: _ClassVar[ECompareType]
    EGreaterAndEqual: _ClassVar[ECompareType]
    ELess: _ClassVar[ECompareType]
    ELessAndEqual: _ClassVar[ECompareType]
ENone: ECompareType
EEqual: ECompareType
EUnequal: ECompareType
EGreater: ECompareType
EGreaterAndEqual: ECompareType
ELess: ECompareType
ELessAndEqual: ECompareType
