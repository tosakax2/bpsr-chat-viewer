import stru_world_activity_param_pb2 as _stru_world_activity_param_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldActivityNtf(_message.Message):
    __slots__ = ()
    class WorldActivityInfoNtf(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _stru_world_activity_param_pb2.WorldActivityParam
        def __init__(self, info: _Optional[_Union[_stru_world_activity_param_pb2.WorldActivityParam, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
