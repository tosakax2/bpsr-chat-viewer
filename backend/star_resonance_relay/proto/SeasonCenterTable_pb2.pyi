from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonCenterTableBase(_message.Message):
    __slots__ = ("function_id", "name_remark", "sort")
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_REMARK_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    function_id: int
    name_remark: str
    sort: int
    def __init__(self, function_id: _Optional[int] = ..., name_remark: _Optional[str] = ..., sort: _Optional[int] = ...) -> None: ...

class SeasonCenterTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonCenterTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonCenterTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonCenterTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonCenterTableBase]] = ...) -> None: ...
