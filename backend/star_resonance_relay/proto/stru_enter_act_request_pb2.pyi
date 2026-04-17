import stru_match_param_context_pb2 as _stru_match_param_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnterActRequest(_message.Message):
    __slots__ = ("act_id", "match_param_context")
    ACT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_PARAM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    act_id: int
    match_param_context: _stru_match_param_context_pb2.MatchParamContext
    def __init__(self, act_id: _Optional[int] = ..., match_param_context: _Optional[_Union[_stru_match_param_context_pb2.MatchParamContext, _Mapping]] = ...) -> None: ...
