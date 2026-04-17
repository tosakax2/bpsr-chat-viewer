import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigationStepTableBase(_message.Message):
    __slots__ = ("id", "clue", "inference_step", "conclusion", "conclusion_tips", "conclusion_bubble", "conclusion_action", "iocked_bubble", "iocked_bubble_action", "review_bubble", "review_bubble_action", "quick_reasoning")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLUE_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_STEP_FIELD_NUMBER: _ClassVar[int]
    CONCLUSION_FIELD_NUMBER: _ClassVar[int]
    CONCLUSION_TIPS_FIELD_NUMBER: _ClassVar[int]
    CONCLUSION_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    CONCLUSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    IOCKED_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    IOCKED_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    REVIEW_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    QUICK_REASONING_FIELD_NUMBER: _ClassVar[int]
    id: int
    clue: _table_basic_pb2.int_array
    inference_step: _table_basic_pb2.int_array
    conclusion: _table_basic_pb2.mlstring
    conclusion_tips: _table_basic_pb2.mlstring
    conclusion_bubble: _table_basic_pb2.mlstring
    conclusion_action: int
    iocked_bubble: _table_basic_pb2.mlstring_array
    iocked_bubble_action: _table_basic_pb2.int_array
    review_bubble: _table_basic_pb2.mlstring_array
    review_bubble_action: _table_basic_pb2.int_array
    quick_reasoning: bool
    def __init__(self, id: _Optional[int] = ..., clue: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., inference_step: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., conclusion: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., conclusion_tips: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., conclusion_bubble: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., conclusion_action: _Optional[int] = ..., iocked_bubble: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., iocked_bubble_action: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., review_bubble: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., review_bubble_action: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., quick_reasoning: bool = ...) -> None: ...

class InvestigationStepTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InvestigationStepTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvestigationStepTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InvestigationStepTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InvestigationStepTableBase]] = ...) -> None: ...
