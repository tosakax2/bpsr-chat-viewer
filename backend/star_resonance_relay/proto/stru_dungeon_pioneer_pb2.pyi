import stru_completed_target_info_pb2 as _stru_completed_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonPioneer(_message.Message):
    __slots__ = ("completed_target_this_time",)
    class CompletedTargetThisTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_completed_target_info_pb2.CompletedTargetInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_completed_target_info_pb2.CompletedTargetInfo, _Mapping]] = ...) -> None: ...
    COMPLETED_TARGET_THIS_TIME_FIELD_NUMBER: _ClassVar[int]
    completed_target_this_time: _containers.MessageMap[int, _stru_completed_target_info_pb2.CompletedTargetInfo]
    def __init__(self, completed_target_this_time: _Optional[_Mapping[int, _stru_completed_target_info_pb2.CompletedTargetInfo]] = ...) -> None: ...
