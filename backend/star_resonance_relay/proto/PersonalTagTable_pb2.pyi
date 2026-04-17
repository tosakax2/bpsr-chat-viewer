from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalTagTableBase(_message.Message):
    __slots__ = ("id", "tag_name", "tag_icon", "type", "sequence")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    tag_name: str
    tag_icon: str
    type: int
    sequence: int
    def __init__(self, id: _Optional[int] = ..., tag_name: _Optional[str] = ..., tag_icon: _Optional[str] = ..., type: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...

class PersonalTagTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PersonalTagTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PersonalTagTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PersonalTagTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PersonalTagTableBase]] = ...) -> None: ...
