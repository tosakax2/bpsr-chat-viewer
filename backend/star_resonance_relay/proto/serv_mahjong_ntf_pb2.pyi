import stru_notify_mahjong_action_request_pb2 as _stru_notify_mahjong_action_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongNtf(_message.Message):
    __slots__ = ()
    class NotifyMahjongAction(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_mahjong_action_request_pb2.NotifyMahjongActionRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_mahjong_action_request_pb2.NotifyMahjongActionRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
