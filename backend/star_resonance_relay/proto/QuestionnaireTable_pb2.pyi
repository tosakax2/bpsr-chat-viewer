import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionnaireTableBase(_message.Message):
    __slots__ = ("id", "name", "link", "level_limit", "day_limit", "mail_id", "award")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    LEVEL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DAY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAIL_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    link: str
    level_limit: int
    day_limit: int
    mail_id: int
    award: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., link: _Optional[str] = ..., level_limit: _Optional[int] = ..., day_limit: _Optional[int] = ..., mail_id: _Optional[int] = ..., award: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class QuestionnaireTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QuestionnaireTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QuestionnaireTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QuestionnaireTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QuestionnaireTableBase]] = ...) -> None: ...
