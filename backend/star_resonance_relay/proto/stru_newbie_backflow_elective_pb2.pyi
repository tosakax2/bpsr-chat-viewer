import stru_newbie_backflow_target_data_pb2 as _stru_newbie_backflow_target_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewbieBackflowElective(_message.Message):
    __slots__ = ("target_map", "progress_award_state")
    class TargetMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_newbie_backflow_target_data_pb2.NewbieBackflowTargetData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_newbie_backflow_target_data_pb2.NewbieBackflowTargetData, _Mapping]] = ...) -> None: ...
    TARGET_MAP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_AWARD_STATE_FIELD_NUMBER: _ClassVar[int]
    target_map: _containers.MessageMap[int, _stru_newbie_backflow_target_data_pb2.NewbieBackflowTargetData]
    progress_award_state: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target_map: _Optional[_Mapping[int, _stru_newbie_backflow_target_data_pb2.NewbieBackflowTargetData]] = ..., progress_award_state: _Optional[_Iterable[int]] = ...) -> None: ...
