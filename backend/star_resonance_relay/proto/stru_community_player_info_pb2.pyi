import stru_community_char_basic_data_pb2 as _stru_community_char_basic_data_pb2
import stru_community_player_authority_info_pb2 as _stru_community_player_authority_info_pb2
import stru_community_quit_cohabitant_pb2 as _stru_community_quit_cohabitant_pb2
import stru_home_land_player_task_info_pb2 as _stru_home_land_player_task_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityPlayerInfo(_message.Message):
    __slots__ = ("community_char", "player_authority_info", "quit_cohabitant", "home_land_player_task_info")
    COMMUNITY_CHAR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_AUTHORITY_INFO_FIELD_NUMBER: _ClassVar[int]
    QUIT_COHABITANT_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_PLAYER_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    community_char: _stru_community_char_basic_data_pb2.CommunityCharBasicData
    player_authority_info: _stru_community_player_authority_info_pb2.CommunityPlayerAuthorityInfo
    quit_cohabitant: _stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant
    home_land_player_task_info: _stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo
    def __init__(self, community_char: _Optional[_Union[_stru_community_char_basic_data_pb2.CommunityCharBasicData, _Mapping]] = ..., player_authority_info: _Optional[_Union[_stru_community_player_authority_info_pb2.CommunityPlayerAuthorityInfo, _Mapping]] = ..., quit_cohabitant: _Optional[_Union[_stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant, _Mapping]] = ..., home_land_player_task_info: _Optional[_Union[_stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo, _Mapping]] = ...) -> None: ...
