import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InferenceStepTableBase(_message.Message):
    __slots__ = ("id", "question", "answer", "question_bubble", "question_bubble_action", "wrong_bubble", "wrong_bubble_action")
    ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    QUESTION_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    WRONG_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    WRONG_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    question: _table_basic_pb2.mlstring
    answer: _table_basic_pb2.int_array
    question_bubble: _table_basic_pb2.mlstring
    question_bubble_action: int
    wrong_bubble: _table_basic_pb2.mlstring_array
    wrong_bubble_action: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., question: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., answer: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., question_bubble: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., question_bubble_action: _Optional[int] = ..., wrong_bubble: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., wrong_bubble_action: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class InferenceStepTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InferenceStepTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InferenceStepTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InferenceStepTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InferenceStepTableBase]] = ...) -> None: ...
