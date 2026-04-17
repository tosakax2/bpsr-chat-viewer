from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalShowRuleBase(_message.Message):
    __slots__ = ("id", "lang_area", "ymd", "ymd_to_ymd", "md", "md_to_md", "hms", "hm")
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_AREA_FIELD_NUMBER: _ClassVar[int]
    YMD_FIELD_NUMBER: _ClassVar[int]
    YMD_TO_YMD_FIELD_NUMBER: _ClassVar[int]
    MD_FIELD_NUMBER: _ClassVar[int]
    MD_TO_MD_FIELD_NUMBER: _ClassVar[int]
    HMS_FIELD_NUMBER: _ClassVar[int]
    HM_FIELD_NUMBER: _ClassVar[int]
    id: int
    lang_area: str
    ymd: str
    ymd_to_ymd: str
    md: str
    md_to_md: str
    hms: str
    hm: str
    def __init__(self, id: _Optional[int] = ..., lang_area: _Optional[str] = ..., ymd: _Optional[str] = ..., ymd_to_ymd: _Optional[str] = ..., md: _Optional[str] = ..., md_to_md: _Optional[str] = ..., hms: _Optional[str] = ..., hm: _Optional[str] = ...) -> None: ...

class LocalShowRuleMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocalShowRuleBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocalShowRuleBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, LocalShowRuleBase]
    def __init__(self, datas: _Optional[_Mapping[int, LocalShowRuleBase]] = ...) -> None: ...
