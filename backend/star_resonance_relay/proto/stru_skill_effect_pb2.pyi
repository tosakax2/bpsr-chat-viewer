import stru_sync_damage_info_pb2 as _stru_sync_damage_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillEffect(_message.Message):
    __slots__ = ("Uuid", "Damages", "TotalDamage")
    UUID_FIELD_NUMBER: _ClassVar[int]
    DAMAGES_FIELD_NUMBER: _ClassVar[int]
    TOTALDAMAGE_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    Damages: _containers.RepeatedCompositeFieldContainer[_stru_sync_damage_info_pb2.SyncDamageInfo]
    TotalDamage: int
    def __init__(self, Uuid: _Optional[int] = ..., Damages: _Optional[_Iterable[_Union[_stru_sync_damage_info_pb2.SyncDamageInfo, _Mapping]]] = ..., TotalDamage: _Optional[int] = ...) -> None: ...
