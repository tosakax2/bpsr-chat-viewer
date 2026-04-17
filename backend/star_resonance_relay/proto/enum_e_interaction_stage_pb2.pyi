from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EInteractionStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EStageDefault: _ClassVar[EInteractionStage]
    EStageRequest: _ClassVar[EInteractionStage]
    EStageResponse: _ClassVar[EInteractionStage]
    EStageInteracting: _ClassVar[EInteractionStage]
EStageDefault: EInteractionStage
EStageRequest: EInteractionStage
EStageResponse: EInteractionStage
EStageInteracting: EInteractionStage
