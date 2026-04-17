from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EUnionActivityRankType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnionActivityRankTypeNull: _ClassVar[EUnionActivityRankType]
    UnionActivityRankTypeScore: _ClassVar[EUnionActivityRankType]
UnionActivityRankTypeNull: EUnionActivityRankType
UnionActivityRankTypeScore: EUnionActivityRankType
