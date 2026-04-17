from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BugReportConfigTableBase(_message.Message):
    __slots__ = ("id", "data_type", "data_index", "data_value", "data_value2", "desc")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_INDEX_FIELD_NUMBER: _ClassVar[int]
    DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_VALUE2_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    id: int
    data_type: int
    data_index: int
    data_value: str
    data_value2: str
    desc: str
    def __init__(self, id: _Optional[int] = ..., data_type: _Optional[int] = ..., data_index: _Optional[int] = ..., data_value: _Optional[str] = ..., data_value2: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...

class BugReportConfigTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BugReportConfigTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BugReportConfigTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BugReportConfigTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BugReportConfigTableBase]] = ...) -> None: ...
