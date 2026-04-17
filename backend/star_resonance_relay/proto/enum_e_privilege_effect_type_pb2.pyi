from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPrivilegeEffectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EPrivilegeEffectTypeNone: _ClassVar[EPrivilegeEffectType]
    EPrivilegeEffectTypeItemDropBonus: _ClassVar[EPrivilegeEffectType]
    EPrivilegeEffectTypeDailyActivityBonus: _ClassVar[EPrivilegeEffectType]
    EPrivilegeEffectTypeBattlePassLevAdd: _ClassVar[EPrivilegeEffectType]
    EPrivilegeEffectTypeShopRefreshTimesBonus: _ClassVar[EPrivilegeEffectType]
EPrivilegeEffectTypeNone: EPrivilegeEffectType
EPrivilegeEffectTypeItemDropBonus: EPrivilegeEffectType
EPrivilegeEffectTypeDailyActivityBonus: EPrivilegeEffectType
EPrivilegeEffectTypeBattlePassLevAdd: EPrivilegeEffectType
EPrivilegeEffectTypeShopRefreshTimesBonus: EPrivilegeEffectType
