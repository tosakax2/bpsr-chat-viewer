from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlotCharactersTableBase(_message.Message):
    __slots__ = ("id", "plot_characters_name", "plot_characters_gender", "plot_characters_age", "plot_characters_content")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_NAME_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_GENDER_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_AGE_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    plot_characters_name: str
    plot_characters_gender: str
    plot_characters_age: str
    plot_characters_content: str
    def __init__(self, id: _Optional[int] = ..., plot_characters_name: _Optional[str] = ..., plot_characters_gender: _Optional[str] = ..., plot_characters_age: _Optional[str] = ..., plot_characters_content: _Optional[str] = ...) -> None: ...

class PlotCharactersTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PlotCharactersTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlotCharactersTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PlotCharactersTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PlotCharactersTableBase]] = ...) -> None: ...
