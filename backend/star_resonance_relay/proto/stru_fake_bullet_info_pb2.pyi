import stru_vec3_pb2 as _stru_vec3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FakeBulletInfo(_message.Message):
    __slots__ = ("Uuid", "BulletId", "TargetId", "PartId", "Offset", "Rotate", "SkinId")
    UUID_FIELD_NUMBER: _ClassVar[int]
    BULLETID_FIELD_NUMBER: _ClassVar[int]
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    BulletId: int
    TargetId: int
    PartId: int
    Offset: _stru_vec3_pb2.Vec3
    Rotate: _stru_vec3_pb2.Vec3
    SkinId: int
    def __init__(self, Uuid: _Optional[int] = ..., BulletId: _Optional[int] = ..., TargetId: _Optional[int] = ..., PartId: _Optional[int] = ..., Offset: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ..., Rotate: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ..., SkinId: _Optional[int] = ...) -> None: ...
