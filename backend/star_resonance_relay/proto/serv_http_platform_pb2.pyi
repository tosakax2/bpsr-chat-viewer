import stru_text_check_reply_pb2 as _stru_text_check_reply_pb2
import stru_text_check_request_pb2 as _stru_text_check_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpPlatform(_message.Message):
    __slots__ = ()
    class TextCheck_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_text_check_reply_pb2.TextCheckReply
        def __init__(self, ret: _Optional[_Union[_stru_text_check_reply_pb2.TextCheckReply, _Mapping]] = ...) -> None: ...
    class TextCheck(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_text_check_request_pb2.TextCheckRequest
        def __init__(self, v_request: _Optional[_Union[_stru_text_check_request_pb2.TextCheckRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
