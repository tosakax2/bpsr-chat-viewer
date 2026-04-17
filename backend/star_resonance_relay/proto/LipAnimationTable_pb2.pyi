from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LipAnimationTableBase(_message.Message):
    __slots__ = ("id", "comment", "vowela", "vowelo", "vowele", "voweli", "vowelu")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    VOWELA_FIELD_NUMBER: _ClassVar[int]
    VOWELO_FIELD_NUMBER: _ClassVar[int]
    VOWELE_FIELD_NUMBER: _ClassVar[int]
    VOWELI_FIELD_NUMBER: _ClassVar[int]
    VOWELU_FIELD_NUMBER: _ClassVar[int]
    id: int
    comment: str
    vowela: str
    vowelo: str
    vowele: str
    voweli: str
    vowelu: str
    def __init__(self, id: _Optional[int] = ..., comment: _Optional[str] = ..., vowela: _Optional[str] = ..., vowelo: _Optional[str] = ..., vowele: _Optional[str] = ..., voweli: _Optional[str] = ..., vowelu: _Optional[str] = ...) -> None: ...

class LipAnimationTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LipAnimationTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LipAnimationTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, LipAnimationTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, LipAnimationTableBase]] = ...) -> None: ...
