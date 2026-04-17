from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapEntityIconTableBase(_message.Message):
    __slots__ = ("id", "type", "sprite")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPRITE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    sprite: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., sprite: _Optional[str] = ...) -> None: ...

class MapEntityIconTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapEntityIconTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapEntityIconTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MapEntityIconTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MapEntityIconTableBase]] = ...) -> None: ...
