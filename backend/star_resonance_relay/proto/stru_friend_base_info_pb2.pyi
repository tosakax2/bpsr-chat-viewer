import stru_application_info_pb2 as _stru_application_info_pb2
import stru_social_info_pb2 as _stru_social_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendBaseInfo(_message.Message):
    __slots__ = ("friend_list", "group_id_list", "application_list", "group_sort")
    class FriendListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_social_info_pb2.SocialInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_social_info_pb2.SocialInfo, _Mapping]] = ...) -> None: ...
    class GroupIdListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_SORT_FIELD_NUMBER: _ClassVar[int]
    friend_list: _containers.MessageMap[int, _stru_social_info_pb2.SocialInfo]
    group_id_list: _containers.ScalarMap[int, str]
    application_list: _containers.RepeatedCompositeFieldContainer[_stru_application_info_pb2.ApplicationInfo]
    group_sort: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, friend_list: _Optional[_Mapping[int, _stru_social_info_pb2.SocialInfo]] = ..., group_id_list: _Optional[_Mapping[int, str]] = ..., application_list: _Optional[_Iterable[_Union[_stru_application_info_pb2.ApplicationInfo, _Mapping]]] = ..., group_sort: _Optional[_Iterable[int]] = ...) -> None: ...
