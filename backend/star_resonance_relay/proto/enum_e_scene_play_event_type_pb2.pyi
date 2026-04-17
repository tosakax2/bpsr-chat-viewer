from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EScenePlayEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EPlayEventTypeCutScene: _ClassVar[EScenePlayEventType]
    EPlayEventTypeFlow: _ClassVar[EScenePlayEventType]
EPlayEventTypeCutScene: EScenePlayEventType
EPlayEventTypeFlow: EScenePlayEventType
