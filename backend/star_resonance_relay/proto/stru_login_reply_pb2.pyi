import stru_account_info_pb2 as _stru_account_info_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginReply(_message.Message):
    __slots__ = ("account_info", "begin_time", "protocol_version", "config_version", "time_zone", "is_privilege", "platform_config", "is_change_account", "install_channel_dis", "reg_channel_dis", "open_ace_check", "err_code")
    class PlatformConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_CHANGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    INSTALL_CHANNEL_DIS_FIELD_NUMBER: _ClassVar[int]
    REG_CHANNEL_DIS_FIELD_NUMBER: _ClassVar[int]
    OPEN_ACE_CHECK_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    account_info: _stru_account_info_pb2.AccountInfo
    begin_time: int
    protocol_version: str
    config_version: str
    time_zone: str
    is_privilege: bool
    platform_config: _containers.ScalarMap[int, str]
    is_change_account: bool
    install_channel_dis: int
    reg_channel_dis: int
    open_ace_check: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, account_info: _Optional[_Union[_stru_account_info_pb2.AccountInfo, _Mapping]] = ..., begin_time: _Optional[int] = ..., protocol_version: _Optional[str] = ..., config_version: _Optional[str] = ..., time_zone: _Optional[str] = ..., is_privilege: bool = ..., platform_config: _Optional[_Mapping[int, str]] = ..., is_change_account: bool = ..., install_channel_dis: _Optional[int] = ..., reg_channel_dis: _Optional[int] = ..., open_ace_check: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
