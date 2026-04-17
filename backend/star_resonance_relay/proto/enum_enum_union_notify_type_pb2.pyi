from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumUnionNotifyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnionNotifyDefault: _ClassVar[EnumUnionNotifyType]
    UnionNotifyJoin: _ClassVar[EnumUnionNotifyType]
    UnionNotifyLeave: _ClassVar[EnumUnionNotifyType]
    UnionNotifyMemUpdate: _ClassVar[EnumUnionNotifyType]
UnionNotifyDefault: EnumUnionNotifyType
UnionNotifyJoin: EnumUnionNotifyType
UnionNotifyLeave: EnumUnionNotifyType
UnionNotifyMemUpdate: EnumUnionNotifyType
