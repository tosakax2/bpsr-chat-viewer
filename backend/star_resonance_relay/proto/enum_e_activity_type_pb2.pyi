from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EActivityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ActivityTypeNone: _ClassVar[EActivityType]
    ActivityTypeBuyGift: _ClassVar[EActivityType]
ActivityTypeNone: EActivityType
ActivityTypeBuyGift: EActivityType
