from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayNameTableBase(_message.Message):
    __slots__ = ("id", "name_cn", "name_en", "name_jp", "name_kr", "sex")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_CN_FIELD_NUMBER: _ClassVar[int]
    NAME_EN_FIELD_NUMBER: _ClassVar[int]
    NAME_JP_FIELD_NUMBER: _ClassVar[int]
    NAME_KR_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    id: int
    name_cn: str
    name_en: str
    name_jp: str
    name_kr: str
    sex: int
    def __init__(self, id: _Optional[int] = ..., name_cn: _Optional[str] = ..., name_en: _Optional[str] = ..., name_jp: _Optional[str] = ..., name_kr: _Optional[str] = ..., sex: _Optional[int] = ...) -> None: ...

class PlayNameTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PlayNameTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlayNameTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PlayNameTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PlayNameTableBase]] = ...) -> None: ...
