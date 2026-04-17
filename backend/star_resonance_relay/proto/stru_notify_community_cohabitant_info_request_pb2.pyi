import stru_community_player_info_pb2 as _stru_community_player_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityCohabitantInfoRequest(_message.Message):
    __slots__ = ("community_id", "homeland_id", "cohabitant", "owner_char_id", "remove_char_id")
    class CohabitantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_player_info_pb2.CommunityPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_player_info_pb2.CommunityPlayerInfo, _Mapping]] = ...) -> None: ...
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    COHABITANT_FIELD_NUMBER: _ClassVar[int]
    OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    cohabitant: _containers.MessageMap[int, _stru_community_player_info_pb2.CommunityPlayerInfo]
    owner_char_id: int
    remove_char_id: int
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., cohabitant: _Optional[_Mapping[int, _stru_community_player_info_pb2.CommunityPlayerInfo]] = ..., owner_char_id: _Optional[int] = ..., remove_char_id: _Optional[int] = ...) -> None: ...
