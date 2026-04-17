import stru_reputation_info_pb2 as _stru_reputation_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReputationList(_message.Message):
    __slots__ = ("reputation_map",)
    class ReputationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_reputation_info_pb2.ReputationInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_reputation_info_pb2.ReputationInfo, _Mapping]] = ...) -> None: ...
    REPUTATION_MAP_FIELD_NUMBER: _ClassVar[int]
    reputation_map: _containers.MessageMap[int, _stru_reputation_info_pb2.ReputationInfo]
    def __init__(self, reputation_map: _Optional[_Mapping[int, _stru_reputation_info_pb2.ReputationInfo]] = ...) -> None: ...
