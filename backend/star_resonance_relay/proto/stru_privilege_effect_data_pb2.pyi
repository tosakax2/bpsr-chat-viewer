from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrivilegeEffectData(_message.Message):
    __slots__ = ("normal_pass_id", "prime_pass_id", "normal_pass_id_map", "prime_pass_id_map")
    class NormalPassIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class PrimePassIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    NORMAL_PASS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIME_PASS_ID_FIELD_NUMBER: _ClassVar[int]
    NORMAL_PASS_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    PRIME_PASS_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    normal_pass_id: int
    prime_pass_id: int
    normal_pass_id_map: _containers.ScalarMap[int, bool]
    prime_pass_id_map: _containers.ScalarMap[int, bool]
    def __init__(self, normal_pass_id: _Optional[int] = ..., prime_pass_id: _Optional[int] = ..., normal_pass_id_map: _Optional[_Mapping[int, bool]] = ..., prime_pass_id_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...
