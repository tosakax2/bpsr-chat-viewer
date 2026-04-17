import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonActTableBase(_message.Message):
    __slots__ = ("id", "function_id", "season_id", "type", "sort", "name", "label_pic", "back_ground_pic", "act_des", "other_des", "preview_award", "quick_jump_type", "quick_jump_param", "unlock_des")
    ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_PIC_FIELD_NUMBER: _ClassVar[int]
    BACK_GROUND_PIC_FIELD_NUMBER: _ClassVar[int]
    ACT_DES_FIELD_NUMBER: _ClassVar[int]
    OTHER_DES_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_AWARD_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_PARAM_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DES_FIELD_NUMBER: _ClassVar[int]
    id: int
    function_id: int
    season_id: int
    type: int
    sort: int
    name: _table_basic_pb2.mlstring
    label_pic: str
    back_ground_pic: str
    act_des: _table_basic_pb2.mlstring
    other_des: _table_basic_pb2.mlstring
    preview_award: int
    quick_jump_type: int
    quick_jump_param: _table_basic_pb2.int_array
    unlock_des: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., function_id: _Optional[int] = ..., season_id: _Optional[int] = ..., type: _Optional[int] = ..., sort: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., label_pic: _Optional[str] = ..., back_ground_pic: _Optional[str] = ..., act_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., other_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., preview_award: _Optional[int] = ..., quick_jump_type: _Optional[int] = ..., quick_jump_param: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., unlock_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class SeasonActTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonActTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonActTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonActTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonActTableBase]] = ...) -> None: ...
