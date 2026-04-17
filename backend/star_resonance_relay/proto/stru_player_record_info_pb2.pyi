import stru_player_record_single_pb2 as _stru_player_record_single_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRecordInfo(_message.Message):
    __slots__ = ("player_records",)
    class PlayerRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_record_single_pb2.PlayerRecordSingle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_record_single_pb2.PlayerRecordSingle, _Mapping]] = ...) -> None: ...
    PLAYER_RECORDS_FIELD_NUMBER: _ClassVar[int]
    player_records: _containers.MessageMap[int, _stru_player_record_single_pb2.PlayerRecordSingle]
    def __init__(self, player_records: _Optional[_Mapping[int, _stru_player_record_single_pb2.PlayerRecordSingle]] = ...) -> None: ...
