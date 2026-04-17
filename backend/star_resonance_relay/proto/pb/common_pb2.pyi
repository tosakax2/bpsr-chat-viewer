from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DelPrivateRecordReq(_message.Message):
    __slots__ = ("client_id", "target_client_id", "index", "all")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    target_client_id: str
    index: _containers.RepeatedScalarFieldContainer[int]
    all: bool
    def __init__(self, client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ..., index: _Optional[_Iterable[int]] = ..., all: bool = ...) -> None: ...

class DelPrivateRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "target_client_id")
    class DelPrivateRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DelPrivateRecordRsp.DelPrivateRecordCode]
        INNER_ERR: _ClassVar[DelPrivateRecordRsp.DelPrivateRecordCode]
        NOT_REGISTER: _ClassVar[DelPrivateRecordRsp.DelPrivateRecordCode]
        INDEX_ERR: _ClassVar[DelPrivateRecordRsp.DelPrivateRecordCode]
    SUCCESS: DelPrivateRecordRsp.DelPrivateRecordCode
    INNER_ERR: DelPrivateRecordRsp.DelPrivateRecordCode
    NOT_REGISTER: DelPrivateRecordRsp.DelPrivateRecordCode
    INDEX_ERR: DelPrivateRecordRsp.DelPrivateRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: DelPrivateRecordRsp.DelPrivateRecordCode
    msg: str
    client_id: str
    target_client_id: str
    def __init__(self, code: _Optional[_Union[DelPrivateRecordRsp.DelPrivateRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ...) -> None: ...

class DelChannelRecordReq(_message.Message):
    __slots__ = ("client_id", "channel_id", "index")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    channel_id: str
    index: int
    def __init__(self, client_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class DelChannelRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "channel_id")
    class DelChannelRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DelChannelRecordRsp.DelChannelRecordCode]
        INNER_ERR: _ClassVar[DelChannelRecordRsp.DelChannelRecordCode]
        NOT_REGISTER: _ClassVar[DelChannelRecordRsp.DelChannelRecordCode]
    SUCCESS: DelChannelRecordRsp.DelChannelRecordCode
    INNER_ERR: DelChannelRecordRsp.DelChannelRecordCode
    NOT_REGISTER: DelChannelRecordRsp.DelChannelRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: DelChannelRecordRsp.DelChannelRecordCode
    msg: str
    client_id: str
    channel_id: str
    def __init__(self, code: _Optional[_Union[DelChannelRecordRsp.DelChannelRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class DelWorldRecordReq(_message.Message):
    __slots__ = ("client_id", "index")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    index: int
    def __init__(self, client_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class DelWorldRecordRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id")
    class DelWorldRecordCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DelWorldRecordRsp.DelWorldRecordCode]
        INNER_ERR: _ClassVar[DelWorldRecordRsp.DelWorldRecordCode]
        NOT_REGISTER: _ClassVar[DelWorldRecordRsp.DelWorldRecordCode]
    SUCCESS: DelWorldRecordRsp.DelWorldRecordCode
    INNER_ERR: DelWorldRecordRsp.DelWorldRecordCode
    NOT_REGISTER: DelWorldRecordRsp.DelWorldRecordCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: DelWorldRecordRsp.DelWorldRecordCode
    msg: str
    client_id: str
    def __init__(self, code: _Optional[_Union[DelWorldRecordRsp.DelWorldRecordCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class GetChannelGroupInfoReq(_message.Message):
    __slots__ = ("client_id", "group_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    group_id: str
    def __init__(self, client_id: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class ChannelGroupInfo(_message.Message):
    __slots__ = ("channel_id", "member_count", "max_member_count")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    member_count: int
    max_member_count: int
    def __init__(self, channel_id: _Optional[str] = ..., member_count: _Optional[int] = ..., max_member_count: _Optional[int] = ...) -> None: ...

class GetChannelGroupInfoRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "group_id", "channel_list", "my_channel_id")
    class GetChannelGroupInfoCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetChannelGroupInfoRsp.GetChannelGroupInfoCode]
        INNER_ERR: _ClassVar[GetChannelGroupInfoRsp.GetChannelGroupInfoCode]
        NOT_REGISTER: _ClassVar[GetChannelGroupInfoRsp.GetChannelGroupInfoCode]
        GROUP_ID_INVALID: _ClassVar[GetChannelGroupInfoRsp.GetChannelGroupInfoCode]
    SUCCESS: GetChannelGroupInfoRsp.GetChannelGroupInfoCode
    INNER_ERR: GetChannelGroupInfoRsp.GetChannelGroupInfoCode
    NOT_REGISTER: GetChannelGroupInfoRsp.GetChannelGroupInfoCode
    GROUP_ID_INVALID: GetChannelGroupInfoRsp.GetChannelGroupInfoCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_LIST_FIELD_NUMBER: _ClassVar[int]
    MY_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    code: GetChannelGroupInfoRsp.GetChannelGroupInfoCode
    msg: str
    client_id: str
    group_id: str
    channel_list: _containers.RepeatedCompositeFieldContainer[ChannelGroupInfo]
    my_channel_id: str
    def __init__(self, code: _Optional[_Union[GetChannelGroupInfoRsp.GetChannelGroupInfoCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., group_id: _Optional[str] = ..., channel_list: _Optional[_Iterable[_Union[ChannelGroupInfo, _Mapping]]] = ..., my_channel_id: _Optional[str] = ...) -> None: ...

class ChannelGroupSwitchReq(_message.Message):
    __slots__ = ("client_id", "group_id", "channel_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    group_id: str
    channel_id: str
    def __init__(self, client_id: _Optional[str] = ..., group_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ChannelGroupSwitchRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "group_id", "channel_id", "channel_member_count")
    class ChannelGroupSwitchCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        INNER_ERR: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        NOT_REGISTER: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        GROUP_ID_INVALID: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        CHANNEL_ID_INVALID: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        ALREADY_IN_CHANNEL: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        LOCKED: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
        MEMBER_COUNT_LIMIT: _ClassVar[ChannelGroupSwitchRsp.ChannelGroupSwitchCode]
    SUCCESS: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    INNER_ERR: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    NOT_REGISTER: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    GROUP_ID_INVALID: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    CHANNEL_ID_INVALID: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    ALREADY_IN_CHANNEL: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    LOCKED: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    MEMBER_COUNT_LIMIT: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    code: ChannelGroupSwitchRsp.ChannelGroupSwitchCode
    msg: str
    client_id: str
    group_id: str
    channel_id: str
    channel_member_count: int
    def __init__(self, code: _Optional[_Union[ChannelGroupSwitchRsp.ChannelGroupSwitchCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., group_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., channel_member_count: _Optional[int] = ...) -> None: ...

class AddBlackListReq(_message.Message):
    __slots__ = ("client_id", "target_client_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    target_client_id: str
    def __init__(self, client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ...) -> None: ...

class AddBlackListRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "target_client_id")
    class AddBlackListCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[AddBlackListRsp.AddBlackListCode]
        INNER_ERROR: _ClassVar[AddBlackListRsp.AddBlackListCode]
        NOT_REGISTER: _ClassVar[AddBlackListRsp.AddBlackListCode]
        ALREADY_IN_LIST: _ClassVar[AddBlackListRsp.AddBlackListCode]
    SUCCESS: AddBlackListRsp.AddBlackListCode
    INNER_ERROR: AddBlackListRsp.AddBlackListCode
    NOT_REGISTER: AddBlackListRsp.AddBlackListCode
    ALREADY_IN_LIST: AddBlackListRsp.AddBlackListCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: AddBlackListRsp.AddBlackListCode
    msg: str
    client_id: str
    target_client_id: str
    def __init__(self, code: _Optional[_Union[AddBlackListRsp.AddBlackListCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ...) -> None: ...

class RemoveBlackListReq(_message.Message):
    __slots__ = ("client_id", "target_client_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    target_client_id: str
    def __init__(self, client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ...) -> None: ...

class RemoveBlackListRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "target_client_id")
    class RemoveBlackListCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[RemoveBlackListRsp.RemoveBlackListCode]
        INNER_ERROR: _ClassVar[RemoveBlackListRsp.RemoveBlackListCode]
        NOT_REGISTER: _ClassVar[RemoveBlackListRsp.RemoveBlackListCode]
        NOT_IN_LIST: _ClassVar[RemoveBlackListRsp.RemoveBlackListCode]
    SUCCESS: RemoveBlackListRsp.RemoveBlackListCode
    INNER_ERROR: RemoveBlackListRsp.RemoveBlackListCode
    NOT_REGISTER: RemoveBlackListRsp.RemoveBlackListCode
    NOT_IN_LIST: RemoveBlackListRsp.RemoveBlackListCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: RemoveBlackListRsp.RemoveBlackListCode
    msg: str
    client_id: str
    target_client_id: str
    def __init__(self, code: _Optional[_Union[RemoveBlackListRsp.RemoveBlackListCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., target_client_id: _Optional[str] = ...) -> None: ...

class GetBlackListReq(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class GetBlackListRsp(_message.Message):
    __slots__ = ("code", "msg", "black_list", "client_id")
    class GetBlackListCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetBlackListRsp.GetBlackListCode]
        INNER_ERROR: _ClassVar[GetBlackListRsp.GetBlackListCode]
        NOT_REGISTER: _ClassVar[GetBlackListRsp.GetBlackListCode]
    SUCCESS: GetBlackListRsp.GetBlackListCode
    INNER_ERROR: GetBlackListRsp.GetBlackListCode
    NOT_REGISTER: GetBlackListRsp.GetBlackListCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    BLACK_LIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: GetBlackListRsp.GetBlackListCode
    msg: str
    black_list: _containers.RepeatedScalarFieldContainer[str]
    client_id: str
    def __init__(self, code: _Optional[_Union[GetBlackListRsp.GetBlackListCode, str]] = ..., msg: _Optional[str] = ..., black_list: _Optional[_Iterable[str]] = ..., client_id: _Optional[str] = ...) -> None: ...

class SyncBlackListReq(_message.Message):
    __slots__ = ("client_id", "black_list")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BLACK_LIST_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    black_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., black_list: _Optional[_Iterable[str]] = ...) -> None: ...

class SyncBlackListRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id")
    class SyncBlackListCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[SyncBlackListRsp.SyncBlackListCode]
        INNER_ERROR: _ClassVar[SyncBlackListRsp.SyncBlackListCode]
        NOT_REGISTER: _ClassVar[SyncBlackListRsp.SyncBlackListCode]
    SUCCESS: SyncBlackListRsp.SyncBlackListCode
    INNER_ERROR: SyncBlackListRsp.SyncBlackListCode
    NOT_REGISTER: SyncBlackListRsp.SyncBlackListCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    code: SyncBlackListRsp.SyncBlackListCode
    msg: str
    client_id: str
    def __init__(self, code: _Optional[_Union[SyncBlackListRsp.SyncBlackListCode, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class GetPersonalBanInfoReq(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class GetPersonalBanInfoRsp(_message.Message):
    __slots__ = ("code", "msg", "client_id", "is_ban", "ban_time_out", "private_left_cd", "channel_left_cd", "world_left_cd")
    class GetPersonalBanInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[GetPersonalBanInfoRsp.GetPersonalBanInfo]
        NOT_REGISTER: _ClassVar[GetPersonalBanInfoRsp.GetPersonalBanInfo]
    SUCCESS: GetPersonalBanInfoRsp.GetPersonalBanInfo
    NOT_REGISTER: GetPersonalBanInfoRsp.GetPersonalBanInfo
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    BAN_TIME_OUT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_LEFT_CD_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_LEFT_CD_FIELD_NUMBER: _ClassVar[int]
    WORLD_LEFT_CD_FIELD_NUMBER: _ClassVar[int]
    code: GetPersonalBanInfoRsp.GetPersonalBanInfo
    msg: str
    client_id: str
    is_ban: bool
    ban_time_out: int
    private_left_cd: int
    channel_left_cd: int
    world_left_cd: int
    def __init__(self, code: _Optional[_Union[GetPersonalBanInfoRsp.GetPersonalBanInfo, str]] = ..., msg: _Optional[str] = ..., client_id: _Optional[str] = ..., is_ban: bool = ..., ban_time_out: _Optional[int] = ..., private_left_cd: _Optional[int] = ..., channel_left_cd: _Optional[int] = ..., world_left_cd: _Optional[int] = ...) -> None: ...
