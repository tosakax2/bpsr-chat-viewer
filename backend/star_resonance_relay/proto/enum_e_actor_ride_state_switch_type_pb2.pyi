from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EActorRideStateSwitchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ActorRideStateSwitchTypeParallel: _ClassVar[EActorRideStateSwitchType]
    ActorRideStateSwitchTypeSwitch: _ClassVar[EActorRideStateSwitchType]
    ActorRideStateSwitchTypeStopAction: _ClassVar[EActorRideStateSwitchType]
ActorRideStateSwitchTypeParallel: EActorRideStateSwitchType
ActorRideStateSwitchTypeSwitch: EActorRideStateSwitchType
ActorRideStateSwitchTypeStopAction: EActorRideStateSwitchType
