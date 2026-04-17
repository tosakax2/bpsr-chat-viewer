from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BodyPartState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BodyPartStateDefault: _ClassVar[BodyPartState]
    BodyPartStateInjury: _ClassVar[BodyPartState]
    BodyPartStateDead: _ClassVar[BodyPartState]
BodyPartStateDefault: BodyPartState
BodyPartStateInjury: BodyPartState
BodyPartStateDead: BodyPartState
