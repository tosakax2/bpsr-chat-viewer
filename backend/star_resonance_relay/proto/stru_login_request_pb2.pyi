import stru_device_info_pb2 as _stru_device_info_pb2
import stru_launch_param_pb2 as _stru_launch_param_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("open_id", "token", "sdk_type", "channel_id", "os", "platform_type", "device_info", "client_version", "protocol_version", "config_version", "area_id", "i_os_ad_service_token", "pay_ext_data", "client_resource_version", "launch_param", "area_id_token", "is_cloud_game", "distinct_id", "bound_providers", "language", "gclid")
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SDK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    I_OS_AD_SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAY_EXT_DATA_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAM_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_GAME_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_ID_FIELD_NUMBER: _ClassVar[int]
    BOUND_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GCLID_FIELD_NUMBER: _ClassVar[int]
    open_id: str
    token: str
    sdk_type: int
    channel_id: int
    os: int
    platform_type: int
    device_info: _stru_device_info_pb2.DeviceInfo
    client_version: str
    protocol_version: str
    config_version: str
    area_id: int
    i_os_ad_service_token: str
    pay_ext_data: str
    client_resource_version: str
    launch_param: _stru_launch_param_pb2.LaunchParam
    area_id_token: str
    is_cloud_game: bool
    distinct_id: str
    bound_providers: _containers.RepeatedScalarFieldContainer[str]
    language: int
    gclid: str
    def __init__(self, open_id: _Optional[str] = ..., token: _Optional[str] = ..., sdk_type: _Optional[int] = ..., channel_id: _Optional[int] = ..., os: _Optional[int] = ..., platform_type: _Optional[int] = ..., device_info: _Optional[_Union[_stru_device_info_pb2.DeviceInfo, _Mapping]] = ..., client_version: _Optional[str] = ..., protocol_version: _Optional[str] = ..., config_version: _Optional[str] = ..., area_id: _Optional[int] = ..., i_os_ad_service_token: _Optional[str] = ..., pay_ext_data: _Optional[str] = ..., client_resource_version: _Optional[str] = ..., launch_param: _Optional[_Union[_stru_launch_param_pb2.LaunchParam, _Mapping]] = ..., area_id_token: _Optional[str] = ..., is_cloud_game: bool = ..., distinct_id: _Optional[str] = ..., bound_providers: _Optional[_Iterable[str]] = ..., language: _Optional[int] = ..., gclid: _Optional[str] = ...) -> None: ...
