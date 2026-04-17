from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteActionGroupDataRequest(_message.Message):
    __slots__ = ("action_group_id",)
    ACTION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    action_group_id: int
    def __init__(self, action_group_id: _Optional[int] = ...) -> None: ...
