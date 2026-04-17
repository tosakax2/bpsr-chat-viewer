import stru_get_face_up_token_ntf_request_pb2 as _stru_get_face_up_token_ntf_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcCharactorNtf(_message.Message):
    __slots__ = ()
    class GetFaceUpTokenNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_face_up_token_ntf_request_pb2.GetFaceUpTokenNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_face_up_token_ntf_request_pb2.GetFaceUpTokenNtfRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
