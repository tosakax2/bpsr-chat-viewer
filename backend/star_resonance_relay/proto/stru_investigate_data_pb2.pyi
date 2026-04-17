import stru_investigate_step_pb2 as _stru_investigate_step_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigateData(_message.Message):
    __slots__ = ("id", "step_ids")
    class StepIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_investigate_step_pb2.InvestigateStep
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_investigate_step_pb2.InvestigateStep, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STEP_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    step_ids: _containers.MessageMap[int, _stru_investigate_step_pb2.InvestigateStep]
    def __init__(self, id: _Optional[int] = ..., step_ids: _Optional[_Mapping[int, _stru_investigate_step_pb2.InvestigateStep]] = ...) -> None: ...
