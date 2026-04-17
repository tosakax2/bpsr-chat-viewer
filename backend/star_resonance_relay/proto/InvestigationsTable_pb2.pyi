import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigationsTableBase(_message.Message):
    __slots__ = ("id", "investigation_theme", "unlock_condition", "investigation_step", "completion_conditions", "theme_introduction", "iocked_tips", "theme_pic", "guarantee")
    ID_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_THEME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONDITION_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_STEP_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    THEME_INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    IOCKED_TIPS_FIELD_NUMBER: _ClassVar[int]
    THEME_PIC_FIELD_NUMBER: _ClassVar[int]
    GUARANTEE_FIELD_NUMBER: _ClassVar[int]
    id: int
    investigation_theme: _table_basic_pb2.mlstring
    unlock_condition: _table_basic_pb2.int_table
    investigation_step: _table_basic_pb2.int_array
    completion_conditions: _table_basic_pb2.int_table
    theme_introduction: _table_basic_pb2.mlstring
    iocked_tips: _table_basic_pb2.mlstring
    theme_pic: str
    guarantee: int
    def __init__(self, id: _Optional[int] = ..., investigation_theme: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., unlock_condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., investigation_step: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., completion_conditions: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., theme_introduction: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., iocked_tips: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., theme_pic: _Optional[str] = ..., guarantee: _Optional[int] = ...) -> None: ...

class InvestigationsTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InvestigationsTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvestigationsTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InvestigationsTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InvestigationsTableBase]] = ...) -> None: ...
