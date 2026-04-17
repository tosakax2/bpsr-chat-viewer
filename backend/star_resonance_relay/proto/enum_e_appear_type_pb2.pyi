from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EAppearType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EAppearNull: _ClassVar[EAppearType]
    EAppearTransferIn: _ClassVar[EAppearType]
    EAppearTransferPassLineIn: _ClassVar[EAppearType]
EAppearNull: EAppearType
EAppearTransferIn: EAppearType
EAppearTransferPassLineIn: EAppearType
