from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WindTunnelTableBase(_message.Message):
    __slots__ = ("id", "name", "effect_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    effect_path: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., effect_path: _Optional[str] = ...) -> None: ...

class WindTunnelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WindTunnelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WindTunnelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WindTunnelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WindTunnelTableBase]] = ...) -> None: ...
