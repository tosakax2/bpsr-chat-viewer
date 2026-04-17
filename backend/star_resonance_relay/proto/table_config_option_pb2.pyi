from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageTable(_message.Message):
    __slots__ = ("msg_type", "pbs_path")
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    PBS_PATH_FIELD_NUMBER: _ClassVar[int]
    msg_type: str
    pbs_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, msg_type: _Optional[str] = ..., pbs_path: _Optional[_Iterable[str]] = ...) -> None: ...

class SecondaryKey(_message.Message):
    __slots__ = ("id", "index")
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    id: int
    index: int
    def __init__(self, id: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class TableConfigFieldOption(_message.Message):
    __slots__ = ("primary_key", "non_unique", "secondary_keys")
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NON_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    primary_key: bool
    non_unique: bool
    secondary_keys: _containers.RepeatedCompositeFieldContainer[SecondaryKey]
    def __init__(self, primary_key: bool = ..., non_unique: bool = ..., secondary_keys: _Optional[_Iterable[_Union[SecondaryKey, _Mapping]]] = ...) -> None: ...
