from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDTAGSpecialLinkTableBase(_message.Message):
    __slots__ = ("id", "note", "note_type", "node_id", "target_node_type", "target_node_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    note: str
    note_type: int
    node_id: int
    target_node_type: int
    target_node_id: int
    def __init__(self, id: _Optional[int] = ..., note: _Optional[str] = ..., note_type: _Optional[int] = ..., node_id: _Optional[int] = ..., target_node_type: _Optional[int] = ..., target_node_id: _Optional[int] = ...) -> None: ...

class BDTAGSpecialLinkTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BDTAGSpecialLinkTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BDTAGSpecialLinkTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BDTAGSpecialLinkTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BDTAGSpecialLinkTableBase]] = ...) -> None: ...
