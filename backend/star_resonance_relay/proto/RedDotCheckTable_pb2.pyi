from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedDotCheckTableBase(_message.Message):
    __slots__ = ("id", "check_method_name", "file_name", "function_id", "check_method_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_METHOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    check_method_name: str
    file_name: str
    function_id: int
    check_method_type: int
    def __init__(self, id: _Optional[int] = ..., check_method_name: _Optional[str] = ..., file_name: _Optional[str] = ..., function_id: _Optional[int] = ..., check_method_type: _Optional[int] = ...) -> None: ...

class RedDotCheckTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RedDotCheckTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RedDotCheckTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, RedDotCheckTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, RedDotCheckTableBase]] = ...) -> None: ...
