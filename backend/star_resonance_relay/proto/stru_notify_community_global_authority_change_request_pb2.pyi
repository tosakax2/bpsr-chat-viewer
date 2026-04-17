import stru_community_authority_info_pb2 as _stru_community_authority_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityGlobalAuthorityChangeRequest(_message.Message):
    __slots__ = ("authority_info",)
    AUTHORITY_INFO_FIELD_NUMBER: _ClassVar[int]
    authority_info: _stru_community_authority_info_pb2.CommunityAuthorityInfo
    def __init__(self, authority_info: _Optional[_Union[_stru_community_authority_info_pb2.CommunityAuthorityInfo, _Mapping]] = ...) -> None: ...
