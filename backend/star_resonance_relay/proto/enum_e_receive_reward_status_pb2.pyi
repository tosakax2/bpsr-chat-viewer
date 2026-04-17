from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EReceiveRewardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EReceiveRewardStatusNotReceive: _ClassVar[EReceiveRewardStatus]
    EReceiveRewardStatusCanReceive: _ClassVar[EReceiveRewardStatus]
    EReceiveRewardStatusReceived: _ClassVar[EReceiveRewardStatus]
EReceiveRewardStatusNotReceive: EReceiveRewardStatus
EReceiveRewardStatusCanReceive: EReceiveRewardStatus
EReceiveRewardStatusReceived: EReceiveRewardStatus
