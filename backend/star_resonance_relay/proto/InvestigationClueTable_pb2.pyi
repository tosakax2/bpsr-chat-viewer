import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigationClueTableBase(_message.Message):
    __slots__ = ("id", "sort", "unlock_condition", "clue", "answer", "tips", "tap_bubble", "tap_bubble_action", "unlocked_bubble", "unlocked_bubble_action")
    ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONDITION_FIELD_NUMBER: _ClassVar[int]
    CLUE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    TIPS_FIELD_NUMBER: _ClassVar[int]
    TAP_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    TAP_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_BUBBLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    sort: int
    unlock_condition: _table_basic_pb2.int_table
    clue: _table_basic_pb2.mlstring
    answer: _table_basic_pb2.mlstring_array
    tips: _table_basic_pb2.mlstring
    tap_bubble: _table_basic_pb2.mlstring_array
    tap_bubble_action: _table_basic_pb2.int_array
    unlocked_bubble: _table_basic_pb2.mlstring
    unlocked_bubble_action: int
    def __init__(self, id: _Optional[int] = ..., sort: _Optional[int] = ..., unlock_condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., clue: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., answer: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., tips: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., tap_bubble: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., tap_bubble_action: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., unlocked_bubble: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., unlocked_bubble_action: _Optional[int] = ...) -> None: ...

class InvestigationClueTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InvestigationClueTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvestigationClueTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InvestigationClueTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InvestigationClueTableBase]] = ...) -> None: ...
