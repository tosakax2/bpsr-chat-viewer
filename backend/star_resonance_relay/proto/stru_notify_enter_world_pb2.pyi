import stru_notify_enter_world_request_pb2 as _stru_notify_enter_world_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyEnterWorld(_message.Message):
    __slots__ = ("VRequest",)
    VREQUEST_FIELD_NUMBER: _ClassVar[int]
    VRequest: _stru_notify_enter_world_request_pb2.NotifyEnterWorldRequest
    def __init__(self, VRequest: _Optional[_Union[_stru_notify_enter_world_request_pb2.NotifyEnterWorldRequest, _Mapping]] = ...) -> None: ...
