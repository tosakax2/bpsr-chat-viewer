import stru_fish_record_pb2 as _stru_fish_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishSocialData(_message.Message):
    __slots__ = ("fish_records",)
    class FishRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fish_record_pb2.FishRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fish_record_pb2.FishRecord, _Mapping]] = ...) -> None: ...
    FISH_RECORDS_FIELD_NUMBER: _ClassVar[int]
    fish_records: _containers.MessageMap[int, _stru_fish_record_pb2.FishRecord]
    def __init__(self, fish_records: _Optional[_Mapping[int, _stru_fish_record_pb2.FishRecord]] = ...) -> None: ...
