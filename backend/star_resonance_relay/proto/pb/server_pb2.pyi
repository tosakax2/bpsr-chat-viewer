from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CHAT_SERVER_CMD(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_SERVER_CMD_INVALID: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_REGISTER_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_REGISTER_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CLIENT_TOKEN_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CLIENT_TOKEN_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CREATE_CHANNEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CREATE_CHANNEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_JOIN_CHANNEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_JOIN_CHANNEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_OUT_CHANNEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_OUT_CHANNEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CHANNEL_MEMBER_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CHANNEL_MEMBER_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_CHANNEL_MEMBER_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_CHANNEL_MEMBER_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_ADD_BLACKLIST_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_ADD_BLACKLIST_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_REMOVE_BLACKLIST_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_REMOVE_BLACKLIST_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_BLACKLIST_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_BLACKLIST_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_BLACKLIST_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_BLACKLIST_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_BAN_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_BAN_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_GROUP_BAN_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_GROUP_BAN_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_PERSONAL_BAN_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_PERSONAL_BAN_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_PERSONAL_BAN_INFO_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_PERSONAL_BAN_INFO_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_PERSONAL_CHANNEL_LEVEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_PERSONAL_CHANNEL_LEVEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_UPDATE_PERSONAL_CHANNEL_LEVEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_UPDATE_PERSONAL_CHANNEL_LEVEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_USER_CHANNEL_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYNC_USER_CHANNEL_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_PRIVATE_CHAT_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_PRIVATE_CHAT_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_CHANNEL_CHAT_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_CHANNEL_CHAT_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_WORLD_CHAT_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_SYSTEM_WORLD_CHAT_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CREATE_CHANNEL_GROUP_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CREATE_CHANNEL_GROUP_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_GROUP_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_GROUP_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CHANNEL_GROUP_INFO_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_GET_CHANNEL_GROUP_INFO_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_GROUP_SWITCH_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CHANNEL_GROUP_SWITCH_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_PRIVATE_CHAT_RECORD_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_PRIVATE_CHAT_RECORD_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_CHAT_RECORD_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_CHANNEL_CHAT_RECORD_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_WORLD_CHAT_RECORD_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_DEL_WORLD_CHAT_RECORD_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CLEAR_USER_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CLEAR_USER_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_USERID_REGISTER_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_USERID_REGISTER_RSP: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CROSS_PRIVATE_CHAT_REQ: _ClassVar[CHAT_SERVER_CMD]
    CHAT_SERVER_CROSS_PRIVATE_CHAT_RSP: _ClassVar[CHAT_SERVER_CMD]
CHAT_SERVER_CMD_INVALID: CHAT_SERVER_CMD
CHAT_SERVER_REGISTER_REQ: CHAT_SERVER_CMD
CHAT_SERVER_REGISTER_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_CLIENT_TOKEN_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_CLIENT_TOKEN_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CREATE_CHANNEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CREATE_CHANNEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_JOIN_CHANNEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_JOIN_CHANNEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_OUT_CHANNEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_OUT_CHANNEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_CHANNEL_MEMBER_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_CHANNEL_MEMBER_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_CHANNEL_MEMBER_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_CHANNEL_MEMBER_RSP: CHAT_SERVER_CMD
CHAT_SERVER_ADD_BLACKLIST_REQ: CHAT_SERVER_CMD
CHAT_SERVER_ADD_BLACKLIST_RSP: CHAT_SERVER_CMD
CHAT_SERVER_REMOVE_BLACKLIST_REQ: CHAT_SERVER_CMD
CHAT_SERVER_REMOVE_BLACKLIST_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_BLACKLIST_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_BLACKLIST_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_BLACKLIST_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_BLACKLIST_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_BAN_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_BAN_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_GROUP_BAN_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_GROUP_BAN_RSP: CHAT_SERVER_CMD
CHAT_SERVER_PERSONAL_BAN_REQ: CHAT_SERVER_CMD
CHAT_SERVER_PERSONAL_BAN_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_PERSONAL_BAN_INFO_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_PERSONAL_BAN_INFO_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_PERSONAL_CHANNEL_LEVEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_PERSONAL_CHANNEL_LEVEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_UPDATE_PERSONAL_CHANNEL_LEVEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_UPDATE_PERSONAL_CHANNEL_LEVEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_USER_CHANNEL_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYNC_USER_CHANNEL_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_PRIVATE_CHAT_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_PRIVATE_CHAT_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_CHANNEL_CHAT_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_CHANNEL_CHAT_RSP: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_WORLD_CHAT_REQ: CHAT_SERVER_CMD
CHAT_SERVER_SYSTEM_WORLD_CHAT_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CREATE_CHANNEL_GROUP_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CREATE_CHANNEL_GROUP_RSP: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_GROUP_REQ: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_GROUP_RSP: CHAT_SERVER_CMD
CHAT_SERVER_GET_CHANNEL_GROUP_INFO_REQ: CHAT_SERVER_CMD
CHAT_SERVER_GET_CHANNEL_GROUP_INFO_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_GROUP_SWITCH_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CHANNEL_GROUP_SWITCH_RSP: CHAT_SERVER_CMD
CHAT_SERVER_DEL_PRIVATE_CHAT_RECORD_REQ: CHAT_SERVER_CMD
CHAT_SERVER_DEL_PRIVATE_CHAT_RECORD_RSP: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_CHAT_RECORD_REQ: CHAT_SERVER_CMD
CHAT_SERVER_DEL_CHANNEL_CHAT_RECORD_RSP: CHAT_SERVER_CMD
CHAT_SERVER_DEL_WORLD_CHAT_RECORD_REQ: CHAT_SERVER_CMD
CHAT_SERVER_DEL_WORLD_CHAT_RECORD_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CLEAR_USER_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CLEAR_USER_RSP: CHAT_SERVER_CMD
CHAT_SERVER_USERID_REGISTER_REQ: CHAT_SERVER_CMD
CHAT_SERVER_USERID_REGISTER_RSP: CHAT_SERVER_CMD
CHAT_SERVER_CROSS_PRIVATE_CHAT_REQ: CHAT_SERVER_CMD
CHAT_SERVER_CROSS_PRIVATE_CHAT_RSP: CHAT_SERVER_CMD

class ServerRegisterReq(_message.Message):
    __slots__ = ("server_id", "server_token")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    server_token: str
    def __init__(self, server_id: _Optional[str] = ..., server_token: _Optional[str] = ...) -> None: ...

class ServerRegisterRsp(_message.Message):
    __slots__ = ("code", "msg", "server_id")
    class ServerRegisterCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ServerRegisterRsp.ServerRegisterCode]
        TOKEN_INVALID: _ClassVar[ServerRegisterRsp.ServerRegisterCode]
        ALREADY_REGISTER: _ClassVar[ServerRegisterRsp.ServerRegisterCode]
    SUCCESS: ServerRegisterRsp.ServerRegisterCode
    TOKEN_INVALID: ServerRegisterRsp.ServerRegisterCode
    ALREADY_REGISTER: ServerRegisterRsp.ServerRegisterCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    code: ServerRegisterRsp.ServerRegisterCode
    msg: str
    server_id: str
    def __init__(self, code: _Optional[_Union[ServerRegisterRsp.ServerRegisterCode, str]] = ..., msg: _Optional[str] = ..., server_id: _Optional[str] = ...) -> None: ...

