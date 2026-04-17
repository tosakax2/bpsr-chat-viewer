from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerStateObjectInteractionParam(_message.Message):
    __slots__ = ("obj_uuid", "state_value", "last_interaction_time")
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    STATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LAST_INTERACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    obj_uuid: int
    state_value: int
    last_interaction_time: int
    def __init__(self, obj_uuid: _Optional[int] = ..., state_value: _Optional[int] = ..., last_interaction_time: _Optional[int] = ...) -> None: ...
