from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EUserState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECreateState: _ClassVar[EUserState]
    ENameState: _ClassVar[EUserState]
ECreateState: EUserState
ENameState: EUserState
