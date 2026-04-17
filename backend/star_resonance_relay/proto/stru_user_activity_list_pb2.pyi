import stru_user_activity_info_pb2 as _stru_user_activity_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserActivityList(_message.Message):
    __slots__ = ("activities",)
    class ActivitiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_user_activity_info_pb2.UserActivityInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_user_activity_info_pb2.UserActivityInfo, _Mapping]] = ...) -> None: ...
    ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    activities: _containers.MessageMap[int, _stru_user_activity_info_pb2.UserActivityInfo]
    def __init__(self, activities: _Optional[_Mapping[int, _stru_user_activity_info_pb2.UserActivityInfo]] = ...) -> None: ...
