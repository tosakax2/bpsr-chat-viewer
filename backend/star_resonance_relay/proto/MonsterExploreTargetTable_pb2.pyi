import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterExploreTargetTableBase(_message.Message):
    __slots__ = ("id", "target_type", "num", "scene_id", "param", "target_pos", "is_team_share", "target_des", "is_show_progress", "sp_variable", "sp_variable_limit", "sp_variable_name", "is_show_sp_variable_progress")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    TARGET_POS_FIELD_NUMBER: _ClassVar[int]
    IS_TEAM_SHARE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DES_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SP_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    SP_VARIABLE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SP_VARIABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_SP_VARIABLE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_type: int
    num: int
    scene_id: int
    param: _table_basic_pb2.int_array
    target_pos: str
    is_team_share: bool
    target_des: _table_basic_pb2.mlstring
    is_show_progress: bool
    sp_variable: _table_basic_pb2.mlstring_array
    sp_variable_limit: _table_basic_pb2.mlstring_array
    sp_variable_name: _table_basic_pb2.mlstring_array
    is_show_sp_variable_progress: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., target_type: _Optional[int] = ..., num: _Optional[int] = ..., scene_id: _Optional[int] = ..., param: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., target_pos: _Optional[str] = ..., is_team_share: bool = ..., target_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., is_show_progress: bool = ..., sp_variable: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., sp_variable_limit: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., sp_variable_name: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., is_show_sp_variable_progress: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class MonsterExploreTargetTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MonsterExploreTargetTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MonsterExploreTargetTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MonsterExploreTargetTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MonsterExploreTargetTableBase]] = ...) -> None: ...
