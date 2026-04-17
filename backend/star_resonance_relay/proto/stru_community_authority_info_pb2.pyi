import stru_community_single_authority_info_pb2 as _stru_community_single_authority_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityAuthorityInfo(_message.Message):
    __slots__ = ("authority", "authority_data")
    class AuthorityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class AuthorityDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_single_authority_info_pb2.CommunitySingleAuthorityInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_single_authority_info_pb2.CommunitySingleAuthorityInfo, _Mapping]] = ...) -> None: ...
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_DATA_FIELD_NUMBER: _ClassVar[int]
    authority: _containers.ScalarMap[int, bool]
    authority_data: _containers.MessageMap[int, _stru_community_single_authority_info_pb2.CommunitySingleAuthorityInfo]
    def __init__(self, authority: _Optional[_Mapping[int, bool]] = ..., authority_data: _Optional[_Mapping[int, _stru_community_single_authority_info_pb2.CommunitySingleAuthorityInfo]] = ...) -> None: ...
