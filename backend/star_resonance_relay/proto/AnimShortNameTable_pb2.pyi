from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnimShortNameTableBase(_message.Message):
    __slots__ = ("id", "name_design", "anim_short_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_DESIGN_FIELD_NUMBER: _ClassVar[int]
    ANIM_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name_design: str
    anim_short_name: str
    def __init__(self, id: _Optional[int] = ..., name_design: _Optional[str] = ..., anim_short_name: _Optional[str] = ...) -> None: ...

class AnimShortNameTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AnimShortNameTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AnimShortNameTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AnimShortNameTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AnimShortNameTableBase]] = ...) -> None: ...
