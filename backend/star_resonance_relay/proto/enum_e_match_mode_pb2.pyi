from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchModeSingle: _ClassVar[EMatchMode]
    EMatchModeTeam: _ClassVar[EMatchMode]
EMatchModeSingle: EMatchMode
EMatchModeTeam: EMatchMode
