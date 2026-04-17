import stru_rogue_buff_data_pb2 as _stru_rogue_buff_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RogueData(_message.Message):
    __slots__ = ("buffs", "seasons")
    class BuffsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_rogue_buff_data_pb2.RogueBuffData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_rogue_buff_data_pb2.RogueBuffData, _Mapping]] = ...) -> None: ...
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    SEASONS_FIELD_NUMBER: _ClassVar[int]
    buffs: _containers.MessageMap[int, _stru_rogue_buff_data_pb2.RogueBuffData]
    seasons: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, buffs: _Optional[_Mapping[int, _stru_rogue_buff_data_pb2.RogueBuffData]] = ..., seasons: _Optional[_Iterable[int]] = ...) -> None: ...
