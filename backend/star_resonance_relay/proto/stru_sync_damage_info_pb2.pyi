import enum_e_damage_source_pb2 as _enum_e_damage_source_pb2
import enum_e_damage_type_pb2 as _enum_e_damage_type_pb2
import enum_e_damage_property_pb2 as _enum_e_damage_property_pb2
import enum_e_damage_mode_pb2 as _enum_e_damage_mode_pb2
import stru_vec3_pb2 as _stru_vec3_pb2
import stru_vec2_pb2 as _stru_vec2_pb2
import stru_client_hit_part_info_pb2 as _stru_client_hit_part_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncDamageInfo(_message.Message):
    __slots__ = ("DamageSource", "IsMiss", "IsCrit", "Type", "TypeFlag", "Value", "ActualValue", "LuckyValue", "HpLessenValue", "ShieldLessenValue", "AttackerUuid", "OwnerId", "OwnerLevel", "OwnerStage", "HitEventId", "IsNormal", "IsDead", "Property", "DamagePos", "PartInfos", "TopSummonerId", "DamageWeight", "PassiveUuid", "IsRainbow", "DamageMode")
    DAMAGESOURCE_FIELD_NUMBER: _ClassVar[int]
    ISMISS_FIELD_NUMBER: _ClassVar[int]
    ISCRIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPEFLAG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUALVALUE_FIELD_NUMBER: _ClassVar[int]
    LUCKYVALUE_FIELD_NUMBER: _ClassVar[int]
    HPLESSENVALUE_FIELD_NUMBER: _ClassVar[int]
    SHIELDLESSENVALUE_FIELD_NUMBER: _ClassVar[int]
    ATTACKERUUID_FIELD_NUMBER: _ClassVar[int]
    OWNERID_FIELD_NUMBER: _ClassVar[int]
    OWNERLEVEL_FIELD_NUMBER: _ClassVar[int]
    OWNERSTAGE_FIELD_NUMBER: _ClassVar[int]
    HITEVENTID_FIELD_NUMBER: _ClassVar[int]
    ISNORMAL_FIELD_NUMBER: _ClassVar[int]
    ISDEAD_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DAMAGEPOS_FIELD_NUMBER: _ClassVar[int]
    PARTINFOS_FIELD_NUMBER: _ClassVar[int]
    TOPSUMMONERID_FIELD_NUMBER: _ClassVar[int]
    DAMAGEWEIGHT_FIELD_NUMBER: _ClassVar[int]
    PASSIVEUUID_FIELD_NUMBER: _ClassVar[int]
    ISRAINBOW_FIELD_NUMBER: _ClassVar[int]
    DAMAGEMODE_FIELD_NUMBER: _ClassVar[int]
    DamageSource: _enum_e_damage_source_pb2.EDamageSource
    IsMiss: bool
    IsCrit: bool
    Type: _enum_e_damage_type_pb2.EDamageType
    TypeFlag: int
    Value: int
    ActualValue: int
    LuckyValue: int
    HpLessenValue: int
    ShieldLessenValue: int
    AttackerUuid: int
    OwnerId: int
    OwnerLevel: int
    OwnerStage: int
    HitEventId: int
    IsNormal: bool
    IsDead: bool
    Property: _enum_e_damage_property_pb2.EDamageProperty
    DamagePos: _stru_vec3_pb2.Vec3
    PartInfos: _containers.RepeatedCompositeFieldContainer[_stru_client_hit_part_info_pb2.ClientHitPartInfo]
    TopSummonerId: int
    DamageWeight: _stru_vec2_pb2.Vec2
    PassiveUuid: int
    IsRainbow: bool
    DamageMode: _enum_e_damage_mode_pb2.EDamageMode
    def __init__(self, DamageSource: _Optional[_Union[_enum_e_damage_source_pb2.EDamageSource, str]] = ..., IsMiss: bool = ..., IsCrit: bool = ..., Type: _Optional[_Union[_enum_e_damage_type_pb2.EDamageType, str]] = ..., TypeFlag: _Optional[int] = ..., Value: _Optional[int] = ..., ActualValue: _Optional[int] = ..., LuckyValue: _Optional[int] = ..., HpLessenValue: _Optional[int] = ..., ShieldLessenValue: _Optional[int] = ..., AttackerUuid: _Optional[int] = ..., OwnerId: _Optional[int] = ..., OwnerLevel: _Optional[int] = ..., OwnerStage: _Optional[int] = ..., HitEventId: _Optional[int] = ..., IsNormal: bool = ..., IsDead: bool = ..., Property: _Optional[_Union[_enum_e_damage_property_pb2.EDamageProperty, str]] = ..., DamagePos: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ..., PartInfos: _Optional[_Iterable[_Union[_stru_client_hit_part_info_pb2.ClientHitPartInfo, _Mapping]]] = ..., TopSummonerId: _Optional[int] = ..., DamageWeight: _Optional[_Union[_stru_vec2_pb2.Vec2, _Mapping]] = ..., PassiveUuid: _Optional[int] = ..., IsRainbow: bool = ..., DamageMode: _Optional[_Union[_enum_e_damage_mode_pb2.EDamageMode, str]] = ...) -> None: ...
