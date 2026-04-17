from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FasionWearRequest(_message.Message):
    __slots__ = ("fasion_type_to_fasion_id_map",)
    class FasionTypeToFasionIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FASION_TYPE_TO_FASION_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    fasion_type_to_fasion_id_map: _containers.ScalarMap[int, int]
    def __init__(self, fasion_type_to_fasion_id_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
