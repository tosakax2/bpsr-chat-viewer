from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EInteractionTemplateAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EInteractionTemplateDefault: _ClassVar[EInteractionTemplateAction]
    EInteractionTemplateBegin: _ClassVar[EInteractionTemplateAction]
    EInteractionTemplateUpdate: _ClassVar[EInteractionTemplateAction]
    EInteractionTemplateEnd: _ClassVar[EInteractionTemplateAction]
    EInteractionTemplateAbort: _ClassVar[EInteractionTemplateAction]
    EInteractionTemplateStageEnd: _ClassVar[EInteractionTemplateAction]
EInteractionTemplateDefault: EInteractionTemplateAction
EInteractionTemplateBegin: EInteractionTemplateAction
EInteractionTemplateUpdate: EInteractionTemplateAction
EInteractionTemplateEnd: EInteractionTemplateAction
EInteractionTemplateAbort: EInteractionTemplateAction
EInteractionTemplateStageEnd: EInteractionTemplateAction
