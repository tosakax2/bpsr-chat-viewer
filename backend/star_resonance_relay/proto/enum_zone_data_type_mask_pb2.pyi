from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneDataTypeMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZoneDataTypeMaskDef: _ClassVar[ZoneDataTypeMask]
    ClientNotifyServerMask: _ClassVar[ZoneDataTypeMask]
    AreaWallMask: _ClassVar[ZoneDataTypeMask]
    EnterableMask: _ClassVar[ZoneDataTypeMask]
    ExitableMask: _ClassVar[ZoneDataTypeMask]
    ClientTriggerMask: _ClassVar[ZoneDataTypeMask]
    CameraBlockMask: _ClassVar[ZoneDataTypeMask]
    OnlyServerTriggerMask: _ClassVar[ZoneDataTypeMask]
    DontShowAreaWallEffectMask: _ClassVar[ZoneDataTypeMask]
    HomeSoftAreaWall: _ClassVar[ZoneDataTypeMask]
    Empty4Mask: _ClassVar[ZoneDataTypeMask]
    NavMask: _ClassVar[ZoneDataTypeMask]
ZoneDataTypeMaskDef: ZoneDataTypeMask
ClientNotifyServerMask: ZoneDataTypeMask
AreaWallMask: ZoneDataTypeMask
EnterableMask: ZoneDataTypeMask
ExitableMask: ZoneDataTypeMask
ClientTriggerMask: ZoneDataTypeMask
CameraBlockMask: ZoneDataTypeMask
OnlyServerTriggerMask: ZoneDataTypeMask
DontShowAreaWallEffectMask: ZoneDataTypeMask
HomeSoftAreaWall: ZoneDataTypeMask
Empty4Mask: ZoneDataTypeMask
NavMask: ZoneDataTypeMask
