from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneResourceTableBase(_message.Message):
    __slots__ = ("id", "scene_load_type", "scene_file")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_LOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_FILE_FIELD_NUMBER: _ClassVar[int]
    id: int
    scene_load_type: int
    scene_file: str
    def __init__(self, id: _Optional[int] = ..., scene_load_type: _Optional[int] = ..., scene_file: _Optional[str] = ...) -> None: ...

class SceneResourceTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneResourceTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneResourceTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneResourceTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneResourceTableBase]] = ...) -> None: ...
