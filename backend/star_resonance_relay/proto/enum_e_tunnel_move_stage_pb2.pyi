from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETunnelMoveStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EEnter: _ClassVar[ETunnelMoveStage]
    EFly: _ClassVar[ETunnelMoveStage]
    EExit: _ClassVar[ETunnelMoveStage]
EEnter: ETunnelMoveStage
EFly: ETunnelMoveStage
EExit: ETunnelMoveStage
