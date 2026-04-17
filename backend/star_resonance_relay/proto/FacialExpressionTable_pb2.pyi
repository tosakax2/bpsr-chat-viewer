from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacialExpressionTableBase(_message.Message):
    __slots__ = ("id", "facial_name", "remark", "path")
    ID_FIELD_NUMBER: _ClassVar[int]
    FACIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    facial_name: str
    remark: str
    path: str
    def __init__(self, id: _Optional[int] = ..., facial_name: _Optional[str] = ..., remark: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class FacialExpressionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FacialExpressionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FacialExpressionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FacialExpressionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FacialExpressionTableBase]] = ...) -> None: ...
