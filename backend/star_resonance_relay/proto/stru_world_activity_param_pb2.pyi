import stru_activity_pb2 as _stru_activity_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldActivityParam(_message.Message):
    __slots__ = ("activity",)
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    activity: _stru_activity_pb2.Activity
    def __init__(self, activity: _Optional[_Union[_stru_activity_pb2.Activity, _Mapping]] = ...) -> None: ...
