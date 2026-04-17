import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetKeyboardContrastTableBase(_message.Message):
    __slots__ = ("id", "keyboard", "show_type", "image_way")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    keyboard: _table_basic_pb2.mlstring
    show_type: int
    image_way: str
    def __init__(self, id: _Optional[int] = ..., keyboard: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., show_type: _Optional[int] = ..., image_way: _Optional[str] = ...) -> None: ...

class SetKeyboardContrastTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SetKeyboardContrastTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SetKeyboardContrastTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SetKeyboardContrastTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SetKeyboardContrastTableBase]] = ...) -> None: ...
