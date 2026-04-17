import stru_launch_param_pb2 as _stru_launch_param_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReconnectRequest(_message.Message):
    __slots__ = ("account_id", "token", "client_version", "client_resource_version", "os", "launch_param")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAM_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    token: str
    client_version: str
    client_resource_version: str
    os: int
    launch_param: _stru_launch_param_pb2.LaunchParam
    def __init__(self, account_id: _Optional[str] = ..., token: _Optional[str] = ..., client_version: _Optional[str] = ..., client_resource_version: _Optional[str] = ..., os: _Optional[int] = ..., launch_param: _Optional[_Union[_stru_launch_param_pb2.LaunchParam, _Mapping]] = ...) -> None: ...
