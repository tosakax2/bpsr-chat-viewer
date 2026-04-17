from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumeTypeTableBase(_message.Message):
    __slots__ = ("id", "note", "invalid", "time_limit", "exclusive")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    note: str
    invalid: int
    time_limit: int
    exclusive: int
    def __init__(self, id: _Optional[int] = ..., note: _Optional[str] = ..., invalid: _Optional[int] = ..., time_limit: _Optional[int] = ..., exclusive: _Optional[int] = ...) -> None: ...

class ConsumeTypeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ConsumeTypeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ConsumeTypeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ConsumeTypeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ConsumeTypeTableBase]] = ...) -> None: ...
