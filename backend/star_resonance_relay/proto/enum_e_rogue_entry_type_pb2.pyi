from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERogueEntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERogueEntryTypeNone: _ClassVar[ERogueEntryType]
    ERogueEntryTypeRandom: _ClassVar[ERogueEntryType]
    ERogueEntryTypeBase: _ClassVar[ERogueEntryType]
    ERogueEntryTypeSkill: _ClassVar[ERogueEntryType]
ERogueEntryTypeNone: ERogueEntryType
ERogueEntryTypeRandom: ERogueEntryType
ERogueEntryTypeBase: ERogueEntryType
ERogueEntryTypeSkill: ERogueEntryType
