from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EToyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECommon: _ClassVar[EToyType]
    EDrawingBoard: _ClassVar[EToyType]
    ESwimmingPool: _ClassVar[EToyType]
ECommon: EToyType
EDrawingBoard: EToyType
ESwimmingPool: EToyType
