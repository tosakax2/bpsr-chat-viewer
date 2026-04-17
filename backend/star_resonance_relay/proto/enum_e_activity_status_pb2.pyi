from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EActivityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ActivityStatusNone: _ClassVar[EActivityStatus]
    ActivityStatusOnline: _ClassVar[EActivityStatus]
    ActivityStatusOffline: _ClassVar[EActivityStatus]
ActivityStatusNone: EActivityStatus
ActivityStatusOnline: EActivityStatus
ActivityStatusOffline: EActivityStatus
