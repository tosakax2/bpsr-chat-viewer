import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionTableBase(_message.Message):
    __slots__ = ("id", "name", "short_description", "description", "job", "icon", "icon_bg", "res_template_id", "buffs", "arrtrs", "profession_effect_id", "tips_description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ICON_BG_FIELD_NUMBER: _ClassVar[int]
    RES_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    ARRTRS_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIPS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    short_description: _table_basic_pb2.mlstring
    description: _table_basic_pb2.mlstring
    job: _table_basic_pb2.int_table
    icon: str
    icon_bg: str
    res_template_id: int
    buffs: _table_basic_pb2.int_array
    arrtrs: _table_basic_pb2.int_table
    profession_effect_id: _table_basic_pb2.int_array
    tips_description: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., short_description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., job: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., icon: _Optional[str] = ..., icon_bg: _Optional[str] = ..., res_template_id: _Optional[int] = ..., buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., arrtrs: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., profession_effect_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., tips_description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class ProfessionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfessionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfessionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfessionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfessionTableBase]] = ...) -> None: ...
