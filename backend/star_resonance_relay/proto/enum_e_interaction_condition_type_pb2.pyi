from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EInteractionConditionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    InteractionConditionTypeNull: _ClassVar[EInteractionConditionType]
    InteractionConditionTypeItem: _ClassVar[EInteractionConditionType]
    InteractionConditionTypeEquip: _ClassVar[EInteractionConditionType]
    InteractionConditionTypeQuest: _ClassVar[EInteractionConditionType]
InteractionConditionTypeNull: EInteractionConditionType
InteractionConditionTypeItem: EInteractionConditionType
InteractionConditionTypeEquip: EInteractionConditionType
InteractionConditionTypeQuest: EInteractionConditionType
