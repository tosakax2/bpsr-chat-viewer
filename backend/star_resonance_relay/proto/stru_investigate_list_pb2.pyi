import stru_investigate_data_pb2 as _stru_investigate_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigateList(_message.Message):
    __slots__ = ("investigate_map", "comp_investigate_map", "comp_reasoning_map")
    class InvestigateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_investigate_data_pb2.InvestigateData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_investigate_data_pb2.InvestigateData, _Mapping]] = ...) -> None: ...
    class CompInvestigateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    INVESTIGATE_MAP_FIELD_NUMBER: _ClassVar[int]
    COMP_INVESTIGATE_MAP_FIELD_NUMBER: _ClassVar[int]
    COMP_REASONING_MAP_FIELD_NUMBER: _ClassVar[int]
    investigate_map: _containers.MessageMap[int, _stru_investigate_data_pb2.InvestigateData]
    comp_investigate_map: _containers.ScalarMap[int, bool]
    comp_reasoning_map: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, investigate_map: _Optional[_Mapping[int, _stru_investigate_data_pb2.InvestigateData]] = ..., comp_investigate_map: _Optional[_Mapping[int, bool]] = ..., comp_reasoning_map: _Optional[_Iterable[int]] = ...) -> None: ...
