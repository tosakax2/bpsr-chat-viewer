import stru_scene_record_pb2 as _stru_scene_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatRecord(_message.Message):
    __slots__ = ("cnt", "group_cnts", "scene_records")
    class GroupCntsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SceneRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_scene_record_pb2.SceneRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_scene_record_pb2.SceneRecord, _Mapping]] = ...) -> None: ...
    CNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_CNTS_FIELD_NUMBER: _ClassVar[int]
    SCENE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    cnt: int
    group_cnts: _containers.ScalarMap[int, int]
    scene_records: _containers.MessageMap[int, _stru_scene_record_pb2.SceneRecord]
    def __init__(self, cnt: _Optional[int] = ..., group_cnts: _Optional[_Mapping[int, int]] = ..., scene_records: _Optional[_Mapping[int, _stru_scene_record_pb2.SceneRecord]] = ...) -> None: ...
