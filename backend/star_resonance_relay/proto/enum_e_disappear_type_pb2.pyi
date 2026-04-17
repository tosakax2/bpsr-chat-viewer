from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDisappearType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDisappearNormal: _ClassVar[EDisappearType]
    EDisappearDead: _ClassVar[EDisappearType]
    EDisappearDestroy: _ClassVar[EDisappearType]
    EDisappearTransferLeave: _ClassVar[EDisappearType]
    EDisappearTransferPassLineLeave: _ClassVar[EDisappearType]
EDisappearNormal: EDisappearType
EDisappearDead: EDisappearType
EDisappearDestroy: EDisappearType
EDisappearTransferLeave: EDisappearType
EDisappearTransferPassLineLeave: EDisappearType
