import stru_energy_info_pb2 as _stru_energy_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnergyItem(_message.Message):
    __slots__ = ("energy_limit", "extra_energy_limit", "energy_info")
    class EnergyInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_energy_info_pb2.EnergyInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_energy_info_pb2.EnergyInfo, _Mapping]] = ...) -> None: ...
    ENERGY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ENERGY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENERGY_INFO_FIELD_NUMBER: _ClassVar[int]
    energy_limit: int
    extra_energy_limit: int
    energy_info: _containers.MessageMap[int, _stru_energy_info_pb2.EnergyInfo]
    def __init__(self, energy_limit: _Optional[int] = ..., extra_energy_limit: _Optional[int] = ..., energy_info: _Optional[_Mapping[int, _stru_energy_info_pb2.EnergyInfo]] = ...) -> None: ...
