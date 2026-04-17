import stru_common_target_activity_info_pb2 as _stru_common_target_activity_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonTargetActivity(_message.Message):
    __slots__ = ("common_target_activity_list",)
    class CommonTargetActivityListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_common_target_activity_info_pb2.CommonTargetActivityInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_common_target_activity_info_pb2.CommonTargetActivityInfo, _Mapping]] = ...) -> None: ...
    COMMON_TARGET_ACTIVITY_LIST_FIELD_NUMBER: _ClassVar[int]
    common_target_activity_list: _containers.MessageMap[int, _stru_common_target_activity_info_pb2.CommonTargetActivityInfo]
    def __init__(self, common_target_activity_list: _Optional[_Mapping[int, _stru_common_target_activity_info_pb2.CommonTargetActivityInfo]] = ...) -> None: ...
