import stru_community_bulletin_board_pb2 as _stru_community_bulletin_board_pb2
import stru_community_invitation_info_pb2 as _stru_community_invitation_info_pb2
import stru_community_player_info_pb2 as _stru_community_player_info_pb2
import stru_community_quit_cohabitant_pb2 as _stru_community_quit_cohabitant_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityInfoUpdateRequest(_message.Message):
    __slots__ = ("house_owner_char_id", "homeland_id", "remove_groups", "add_bulletin_boards", "remove_bulletin_boards", "add_cohabitant", "remove_cohabitant", "add_invitation_list", "remove_invitation_list", "add_quit_cohabitant", "remove_quit_cohabitant")
    class AddBulletinBoardsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_bulletin_board_pb2.CommunityBulletinBoard
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_bulletin_board_pb2.CommunityBulletinBoard, _Mapping]] = ...) -> None: ...
    class AddCohabitantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_player_info_pb2.CommunityPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_player_info_pb2.CommunityPlayerInfo, _Mapping]] = ...) -> None: ...
    class AddInvitationListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_invitation_info_pb2.CommunityInvitationInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_invitation_info_pb2.CommunityInvitationInfo, _Mapping]] = ...) -> None: ...
    HOUSE_OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ADD_BULLETIN_BOARDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_BULLETIN_BOARDS_FIELD_NUMBER: _ClassVar[int]
    ADD_COHABITANT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_COHABITANT_FIELD_NUMBER: _ClassVar[int]
    ADD_INVITATION_LIST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_INVITATION_LIST_FIELD_NUMBER: _ClassVar[int]
    ADD_QUIT_COHABITANT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_QUIT_COHABITANT_FIELD_NUMBER: _ClassVar[int]
    house_owner_char_id: int
    homeland_id: int
    remove_groups: _containers.RepeatedScalarFieldContainer[int]
    add_bulletin_boards: _containers.MessageMap[int, _stru_community_bulletin_board_pb2.CommunityBulletinBoard]
    remove_bulletin_boards: _containers.RepeatedScalarFieldContainer[int]
    add_cohabitant: _containers.MessageMap[int, _stru_community_player_info_pb2.CommunityPlayerInfo]
    remove_cohabitant: _containers.RepeatedScalarFieldContainer[int]
    add_invitation_list: _containers.MessageMap[int, _stru_community_invitation_info_pb2.CommunityInvitationInfo]
    remove_invitation_list: _containers.RepeatedScalarFieldContainer[int]
    add_quit_cohabitant: _containers.RepeatedCompositeFieldContainer[_stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant]
    remove_quit_cohabitant: _containers.RepeatedCompositeFieldContainer[_stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant]
    def __init__(self, house_owner_char_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., remove_groups: _Optional[_Iterable[int]] = ..., add_bulletin_boards: _Optional[_Mapping[int, _stru_community_bulletin_board_pb2.CommunityBulletinBoard]] = ..., remove_bulletin_boards: _Optional[_Iterable[int]] = ..., add_cohabitant: _Optional[_Mapping[int, _stru_community_player_info_pb2.CommunityPlayerInfo]] = ..., remove_cohabitant: _Optional[_Iterable[int]] = ..., add_invitation_list: _Optional[_Mapping[int, _stru_community_invitation_info_pb2.CommunityInvitationInfo]] = ..., remove_invitation_list: _Optional[_Iterable[int]] = ..., add_quit_cohabitant: _Optional[_Iterable[_Union[_stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant, _Mapping]]] = ..., remove_quit_cohabitant: _Optional[_Iterable[_Union[_stru_community_quit_cohabitant_pb2.CommunityQuitCohabitant, _Mapping]]] = ...) -> None: ...
