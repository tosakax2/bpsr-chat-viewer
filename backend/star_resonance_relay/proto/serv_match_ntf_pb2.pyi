import stru_cancel_match_result_ntf_request_pb2 as _stru_cancel_match_result_ntf_request_pb2
import stru_enter_match_result_ntf_request_pb2 as _stru_enter_match_result_ntf_request_pb2
import stru_match_ready_status_ntf_request_pb2 as _stru_match_ready_status_ntf_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchNtf(_message.Message):
    __slots__ = ()
    class EnterMatchResultNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_enter_match_result_ntf_request_pb2.EnterMatchResultNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_enter_match_result_ntf_request_pb2.EnterMatchResultNtfRequest, _Mapping]] = ...) -> None: ...
    class CancelMatchResultNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_cancel_match_result_ntf_request_pb2.CancelMatchResultNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_cancel_match_result_ntf_request_pb2.CancelMatchResultNtfRequest, _Mapping]] = ...) -> None: ...
    class MatchReadyStatusNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_match_ready_status_ntf_request_pb2.MatchReadyStatusNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_match_ready_status_ntf_request_pb2.MatchReadyStatusNtfRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
