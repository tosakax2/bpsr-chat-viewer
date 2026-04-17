from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CHAT_CLIENT_CMD(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_CLIENT_CMD_INVALID: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_REGISTER_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_REGISTER_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_UNREGISTER_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_UNREGISTER_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_PRIVATE_CHAT_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_PRIVATE_CHAT_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_CHANNEL_CHAT_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_CHANNEL_CHAT_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_WORLD_CHAT_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_WORLD_CHAT_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_PRIVATE_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_PRIVATE_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_CHANNEL_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_CHANNEL_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_WORLD_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_WORLD_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_PRIVATE_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_PRIVATE_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_CHANNEL_GROUP_INFO_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_CHANNEL_GROUP_INFO_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_CHANNEL_GROUP_SWITCH_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_CHANNEL_GROUP_SWITCH_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_ADD_BLACKLIST_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_ADD_BLACKLIST_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_REMOVE_BLACKLIST_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_REMOVE_BLACKLIST_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_BLACKLIST_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_BLACKLIST_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_SYNC_BLACKLIST_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_SYNC_BLACKLIST_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_PERSONAL_BAN_INFO_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_GET_PERSONAL_BAN_INFO_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_CHANNEL_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_CHANNEL_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_WORLD_CHAT_RECORD_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_DEL_WORLD_CHAT_RECORD_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_READ_PRIVATE_LAST_MSG_INDEX_REQ: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_READ_PRIVATE_LAST_MSG_INDEX_RSP: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_PRIVATE_CHAT_RECEIVE: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_CHANNEL_CHAT_RECEIVE: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_WORLD_CHAT_RECEIVE: _ClassVar[CHAT_CLIENT_CMD]
    CHAT_CLIENT_EVENT_NOTICE: _ClassVar[CHAT_CLIENT_CMD]
CHAT_CLIENT_CMD_INVALID: CHAT_CLIENT_CMD
CHAT_CLIENT_REGISTER_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_REGISTER_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_UNREGISTER_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_UNREGISTER_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_PRIVATE_CHAT_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_PRIVATE_CHAT_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_CHANNEL_CHAT_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_CHANNEL_CHAT_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_WORLD_CHAT_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_WORLD_CHAT_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_PRIVATE_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_PRIVATE_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_CHANNEL_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_CHANNEL_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_WORLD_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_WORLD_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_PRIVATE_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_PRIVATE_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_CHANNEL_GROUP_INFO_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_CHANNEL_GROUP_INFO_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_CHANNEL_GROUP_SWITCH_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_CHANNEL_GROUP_SWITCH_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_ADD_BLACKLIST_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_ADD_BLACKLIST_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_REMOVE_BLACKLIST_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_REMOVE_BLACKLIST_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_BLACKLIST_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_BLACKLIST_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_SYNC_BLACKLIST_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_SYNC_BLACKLIST_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_PERSONAL_BAN_INFO_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_GET_PERSONAL_BAN_INFO_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_CHANNEL_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_CHANNEL_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_WORLD_CHAT_RECORD_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_DEL_WORLD_CHAT_RECORD_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_READ_PRIVATE_LAST_MSG_INDEX_REQ: CHAT_CLIENT_CMD
CHAT_CLIENT_READ_PRIVATE_LAST_MSG_INDEX_RSP: CHAT_CLIENT_CMD
CHAT_CLIENT_PRIVATE_CHAT_RECEIVE: CHAT_CLIENT_CMD
CHAT_CLIENT_CHANNEL_CHAT_RECEIVE: CHAT_CLIENT_CMD
CHAT_CLIENT_WORLD_CHAT_RECEIVE: CHAT_CLIENT_CMD
CHAT_CLIENT_EVENT_NOTICE: CHAT_CLIENT_CMD

class JoinChannelInfo(_message.Message):
    __slots__ = ("channel_id", "msg_count")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_COUNT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    msg_count: int
    def __init__(self, channel_id: _Optional[str] = ..., msg_count: _Optional[int] = ...) -> None: ...

class ClientRegisterReq(_message.Message):
    __slots__ = ("client_id", "client_token")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_token: str
    def __init__(self, client_id: _Optional[str] = ..., client_token: _Optional[str] = ...) -> None: ...

class ClientRegisterRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "join_channel_list")
    class ClientRegisterCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ClientRegisterRsp.ClientRegisterCode]
        TOKEN_INVALID: _ClassVar[ClientRegisterRsp.ClientRegisterCode]
        ALREADY_REGISTER: _ClassVar[ClientRegisterRsp.ClientRegisterCode]
    SUCCESS: ClientRegisterRsp.ClientRegisterCode
    TOKEN_INVALID: ClientRegisterRsp.ClientRegisterCode
    ALREADY_REGISTER: ClientRegisterRsp.ClientRegisterCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_CHANNEL_LIST_FIELD_NUMBER: _ClassVar[int]
    code: ClientRegisterRsp.ClientRegisterCode
    msg: str
    client_id: str
    join_channel_list: _containers.RepeatedCompositeFieldContainer[JoinChannelInfo]
    def __init__(self, code: _Optional[_Union[ClientRegisterRsp.ClientRegisterCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., join_channel_list: _Optional[_Iterable[_Union[JoinChannelInfo, _Mapping]]] = ...) -> None: ...

class ClientUnRegisterReq(_message.Message):
    __slots__ = ("client_id", "client_token")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_token: str
    def __init__(self, client_id: _Optional[str] = ..., client_token: _Optional[str] = ...) -> None: ...

class ClientUnRegisterRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id")
    class ClientUnRegisterCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ClientUnRegisterRsp.ClientUnRegisterCode]
        TOKEN_INVALID: _ClassVar[ClientUnRegisterRsp.ClientUnRegisterCode]
        NOT_REGISTER: _ClassVar[ClientUnRegisterRsp.ClientUnRegisterCode]
    SUCCESS: ClientUnRegisterRsp.ClientUnRegisterCode
    TOKEN_INVALID: ClientUnRegisterRsp.ClientUnRegisterCode
    NOT_REGISTER: ClientUnRegisterRsp.ClientUnRegisterCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: ClientUnRegisterRsp.ClientUnRegisterCode
    msg: str
    client_id: str
    def __init__(self, code: _Optional[_Union[ClientUnRegisterRsp.ClientUnRegisterCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class PrivateChatReq(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "to_client_id", "msg")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    to_client_id: str
    msg: str
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., to_client_id: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class PrivateChatRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "to_client_id", "left_cd_time", "baseinfo", "chat_msg")
    class PrivateChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[PrivateChatRsp.PrivateChatCode]
        INNER_ERR: _ClassVar[PrivateChatRsp.PrivateChatCode]
        NOT_REGISTER: _ClassVar[PrivateChatRsp.PrivateChatCode]
        IN_BAN: _ClassVar[PrivateChatRsp.PrivateChatCode]
        IN_BLACK_LIST: _ClassVar[PrivateChatRsp.PrivateChatCode]
        CD_LIMIT: _ClassVar[PrivateChatRsp.PrivateChatCode]
        TARGET_CLIENTID_INVALID: _ClassVar[PrivateChatRsp.PrivateChatCode]
    SUCCESS: PrivateChatRsp.PrivateChatCode
    INNER_ERR: PrivateChatRsp.PrivateChatCode
    NOT_REGISTER: PrivateChatRsp.PrivateChatCode
    IN_BAN: PrivateChatRsp.PrivateChatCode
    IN_BLACK_LIST: PrivateChatRsp.PrivateChatCode
    CD_LIMIT: PrivateChatRsp.PrivateChatCode
    TARGET_CLIENTID_INVALID: PrivateChatRsp.PrivateChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    CHAT_MSG_FIELD_NUMBER: _ClassVar[int]
    code: PrivateChatRsp.PrivateChatCode
    msg: str
    client_id: str
    to_client_id: str
    left_cd_time: int
    baseinfo: bytes
    chat_msg: str
    def __init__(self, code: _Optional[_Union[PrivateChatRsp.PrivateChatCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., to_client_id: _Optional[str] = ..., left_cd_time: _Optional[int] = ..., baseinfo: _Optional[bytes] = ..., chat_msg: _Optional[str] = ...) -> None: ...

class ChannelChatReq(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "channel_id", "msg")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    channel_id: str
    msg: str
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., channel_id: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class ChannelChatRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "channel_id", "left_cd_time", "baseinfo", "chat_msg")
    class ChannelChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ChannelChatRsp.ChannelChatCode]
        INNER_ERR: _ClassVar[ChannelChatRsp.ChannelChatCode]
        NOT_REGISTER: _ClassVar[ChannelChatRsp.ChannelChatCode]
        CHANNEL_ID_INVALID: _ClassVar[ChannelChatRsp.ChannelChatCode]
        NOT_MEMBER: _ClassVar[ChannelChatRsp.ChannelChatCode]
        IN_BAN: _ClassVar[ChannelChatRsp.ChannelChatCode]
        CD_LIMIT: _ClassVar[ChannelChatRsp.ChannelChatCode]
        COUNT_LIMIT: _ClassVar[ChannelChatRsp.ChannelChatCode]
    SUCCESS: ChannelChatRsp.ChannelChatCode
    INNER_ERR: ChannelChatRsp.ChannelChatCode
    NOT_REGISTER: ChannelChatRsp.ChannelChatCode
    CHANNEL_ID_INVALID: ChannelChatRsp.ChannelChatCode
    NOT_MEMBER: ChannelChatRsp.ChannelChatCode
    IN_BAN: ChannelChatRsp.ChannelChatCode
    CD_LIMIT: ChannelChatRsp.ChannelChatCode
    COUNT_LIMIT: ChannelChatRsp.ChannelChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    CHAT_MSG_FIELD_NUMBER: _ClassVar[int]
    code: ChannelChatRsp.ChannelChatCode
    msg: str
    client_id: str
    channel_id: str
    left_cd_time: int
    baseinfo: bytes
    chat_msg: str
    def __init__(self, code: _Optional[_Union[ChannelChatRsp.ChannelChatCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., left_cd_time: _Optional[int] = ..., baseinfo: _Optional[bytes] = ..., chat_msg: _Optional[str] = ...) -> None: ...

class WorldChatReq(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "msg")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    msg: str
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., msg: _Optional[str] = ...) -> None: ...

class WorldChatRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "left_cd_time", "baseinfo", "chat_msg")
    class WorldChatCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[WorldChatRsp.WorldChatCode]
        INNER_ERR: _ClassVar[WorldChatRsp.WorldChatCode]
        NOT_REGISTER: _ClassVar[WorldChatRsp.WorldChatCode]
        IN_BAN: _ClassVar[WorldChatRsp.WorldChatCode]
        CD_LIMIT: _ClassVar[WorldChatRsp.WorldChatCode]
        COUNT_LIMIT: _ClassVar[WorldChatRsp.WorldChatCode]
    SUCCESS: WorldChatRsp.WorldChatCode
    INNER_ERR: WorldChatRsp.WorldChatCode
    NOT_REGISTER: WorldChatRsp.WorldChatCode
    IN_BAN: WorldChatRsp.WorldChatCode
    CD_LIMIT: WorldChatRsp.WorldChatCode
    COUNT_LIMIT: WorldChatRsp.WorldChatCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    CHAT_MSG_FIELD_NUMBER: _ClassVar[int]
    code: WorldChatRsp.WorldChatCode
    msg: str
    client_id: str
    left_cd_time: int
    baseinfo: bytes
    chat_msg: str
    def __init__(self, code: _Optional[_Union[WorldChatRsp.WorldChatCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., left_cd_time: _Optional[int] = ..., baseinfo: _Optional[bytes] = ..., chat_msg: _Optional[str] = ...) -> None: ...

class ChatRecord(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "msg", "send_time", "index")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    msg: str
    send_time: int
    index: int
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., msg: _Optional[str] = ..., send_time: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class GetPrivateRecordReq(_message.Message):
    __slots__ = ("client_id", "target_client_id", "is_batch_get", "start_index", "count")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BATCH_GET_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    target_client_id: str
    is_batch_get: bool
    start_index: int
    count: int
    def __init__(self, client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ..., is_batch_get: bool = ..., start_index: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class GetPrivateRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "target_client_id", "record_list", "total_count", "un_read_count", "readed_last_index")
    class GetPrivateRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetPrivateRecordRsp.GetPrivateRecordCode]
        INNER_ERR: _ClassVar[GetPrivateRecordRsp.GetPrivateRecordCode]
        NOT_REGISTER: _ClassVar[GetPrivateRecordRsp.GetPrivateRecordCode]
        INDEX_ERR: _ClassVar[GetPrivateRecordRsp.GetPrivateRecordCode]
    SUCCESS: GetPrivateRecordRsp.GetPrivateRecordCode
    INNER_ERR: GetPrivateRecordRsp.GetPrivateRecordCode
    NOT_REGISTER: GetPrivateRecordRsp.GetPrivateRecordCode
    INDEX_ERR: GetPrivateRecordRsp.GetPrivateRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UN_READ_COUNT_FIELD_NUMBER: _ClassVar[int]
    READED_LAST_INDEX_FIELD_NUMBER: _ClassVar[int]
    code: GetPrivateRecordRsp.GetPrivateRecordCode
    msg: str
    client_id: str
    target_client_id: str
    record_list: _containers.RepeatedCompositeFieldContainer[ChatRecord]
    total_count: int
    un_read_count: int
    readed_last_index: int
    def __init__(self, code: _Optional[_Union[GetPrivateRecordRsp.GetPrivateRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ..., record_list: _Optional[_Iterable[_Union[ChatRecord, _Mapping]]] = ..., total_count: _Optional[int] = ..., un_read_count: _Optional[int] = ..., readed_last_index: _Optional[int] = ...) -> None: ...

class GetChannelRecordReq(_message.Message):
    __slots__ = ("client_id", "channel_id", "is_batch_get", "start_index", "count")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BATCH_GET_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    channel_id: str
    is_batch_get: bool
    start_index: int
    count: int
    def __init__(self, client_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., is_batch_get: bool = ..., start_index: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class GetChannelRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "channel_id", "record_list", "total_count")
    class GetChannelRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
        INNER_ERR: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
        NOT_REGISTER: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
        CHANNEL_ID_INVALID: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
        NOT_MEMBER: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
        INDEX_ERR: _ClassVar[GetChannelRecordRsp.GetChannelRecordCode]
    SUCCESS: GetChannelRecordRsp.GetChannelRecordCode
    INNER_ERR: GetChannelRecordRsp.GetChannelRecordCode
    NOT_REGISTER: GetChannelRecordRsp.GetChannelRecordCode
    CHANNEL_ID_INVALID: GetChannelRecordRsp.GetChannelRecordCode
    NOT_MEMBER: GetChannelRecordRsp.GetChannelRecordCode
    INDEX_ERR: GetChannelRecordRsp.GetChannelRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    code: GetChannelRecordRsp.GetChannelRecordCode
    msg: str
    client_id: str
    channel_id: str
    record_list: _containers.RepeatedCompositeFieldContainer[ChatRecord]
    total_count: int
    def __init__(self, code: _Optional[_Union[GetChannelRecordRsp.GetChannelRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., record_list: _Optional[_Iterable[_Union[ChatRecord, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetWorldRecordReq(_message.Message):
    __slots__ = ("client_id", "is_batch_get", "start_index", "count")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BATCH_GET_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    is_batch_get: bool
    start_index: int
    count: int
    def __init__(self, client_id: _Optional[str] = ..., is_batch_get: bool = ..., start_index: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class GetWorldRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "record_list", "total_count")
    class GetWorldRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetWorldRecordRsp.GetWorldRecordCode]
        INNER_ERR: _ClassVar[GetWorldRecordRsp.GetWorldRecordCode]
        NOT_REGISTER: _ClassVar[GetWorldRecordRsp.GetWorldRecordCode]
        INDEX_ERR: _ClassVar[GetWorldRecordRsp.GetWorldRecordCode]
    SUCCESS: GetWorldRecordRsp.GetWorldRecordCode
    INNER_ERR: GetWorldRecordRsp.GetWorldRecordCode
    NOT_REGISTER: GetWorldRecordRsp.GetWorldRecordCode
    INDEX_ERR: GetWorldRecordRsp.GetWorldRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    code: GetWorldRecordRsp.GetWorldRecordCode
    msg: str
    client_id: str
    record_list: _containers.RepeatedCompositeFieldContainer[ChatRecord]
    total_count: int
    def __init__(self, code: _Optional[_Union[GetWorldRecordRsp.GetWorldRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., record_list: _Optional[_Iterable[_Union[ChatRecord, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class ReadPrivateLastMsgIndexReq(_message.Message):
    __slots__ = ("client_id", "target_client_id", "last_index")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEX_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    target_client_id: str
    last_index: int
    def __init__(self, client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ..., last_index: _Optional[int] = ...) -> None: ...

class ReadPrivateLastMsgIndexRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "target_client_id", "last_index")
    class ReadPrivateLastMsgIndexCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode]
        INNER_ERR: _ClassVar[ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode]
        NOT_REGISTER: _ClassVar[ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode]
        INDEX_ERR: _ClassVar[ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode]
    SUCCESS: ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode
    INNER_ERR: ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode
    NOT_REGISTER: ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode
    INDEX_ERR: ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEX_FIELD_NUMBER: _ClassVar[int]
    code: ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode
    msg: str
    client_id: str
    target_client_id: str
    last_index: int
    def __init__(self, code: _Optional[_Union[ReadPrivateLastMsgIndexRsp.ReadPrivateLastMsgIndexCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ..., last_index: _Optional[int] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("from_client_id", "baseinfo", "msg", "send_time", "index")
    FROM_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASEINFO_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    from_client_id: str
    baseinfo: bytes
    msg: str
    send_time: int
    index: int
    def __init__(self, from_client_id: _Optional[str] = ..., baseinfo: _Optional[bytes] = ..., msg: _Optional[str] = ..., send_time: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class PrivateMessage(_message.Message):
    __slots__ = ("client_id", "msg_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    msg_list: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    def __init__(self, client_id: _Optional[str] = ..., msg_list: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ...) -> None: ...

class PrivateChatReceive(_message.Message):
    __slots__ = ("msg_list",)
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    msg_list: _containers.RepeatedCompositeFieldContainer[PrivateMessage]
    def __init__(self, msg_list: _Optional[_Iterable[_Union[PrivateMessage, _Mapping]]] = ...) -> None: ...

class ChannelMessage(_message.Message):
    __slots__ = ("client_id", "channel_id", "msg_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    channel_id: str
    msg_list: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    def __init__(self, client_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., msg_list: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ...) -> None: ...

class ChannelChatReceive(_message.Message):
    __slots__ = ("msg_list",)
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    msg_list: _containers.RepeatedCompositeFieldContainer[ChannelMessage]
    def __init__(self, msg_list: _Optional[_Iterable[_Union[ChannelMessage, _Mapping]]] = ...) -> None: ...

class WorldMessage(_message.Message):
    __slots__ = ("client_id", "msg_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    msg_list: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    def __init__(self, client_id: _Optional[str] = ..., msg_list: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ...) -> None: ...

class WorldChatReceive(_message.Message):
    __slots__ = ("msg_list",)
    MSG_LIST_FIELD_NUMBER: _ClassVar[int]
    msg_list: _containers.RepeatedCompositeFieldContainer[WorldMessage]
    def __init__(self, msg_list: _Optional[_Iterable[_Union[WorldMessage, _Mapping]]] = ...) -> None: ...

class ChatEventNotice(_message.Message):
    __slots__ = ("event_type", "id", "state")
    class CHAT_EVENT_TYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHAT_EVENT_TYPE_NONE: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_CHANNEL_JOIN: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_CHANNEL_OUT: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_CHANNEL_GROUP_CHANGE: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_PERSONAL_BAN_CHANGE: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_CHANNEL_BAN_CHANGE: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
        CHAT_EVENT_TYPE_CHANNEL_GROUP_BAN_CHANGE: _ClassVar[ChatEventNotice.CHAT_EVENT_TYPE]
    CHAT_EVENT_TYPE_NONE: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_CHANNEL_JOIN: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_CHANNEL_OUT: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_CHANNEL_GROUP_CHANGE: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_PERSONAL_BAN_CHANGE: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_CHANNEL_BAN_CHANGE: ChatEventNotice.CHAT_EVENT_TYPE
    CHAT_EVENT_TYPE_CHANNEL_GROUP_BAN_CHANGE: ChatEventNotice.CHAT_EVENT_TYPE
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    event_type: ChatEventNotice.CHAT_EVENT_TYPE
    id: str
    state: int
    def __init__(self, event_type: _Optional[_Union[ChatEventNotice.CHAT_EVENT_TYPE, str]] = ..., id: _Optional[str] = ..., state: _Optional[int] = ...) -> None: ...

class BaseInfo(_message.Message):
    __slots__ = ("char_id", "head_id", "model_id", "player_uuid", "player_name", "player_level")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HEAD_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_UUID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    head_id: int
    model_id: int
    player_uuid: int
    player_name: str
    player_level: int
    def __init__(self, char_id: _Optional[int] = ..., head_id: _Optional[int] = ..., model_id: _Optional[int] = ..., player_uuid: _Optional[int] = ..., player_name: _Optional[str] = ..., player_level: _Optional[int] = ...) -> None: ...
