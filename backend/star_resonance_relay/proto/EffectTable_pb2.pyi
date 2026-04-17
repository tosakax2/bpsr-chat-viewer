from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EffectTableBase(_message.Message):
    __slots__ = ("id", "comment", "path", "play_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PLAY_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    comment: str
    path: str
    play_time: float
    def __init__(self, id: _Optional[int] = ..., comment: _Optional[str] = ..., path: _Optional[str] = ..., play_time: _Optional[float] = ...) -> None: ...

class EffectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EffectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EffectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EffectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EffectTableBase]] = ...) -> None: ...
