from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerTableBase(_message.Message):
    __slots__ = ("id", "starttime", "endtime", "type", "offset", "duration", "command")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    id: int
    starttime: str
    endtime: str
    type: int
    offset: str
    duration: str
    command: str
    def __init__(self, id: _Optional[int] = ..., starttime: _Optional[str] = ..., endtime: _Optional[str] = ..., type: _Optional[int] = ..., offset: _Optional[str] = ..., duration: _Optional[str] = ..., command: _Optional[str] = ...) -> None: ...

class TimerTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TimerTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TimerTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TimerTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TimerTableBase]] = ...) -> None: ...
