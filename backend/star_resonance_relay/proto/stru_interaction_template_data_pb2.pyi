import enum_e_interaction_template_action_pb2 as _enum_e_interaction_template_action_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InteractionTemplateData(_message.Message):
    __slots__ = ("type", "object_id", "template_id", "homeland_id", "pos_id", "sub_template_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    POS_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_interaction_template_action_pb2.EInteractionTemplateAction
    object_id: int
    template_id: int
    homeland_id: int
    pos_id: int
    sub_template_id: int
    def __init__(self, type: _Optional[_Union[_enum_e_interaction_template_action_pb2.EInteractionTemplateAction, str]] = ..., object_id: _Optional[int] = ..., template_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., pos_id: _Optional[int] = ..., sub_template_id: _Optional[int] = ...) -> None: ...
