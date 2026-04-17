import stru_sign_status_pb2 as _stru_sign_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignStatusList(_message.Message):
    __slots__ = ("sign_status_data",)
    class SignStatusDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_sign_status_pb2.SignStatus
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_sign_status_pb2.SignStatus, _Mapping]] = ...) -> None: ...
    SIGN_STATUS_DATA_FIELD_NUMBER: _ClassVar[int]
    sign_status_data: _containers.MessageMap[int, _stru_sign_status_pb2.SignStatus]
    def __init__(self, sign_status_data: _Optional[_Mapping[int, _stru_sign_status_pb2.SignStatus]] = ...) -> None: ...
