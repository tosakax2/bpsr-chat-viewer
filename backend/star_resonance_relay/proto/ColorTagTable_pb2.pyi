from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColorTagTableBase(_message.Message):
    __slots__ = ("id", "color_tag", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_TAG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    color_tag: str
    color: str
    def __init__(self, id: _Optional[int] = ..., color_tag: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class ColorTagTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ColorTagTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ColorTagTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ColorTagTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ColorTagTableBase]] = ...) -> None: ...
