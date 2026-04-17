import stru_notify_instruction_info_request_pb2 as _stru_notify_instruction_info_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldLoginNtf(_message.Message):
    __slots__ = ()
    class NotifyInstructionInfo(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_notify_instruction_info_request_pb2.NotifyInstructionInfoRequest
        def __init__(self, v_info: _Optional[_Union[_stru_notify_instruction_info_request_pb2.NotifyInstructionInfoRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
