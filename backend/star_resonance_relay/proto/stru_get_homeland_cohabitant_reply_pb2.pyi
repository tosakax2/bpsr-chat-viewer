import stru_community_player_info_pb2 as _stru_community_player_info_pb2
import stru_community_transfer_pb2 as _stru_community_transfer_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandCohabitantReply(_message.Message):
    __slots__ = ("transfer_community", "cohabitant", "err_code")
    class CohabitantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_player_info_pb2.CommunityPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_player_info_pb2.CommunityPlayerInfo, _Mapping]] = ...) -> None: ...
    TRANSFER_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    COHABITANT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    transfer_community: _stru_community_transfer_pb2.CommunityTransfer
    cohabitant: _containers.MessageMap[int, _stru_community_player_info_pb2.CommunityPlayerInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, transfer_community: _Optional[_Union[_stru_community_transfer_pb2.CommunityTransfer, _Mapping]] = ..., cohabitant: _Optional[_Mapping[int, _stru_community_player_info_pb2.CommunityPlayerInfo]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
