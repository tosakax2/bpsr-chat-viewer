import stru_answer_list_pb2 as _stru_answer_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigateStep(_message.Message):
    __slots__ = ("clues", "reasoning_map")
    class ReasoningMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_answer_list_pb2.AnswerList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_answer_list_pb2.AnswerList, _Mapping]] = ...) -> None: ...
    CLUES_FIELD_NUMBER: _ClassVar[int]
    REASONING_MAP_FIELD_NUMBER: _ClassVar[int]
    clues: _containers.RepeatedScalarFieldContainer[int]
    reasoning_map: _containers.MessageMap[int, _stru_answer_list_pb2.AnswerList]
    def __init__(self, clues: _Optional[_Iterable[int]] = ..., reasoning_map: _Optional[_Mapping[int, _stru_answer_list_pb2.AnswerList]] = ...) -> None: ...
