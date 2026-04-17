from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPersonalizationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EStatusDefault: _ClassVar[EPersonalizationStatus]
    EStatusOnline: _ClassVar[EPersonalizationStatus]
    EStatusDungeon: _ClassVar[EPersonalizationStatus]
    EStatusCutScene: _ClassVar[EPersonalizationStatus]
    EStatusPhoto: _ClassVar[EPersonalizationStatus]
    EStatusRecruit: _ClassVar[EPersonalizationStatus]
EStatusDefault: EPersonalizationStatus
EStatusOnline: EPersonalizationStatus
EStatusDungeon: EPersonalizationStatus
EStatusCutScene: EPersonalizationStatus
EStatusPhoto: EPersonalizationStatus
EStatusRecruit: EPersonalizationStatus
