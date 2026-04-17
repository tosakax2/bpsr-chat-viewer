import stru_unlock_proficiency_pb2 as _stru_unlock_proficiency_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LevelProficiency(_message.Message):
    __slots__ = ("using_proficiency_map", "unlock_proficiency_map")
    class UsingProficiencyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class UnlockProficiencyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_unlock_proficiency_pb2.UnlockProficiency
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_unlock_proficiency_pb2.UnlockProficiency, _Mapping]] = ...) -> None: ...
    USING_PROFICIENCY_MAP_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_PROFICIENCY_MAP_FIELD_NUMBER: _ClassVar[int]
    using_proficiency_map: _containers.ScalarMap[int, int]
    unlock_proficiency_map: _containers.MessageMap[int, _stru_unlock_proficiency_pb2.UnlockProficiency]
    def __init__(self, using_proficiency_map: _Optional[_Mapping[int, int]] = ..., unlock_proficiency_map: _Optional[_Mapping[int, _stru_unlock_proficiency_pb2.UnlockProficiency]] = ...) -> None: ...
