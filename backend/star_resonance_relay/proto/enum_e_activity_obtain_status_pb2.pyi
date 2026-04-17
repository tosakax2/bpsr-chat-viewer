from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EActivityObtainStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ActivityObtainStatusNone: _ClassVar[EActivityObtainStatus]
    ActivityObtainStatusCan: _ClassVar[EActivityObtainStatus]
    ActivityObtainStatusAlready: _ClassVar[EActivityObtainStatus]
ActivityObtainStatusNone: EActivityObtainStatus
ActivityObtainStatusCan: EActivityObtainStatus
ActivityObtainStatusAlready: EActivityObtainStatus
