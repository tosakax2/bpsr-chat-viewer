import stru_community_player_authority_info_pb2 as _stru_community_player_authority_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunitySetPlayerAuthorityRequest(_message.Message):
    __slots__ = ("char_id", "authority_info")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_INFO_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    authority_info: _stru_community_player_authority_info_pb2.CommunityPlayerAuthorityInfo
    def __init__(self, char_id: _Optional[int] = ..., authority_info: _Optional[_Union[_stru_community_player_authority_info_pb2.CommunityPlayerAuthorityInfo, _Mapping]] = ...) -> None: ...
