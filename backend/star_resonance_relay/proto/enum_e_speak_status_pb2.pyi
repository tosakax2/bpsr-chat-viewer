from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESpeakStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESpeakStatusDefault: _ClassVar[ESpeakStatus]
    ESpeakStatusBegin: _ClassVar[ESpeakStatus]
    ESpeakStatusEnd: _ClassVar[ESpeakStatus]
ESpeakStatusDefault: ESpeakStatus
ESpeakStatusBegin: ESpeakStatus
ESpeakStatusEnd: ESpeakStatus
