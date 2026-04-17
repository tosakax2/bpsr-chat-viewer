import stru_action_info_pb2 as _stru_action_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneActionInfoRequest(_message.Message):
    __slots__ = ("action_info",)
    ACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    action_info: _stru_action_info_pb2.ActionInfo
    def __init__(self, action_info: _Optional[_Union[_stru_action_info_pb2.ActionInfo, _Mapping]] = ...) -> None: ...
