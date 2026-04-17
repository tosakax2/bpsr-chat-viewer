from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InteractionInfo(_message.Message):
    __slots__ = ("interaction_stage", "action_id", "originator_id", "invitee_id", "is_originator", "interaction_type")
    INTERACTION_STAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATOR_ID_FIELD_NUMBER: _ClassVar[int]
    INVITEE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    interaction_stage: int
    action_id: int
    originator_id: int
    invitee_id: int
    is_originator: bool
    interaction_type: int
    def __init__(self, interaction_stage: _Optional[int] = ..., action_id: _Optional[int] = ..., originator_id: _Optional[int] = ..., invitee_id: _Optional[int] = ..., is_originator: bool = ..., interaction_type: _Optional[int] = ...) -> None: ...
