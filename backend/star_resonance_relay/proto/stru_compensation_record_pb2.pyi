import stru_compensation_data_pb2 as _stru_compensation_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompensationRecord(_message.Message):
    __slots__ = ("compensation_data",)
    class CompensationDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_compensation_data_pb2.CompensationData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_compensation_data_pb2.CompensationData, _Mapping]] = ...) -> None: ...
    COMPENSATION_DATA_FIELD_NUMBER: _ClassVar[int]
    compensation_data: _containers.MessageMap[int, _stru_compensation_data_pb2.CompensationData]
    def __init__(self, compensation_data: _Optional[_Mapping[int, _stru_compensation_data_pb2.CompensationData]] = ...) -> None: ...