class GetClientTokenReq(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class GetClientTokenRsp(_message.Message):
    __slots__ = ("code", "msg", "client_token", "client_id")
    class GetClientTokenCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetClientTokenRsp.GetClientTokenCode]
        INNER_ERR: _ClassVar[GetClientTokenRsp.GetClientTokenCode]
        NOT_REGISTER: _ClassVar[GetClientTokenRsp.GetClientTokenCode]
    SUCCESS: GetClientTokenRsp.GetClientTokenCode
    INNER_ERR: GetClientTokenRsp.GetClientTokenCode
    NOT_REGISTER: GetClientTokenRsp.GetClientTokenCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: GetClientTokenRsp.GetClientTokenCode
    msg: str
    client_token: str
    client_id: str
    def __init__(self, code: _Optional[_Union[GetClientTokenRsp.GetClientTokenCode, str]] = ..., msg: _Optional[str] = ..., client_token: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class CreateChannelReq(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class CreateChannelRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id")
    class CreateChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[CreateChannelRsp.CreateChannelCode]
        NOT_REGISTER: _ClassVar[CreateChannelRsp.CreateChannelCode]
        ALREADY_CREATE: _ClassVar[CreateChannelRsp.CreateChannelCode]
    SUCCESS: CreateChannelRsp.CreateChannelCode
    NOT_REGISTER: CreateChannelRsp.CreateChannelCode
    ALREADY_CREATE: CreateChannelRsp.CreateChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: CreateChannelRsp.CreateChannelCode
    msg: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[CreateChannelRsp.CreateChannelCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class DelChannelReq(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class DelChannelRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id")
    class DelChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DelChannelRsp.DelChannelCode]
        NOT_REGISTER: _ClassVar[DelChannelRsp.DelChannelCode]
        CHANNEL_ID_INVALID: _ClassVar[DelChannelRsp.DelChannelCode]
    SUCCESS: DelChannelRsp.DelChannelCode
    NOT_REGISTER: DelChannelRsp.DelChannelCode
    CHANNEL_ID_INVALID: DelChannelRsp.DelChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: DelChannelRsp.DelChannelCode
    msg: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[DelChannelRsp.DelChannelCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class JoinChannelReq(_message.Message):
    __slots__ = ("channel_id", "client_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    client_id: str
    def __init__(self, channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class JoinChannelRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id", "client_id")
    class JoinChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[JoinChannelRsp.JoinChannelCode]
        NOT_REGISTER: _ClassVar[JoinChannelRsp.JoinChannelCode]
        CHANNEL_ID_INVALID: _ClassVar[JoinChannelRsp.JoinChannelCode]
        JOIN_ALREADY: _ClassVar[JoinChannelRsp.JoinChannelCode]
        JOIN_GROUP_CHANNEL_FAILED: _ClassVar[JoinChannelRsp.JoinChannelCode]
    SUCCESS: JoinChannelRsp.JoinChannelCode
    NOT_REGISTER: JoinChannelRsp.JoinChannelCode
    CHANNEL_ID_INVALID: JoinChannelRsp.JoinChannelCode
    JOIN_ALREADY: JoinChannelRsp.JoinChannelCode
    JOIN_GROUP_CHANNEL_FAILED: JoinChannelRsp.JoinChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: JoinChannelRsp.JoinChannelCode
    msg: str
    channel_id: str
    client_id: str
    def __init__(self, code: _Optional[_Union[JoinChannelRsp.JoinChannelCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class OutChannelReq(_message.Message):
    __slots__ = ("channel_id", "client_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    client_id: str
    def __init__(self, channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class OutChannelRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id", "client_id")
    class OutChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[OutChannelRsp.OutChannelCode]
        NOT_REGISTER: _ClassVar[OutChannelRsp.OutChannelCode]
        CHANNEL_ID_INVALID: _ClassVar[OutChannelRsp.OutChannelCode]
        NOT_IN_CHANNEL: _ClassVar[OutChannelRsp.OutChannelCode]
    SUCCESS: OutChannelRsp.OutChannelCode
    NOT_REGISTER: OutChannelRsp.OutChannelCode
    CHANNEL_ID_INVALID: OutChannelRsp.OutChannelCode
    NOT_IN_CHANNEL: OutChannelRsp.OutChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: OutChannelRsp.OutChannelCode
    msg: str
    channel_id: str
    client_id: str
    def __init__(self, code: _Optional[_Union[OutChannelRsp.OutChannelCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class GetChannelMemberReq(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetChannelMemberRsp(_message.Message):
    __slots__ = ("code", "msg", "member_list", "channel_id")
    class GetChannelMemberCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetChannelMemberRsp.GetChannelMemberCode]
        NOT_REGISTER: _ClassVar[GetChannelMemberRsp.GetChannelMemberCode]
        CHANNEL_ID_INVALID: _ClassVar[GetChannelMemberRsp.GetChannelMemberCode]
    SUCCESS: GetChannelMemberRsp.GetChannelMemberCode
    NOT_REGISTER: GetChannelMemberRsp.GetChannelMemberCode
    CHANNEL_ID_INVALID: GetChannelMemberRsp.GetChannelMemberCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: GetChannelMemberRsp.GetChannelMemberCode
    msg: str
    member_list: _containers.RepeatedScalarFieldContainer[str]
    channel_id: str
    def __init__(self, code: _Optional[_Union[GetChannelMemberRsp.GetChannelMemberCode, str]] = ..., msg: _Optional[str] = ..., member_list: _Optional[_Iterable[str]] = ..., channel_id: _Optional[str] = ...) -> None: ...

class SyncChannelMemberReq(_message.Message):
    __slots__ = ("channel_id", "member_list")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    member_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_id: _Optional[str] = ..., member_list: _Optional[_Iterable[str]] = ...) -> None: ...

class SyncChannelMemberRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id")
    class SyncChannelMember(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SyncChannelMemberRsp.SyncChannelMember]
        NOT_REGISTER: _ClassVar[SyncChannelMemberRsp.SyncChannelMember]
        CHANNEL_ID_INVALID: _ClassVar[SyncChannelMemberRsp.SyncChannelMember]
    SUCCESS: SyncChannelMemberRsp.SyncChannelMember
    NOT_REGISTER: SyncChannelMemberRsp.SyncChannelMember
    CHANNEL_ID_INVALID: SyncChannelMemberRsp.SyncChannelMember
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: SyncChannelMemberRsp.SyncChannelMember
    msg: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[SyncChannelMemberRsp.SyncChannelMember, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ChannelBanReq(_message.Message):
    __slots__ = ("channel_id", "is_ban", "black_list", "white_list")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    BLACK_LIST_FIELD_NUMBER: _ClassVar[int]
    WHITE_LIST_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    is_ban: bool
    black_list: _containers.RepeatedScalarFieldContainer[str]
    white_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_id: _Optional[str] = ..., is_ban: bool = ..., black_list: _Optional[_Iterable[str]] = ..., white_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ChannelBanRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id")
    class ChannelBanCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ChannelBanRsp.ChannelBanCode]
        NOT_REGISTER: _ClassVar[ChannelBanRsp.ChannelBanCode]
        CHANNEL_ID_INVALID: _ClassVar[ChannelBanRsp.ChannelBanCode]
    SUCCESS: ChannelBanRsp.ChannelBanCode
    NOT_REGISTER: ChannelBanRsp.ChannelBanCode
    CHANNEL_ID_INVALID: ChannelBanRsp.ChannelBanCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: ChannelBanRsp.ChannelBanCode
    msg: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[ChannelBanRsp.ChannelBanCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ChannelGroupBanReq(_message.Message):
    __slots__ = ("group_id", "client_id", "is_ban")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    client_id: str
    is_ban: bool
    def __init__(self, group_id: _Optional[str] = ..., client_id: _Optional[str] = ..., is_ban: bool = ...) -> None: ...

class ChannelGroupBanRsp(_message.Message):
    __slots__ = ("code", "msg", "group_id", "client_id")
    class ChannelGroupBan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ChannelGroupBanRsp.ChannelGroupBan]
        NOT_REGISTER: _ClassVar[ChannelGroupBanRsp.ChannelGroupBan]
        GROUP_ID_INVALID: _ClassVar[ChannelGroupBanRsp.ChannelGroupBan]
    SUCCESS: ChannelGroupBanRsp.ChannelGroupBan
    NOT_REGISTER: ChannelGroupBanRsp.ChannelGroupBan
    GROUP_ID_INVALID: ChannelGroupBanRsp.ChannelGroupBan
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: ChannelGroupBanRsp.ChannelGroupBan
    msg: str
    group_id: str
    client_id: str
    def __init__(self, code: _Optional[_Union[ChannelGroupBanRsp.ChannelGroupBan, str]] = ..., msg: _Optional[str] = ..., group_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class PersonalBanReq(_message.Message):
    __slots__ = ("client_id", "is_ban", "ban_time")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    BAN_TIME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    is_ban: bool
    ban_time: int
    def __init__(self, client_id: _Optional[str] = ..., is_ban: bool = ..., ban_time: _Optional[int] = ...) -> None: ...

class PersonalBanRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id")
    class PersonalBanCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[PersonalBanRsp.PersonalBanCode]
        NOT_REGISTER: _ClassVar[PersonalBanRsp.PersonalBanCode]
    SUCCESS: PersonalBanRsp.PersonalBanCode
    NOT_REGISTER: PersonalBanRsp.PersonalBanCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: PersonalBanRsp.PersonalBanCode
    msg: str
    client_id: str
    def __init__(self, code: _Optional[_Union[PersonalBanRsp.PersonalBanCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class GetPersonalChannelLevelReq(_message.Message):
    __slots__ = ("channel_id", "client_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    client_id: str
    def __init__(self, channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class GetPersonalChannelLevelRsp(_message.Message):
    __slots__ = ("code", "msg", "level", "channel_id", "client_id")
    class GetPersonalChannelLevelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode]
        NOT_REGISTER: _ClassVar[GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode]
        CHANNEL_ID_INVALID: _ClassVar[GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode]
    SUCCESS: GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode
    NOT_REGISTER: GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode
    CHANNEL_ID_INVALID: GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode
    msg: str
    level: int
    channel_id: str
    client_id: str
    def __init__(self, code: _Optional[_Union[GetPersonalChannelLevelRsp.GetPersonalChannelLevelCode, str]] = ..., msg: _Optional[str] = ..., level: _Optional[int] = ..., channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class UpdatePersonalChannelLevelReq(_message.Message):
    __slots__ = ("channel_id", "client_id", "level")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    client_id: str
    level: int
    def __init__(self, channel_id: _Optional[str] = ..., client_id: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...

class UpdatePersonalChannelLevelRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id", "client_id")
    class UpdatePersonalChannelLevelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode]
        NOT_REGISTER: _ClassVar[UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode]
        CHANNEL_ID_INVALID: _ClassVar[UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode]
    SUCCESS: UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode
    NOT_REGISTER: UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode
    CHANNEL_ID_INVALID: UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode
    msg: str
    channel_id: str
    client_id: str
    def __init__(self, code: _Optional[_Union[UpdatePersonalChannelLevelRsp.UpdatePersonalChannelLevelCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class SyncUserChannelReq(_message.Message):
    __slots__ = ("client_id", "channel_id_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    channel_id_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., channel_id_list: _Optional[_Iterable[str]] = ...) -> None: ...

class SyncUserChannelRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id")
    class SyncUserChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SyncUserChannelRsp.SyncUserChannelCode]
        NOT_REGISTER: _ClassVar[SyncUserChannelRsp.SyncUserChannelCode]
    SUCCESS: SyncUserChannelRsp.SyncUserChannelCode
    NOT_REGISTER: SyncUserChannelRsp.SyncUserChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: SyncUserChannelRsp.SyncUserChannelCode
    msg: str
    client_id: str
    def __init__(self, code: _Optional[_Union[SyncUserChannelRsp.SyncUserChannelCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class SystemPrivateChatReq(_message.Message):
    __slots__ = ("to_client_id", "msg")
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    to_client_id: str
    msg: str
    def __init__(self, to_client_id: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class SystemPrivateChatRsp(_message.Message):
    __slots__ = ("code", "msg", "to_client_id")
    class PrivateChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SystemPrivateChatRsp.PrivateChatCode]
        INNER_ERR: _ClassVar[SystemPrivateChatRsp.PrivateChatCode]
        NOT_REGISTER: _ClassVar[SystemPrivateChatRsp.PrivateChatCode]
    SUCCESS: SystemPrivateChatRsp.PrivateChatCode
    INNER_ERR: SystemPrivateChatRsp.PrivateChatCode
    NOT_REGISTER: SystemPrivateChatRsp.PrivateChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: SystemPrivateChatRsp.PrivateChatCode
    msg: str
    to_client_id: str
    def __init__(self, code: _Optional[_Union[SystemPrivateChatRsp.PrivateChatCode, str]] = ..., msg: _Optional[str] = ..., to_client_id: _Optional[str] = ...) -> None: ...

class SystemChannelChatReq(_message.Message):
    __slots__ = ("channel_id", "msg")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    msg: str
    def __init__(self, channel_id: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class SystemChannelChatRsp(_message.Message):
    __slots__ = ("code", "msg", "channel_id")
    class ChannelChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SystemChannelChatRsp.ChannelChatCode]
        INNER_ERR: _ClassVar[SystemChannelChatRsp.ChannelChatCode]
        NOT_REGISTER: _ClassVar[SystemChannelChatRsp.ChannelChatCode]
        CHANNEL_ID_INVALID: _ClassVar[SystemChannelChatRsp.ChannelChatCode]
    SUCCESS: SystemChannelChatRsp.ChannelChatCode
    INNER_ERR: SystemChannelChatRsp.ChannelChatCode
    NOT_REGISTER: SystemChannelChatRsp.ChannelChatCode
    CHANNEL_ID_INVALID: SystemChannelChatRsp.ChannelChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: SystemChannelChatRsp.ChannelChatCode
    msg: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[SystemChannelChatRsp.ChannelChatCode, str]] = ..., msg: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class SystemWorldChatReq(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class SystemWorldChatRsp(_message.Message):
    __slots__ = ("code", "msg")
    class WorldChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SystemWorldChatRsp.WorldChatCode]
        INNER_ERR: _ClassVar[SystemWorldChatRsp.WorldChatCode]
        NOT_REGISTER: _ClassVar[SystemWorldChatRsp.WorldChatCode]
    SUCCESS: SystemWorldChatRsp.WorldChatCode
    INNER_ERR: SystemWorldChatRsp.WorldChatCode
    NOT_REGISTER: SystemWorldChatRsp.WorldChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    code: SystemWorldChatRsp.WorldChatCode
    msg: str
    def __init__(self, code: _Optional[_Union[SystemWorldChatRsp.WorldChatCode, str]] = ..., msg: _Optional[str] = ...) -> None: ...

class CreateChannelGroupReq(_message.Message):
    __slots__ = ("group_id", "default_channel_count", "max_channel_member_count")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CHANNEL_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    default_channel_count: int
    max_channel_member_count: int
    def __init__(self, group_id: _Optional[str] = ..., default_channel_count: _Optional[int] = ..., max_channel_member_count: _Optional[int] = ...) -> None: ...

class CreateChannelGroupRsp(_message.Message):
    __slots__ = ("code", "msg", "group_id")
    class CreateChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[CreateChannelGroupRsp.CreateChannelCode]
        INNER_ERR: _ClassVar[CreateChannelGroupRsp.CreateChannelCode]
        NOT_REGISTER: _ClassVar[CreateChannelGroupRsp.CreateChannelCode]
        ALREADY_CREATE: _ClassVar[CreateChannelGroupRsp.CreateChannelCode]
    SUCCESS: CreateChannelGroupRsp.CreateChannelCode
    INNER_ERR: CreateChannelGroupRsp.CreateChannelCode
    NOT_REGISTER: CreateChannelGroupRsp.CreateChannelCode
    ALREADY_CREATE: CreateChannelGroupRsp.CreateChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    code: CreateChannelGroupRsp.CreateChannelCode
    msg: str
    group_id: str
    def __init__(self, code: _Optional[_Union[CreateChannelGroupRsp.CreateChannelCode, str]] = ..., msg: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class DelChannelGroupReq(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DelChannelGroupRsp(_message.Message):
    __slots__ = ("code", "msg", "group_id")
    class CreateChannelCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DelChannelGroupRsp.CreateChannelCode]
        INNER_ERR: _ClassVar[DelChannelGroupRsp.CreateChannelCode]
        NOT_REGISTER: _ClassVar[DelChannelGroupRsp.CreateChannelCode]
        GROUP_ID_INVALID: _ClassVar[DelChannelGroupRsp.CreateChannelCode]
    SUCCESS: DelChannelGroupRsp.CreateChannelCode
    INNER_ERR: DelChannelGroupRsp.CreateChannelCode
    NOT_REGISTER: DelChannelGroupRsp.CreateChannelCode
    GROUP_ID_INVALID: DelChannelGroupRsp.CreateChannelCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    code: DelChannelGroupRsp.CreateChannelCode
    msg: str
    group_id: str
    def __init__(self, code: _Optional[_Union[DelChannelGroupRsp.CreateChannelCode, str]] = ..., msg: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class ClearUserReq(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ClearUserRsp(_message.Message):
    __slots__ = ("code", "msg", "user_id")
    class ClearUserCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ClearUserRsp.ClearUserCode]
        INNER_ERR: _ClassVar[ClearUserRsp.ClearUserCode]
        NOT_REGISTER: _ClassVar[ClearUserRsp.ClearUserCode]
        USER_ID_INVALID: _ClassVar[ClearUserRsp.ClearUserCode]
    SUCCESS: ClearUserRsp.ClearUserCode
    INNER_ERR: ClearUserRsp.ClearUserCode
    NOT_REGISTER: ClearUserRsp.ClearUserCode
    USER_ID_INVALID: ClearUserRsp.ClearUserCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    code: ClearUserRsp.ClearUserCode
    msg: str
    user_id: str
    def __init__(self, code: _Optional[_Union[ClearUserRsp.ClearUserCode, str]] = ..., msg: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserIDRegisterReq(_message.Message):
    __slots__ = ("user_id_list",)
    USER_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    user_id_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id_list: _Optional[_Iterable[str]] = ...) -> None: ...

class UserIDRegisterRsp(_message.Message):
    __slots__ = ("code", "msg")
    class UserIDRegisterCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[UserIDRegisterRsp.UserIDRegisterCode]
        SERVER_NOT_REGISTER: _ClassVar[UserIDRegisterRsp.UserIDRegisterCode]
    SUCCESS: UserIDRegisterRsp.UserIDRegisterCode
    SERVER_NOT_REGISTER: UserIDRegisterRsp.UserIDRegisterCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    code: UserIDRegisterRsp.UserIDRegisterCode
    msg: str
    def __init__(self, code: _Optional[_Union[UserIDRegisterRsp.UserIDRegisterCode, str]] = ..., msg: _Optional[str] = ...) -> None: ...

class CrossPrivateChatReq(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "to_group_id", "to_client_id", "msg")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    TO_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    to_group_id: str
    to_client_id: str
    msg: str
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., to_group_id: _Optional[str] = ..., to_client_id: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class CrossPrivateChatRsp(_message.Message):
    __slots__ = ("code", "msg", "from_client_id", "to_group_id", "to_client_id", "left_cd_time")
    class CrossPrivateChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[CrossPrivateChatRsp.CrossPrivateChatCode]
        INNER_ERR: _ClassVar[CrossPrivateChatRsp.CrossPrivateChatCode]
        NOT_REGISTER: _ClassVar[CrossPrivateChatRsp.CrossPrivateChatCode]
        IN_BAN: _ClassVar[CrossPrivateChatRsp.CrossPrivateChatCode]
        CD_LIMIT: _ClassVar[CrossPrivateChatRsp.CrossPrivateChatCode]
    SUCCESS: CrossPrivateChatRsp.CrossPrivateChatCode
    INNER_ERR: CrossPrivateChatRsp.CrossPrivateChatCode
    NOT_REGISTER: CrossPrivateChatRsp.CrossPrivateChatCode
    IN_BAN: CrossPrivateChatRsp.CrossPrivateChatCode
    CD_LIMIT: CrossPrivateChatRsp.CrossPrivateChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TO_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    code: CrossPrivateChatRsp.CrossPrivateChatCode
    msg: str
    from_client_id: str
    to_group_id: str
    to_client_id: str
    left_cd_time: int
    def __init__(self, code: _Optional[_Union[CrossPrivateChatRsp.CrossPrivateChatCode, str]] = ..., msg: _Optional[str] = ..., from_client_id: _Optional[str] = ..., to_group_id: _Optional[str] = ..., to_client_id: _Optional[str] = ..., left_cd_time: _Optional[int] = ...) -> None: ...
