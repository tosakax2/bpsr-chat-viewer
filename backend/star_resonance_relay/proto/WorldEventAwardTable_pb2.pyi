from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldEventAwardTableBase(_message.Message):
    __slots__ = ("score", "award")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    score: int
    award: int
    def __init__(self, score: _Optional[int] = ..., award: _Optional[int] = ...) -> None: ...

class WorldEventAwardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WorldEventAwardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WorldEventAwardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WorldEventAwardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WorldEventAwardTableBase]] = ...) -> None: ...
