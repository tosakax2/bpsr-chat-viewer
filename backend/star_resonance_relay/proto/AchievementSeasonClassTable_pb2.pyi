import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementSeasonClassTableBase(_message.Message):
    __slots__ = ("id", "class_name", "class_background", "class_des", "entry_list", "sort_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    CLASS_DES_FIELD_NUMBER: _ClassVar[int]
    ENTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    class_name: _table_basic_pb2.mlstring
    class_background: str
    class_des: str
    entry_list: _table_basic_pb2.int_array
    sort_id: int
    def __init__(self, id: _Optional[int] = ..., class_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., class_background: _Optional[str] = ..., class_des: _Optional[str] = ..., entry_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., sort_id: _Optional[int] = ...) -> None: ...

class AchievementSeasonClassTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AchievementSeasonClassTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AchievementSeasonClassTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AchievementSeasonClassTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AchievementSeasonClassTableBase]] = ...) -> None: ...
