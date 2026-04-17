from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGTableBase(_message.Message):
    __slots__ = ("id", "cg_name", "res_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    CG_NAME_FIELD_NUMBER: _ClassVar[int]
    RES_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    cg_name: str
    res_path: str
    def __init__(self, id: _Optional[int] = ..., cg_name: _Optional[str] = ..., res_path: _Optional[str] = ...) -> None: ...

class CGTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CGTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CGTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CGTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CGTableBase]] = ...) -> None: ...
