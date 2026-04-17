import stru_clutter_generation_record_pb2 as _stru_clutter_generation_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandClutterGenerationRecord(_message.Message):
    __slots__ = ("home_land_clutter_record",)
    class HomeLandClutterRecordEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_clutter_generation_record_pb2.ClutterGenerationRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_clutter_generation_record_pb2.ClutterGenerationRecord, _Mapping]] = ...) -> None: ...
    HOME_LAND_CLUTTER_RECORD_FIELD_NUMBER: _ClassVar[int]
    home_land_clutter_record: _containers.MessageMap[int, _stru_clutter_generation_record_pb2.ClutterGenerationRecord]
    def __init__(self, home_land_clutter_record: _Optional[_Mapping[int, _stru_clutter_generation_record_pb2.ClutterGenerationRecord]] = ...) -> None: ...
