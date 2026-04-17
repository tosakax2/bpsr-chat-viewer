import stru_vec3_pb2 as _stru_vec3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientHitPartInfo(_message.Message):
    __slots__ = ("PartId", "DamagePos", "DamageVal")
    PARTID_FIELD_NUMBER: _ClassVar[int]
    DAMAGEPOS_FIELD_NUMBER: _ClassVar[int]
    DAMAGEVAL_FIELD_NUMBER: _ClassVar[int]
    PartId: int
    DamagePos: _stru_vec3_pb2.Vec3
    DamageVal: int
    def __init__(self, PartId: _Optional[int] = ..., DamagePos: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ..., DamageVal: _Optional[int] = ...) -> None: ...
