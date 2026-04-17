from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmoClipsTableBase(_message.Message):
    __slots__ = ("id", "soure_key", "layer", "address")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURE_KEY_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    soure_key: str
    layer: int
    address: str
    def __init__(self, id: _Optional[int] = ..., soure_key: _Optional[str] = ..., layer: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class EmoClipsTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EmoClipsTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EmoClipsTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EmoClipsTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EmoClipsTableBase]] = ...) -> None: ...
