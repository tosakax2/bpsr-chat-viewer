from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BugReportFilterTableBase(_message.Message):
    __slots__ = ("id", "filter_str", "match_str", "desc")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_STR_FIELD_NUMBER: _ClassVar[int]
    MATCH_STR_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    id: int
    filter_str: str
    match_str: str
    desc: str
    def __init__(self, id: _Optional[int] = ..., filter_str: _Optional[str] = ..., match_str: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...

class BugReportFilterTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BugReportFilterTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BugReportFilterTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BugReportFilterTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BugReportFilterTableBase]] = ...) -> None: ...
