import stru_union_official_pb2 as _stru_union_official_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyOfficialLimitUpdateRequest(_message.Message):
    __slots__ = ("officials",)
    class OfficialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_official_pb2.UnionOfficial
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_official_pb2.UnionOfficial, _Mapping]] = ...) -> None: ...
    OFFICIALS_FIELD_NUMBER: _ClassVar[int]
    officials: _containers.MessageMap[int, _stru_union_official_pb2.UnionOfficial]
    def __init__(self, officials: _Optional[_Mapping[int, _stru_union_official_pb2.UnionOfficial]] = ...) -> None: ...
