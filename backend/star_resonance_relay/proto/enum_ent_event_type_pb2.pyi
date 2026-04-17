from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EntEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HudChat: _ClassVar[EntEventType]
    PlayAnim: _ClassVar[EntEventType]
    PlayAudio: _ClassVar[EntEventType]
    EventPlayEffect: _ClassVar[EntEventType]
HudChat: EntEventType
PlayAnim: EntEventType
PlayAudio: EntEventType
EventPlayEffect: EntEventType
