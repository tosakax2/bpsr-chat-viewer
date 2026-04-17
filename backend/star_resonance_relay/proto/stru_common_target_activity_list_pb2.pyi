import stru_common_target_activity_pb2 as _stru_common_target_activity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonTargetActivityList(_message.Message):
    __slots__ = ("common_target_activity_map", "version")
    class CommonTargetActivityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_common_target_activity_pb2.CommonTargetActivity
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_common_target_activity_pb2.CommonTargetActivity, _Mapping]] = ...) -> None: ...
    COMMON_TARGET_ACTIVITY_MAP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    common_target_activity_map: _containers.MessageMap[int, _stru_common_target_activity_pb2.CommonTargetActivity]
    version: int
    def __init__(self, common_target_activity_map: _Optional[_Mapping[int, _stru_common_target_activity_pb2.CommonTargetActivity]] = ..., version: _Optional[int] = ...) -> None: ...
