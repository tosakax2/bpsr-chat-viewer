import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailTableBase(_message.Message):
    __slots__ = ("id", "title", "npc_id", "npc_name", "content", "award_id", "mail_group_content", "expire_time", "mail_type", "important", "limit_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    MAIL_GROUP_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: _table_basic_pb2.mlstring
    npc_id: int
    npc_name: _table_basic_pb2.mlstring
    content: _table_basic_pb2.mlstring
    award_id: int
    mail_group_content: str
    expire_time: int
    mail_type: int
    important: int
    limit_type: int
    def __init__(self, id: _Optional[int] = ..., title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., npc_id: _Optional[int] = ..., npc_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., award_id: _Optional[int] = ..., mail_group_content: _Optional[str] = ..., expire_time: _Optional[int] = ..., mail_type: _Optional[int] = ..., important: _Optional[int] = ..., limit_type: _Optional[int] = ...) -> None: ...

class MailTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MailTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MailTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MailTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MailTableBase]] = ...) -> None: ...
