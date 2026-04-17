from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EItemBindFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ItemBindNone: _ClassVar[EItemBindFlag]
    ItemNotBind: _ClassVar[EItemBindFlag]
    ItemBindAll: _ClassVar[EItemBindFlag]
ItemBindNone: EItemBindFlag
ItemNotBind: EItemBindFlag
ItemBindAll: EItemBindFlag
