import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FollowTableBase(_message.Message):
    __slots__ = ("id", "para_offset", "para_sca_double", "para_sca_base", "para_pre_dis", "para_pre_double", "para_s_pre_base", "para_time_to", "para_time_back")
    ID_FIELD_NUMBER: _ClassVar[int]
    PARA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PARA_SCA_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PARA_SCA_BASE_FIELD_NUMBER: _ClassVar[int]
    PARA_PRE_DIS_FIELD_NUMBER: _ClassVar[int]
    PARA_PRE_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PARA_S_PRE_BASE_FIELD_NUMBER: _ClassVar[int]
    PARA_TIME_TO_FIELD_NUMBER: _ClassVar[int]
    PARA_TIME_BACK_FIELD_NUMBER: _ClassVar[int]
    id: int
    para_offset: _table_basic_pb2.number_array
    para_sca_double: _table_basic_pb2.number_array
    para_sca_base: _table_basic_pb2.number_array
    para_pre_dis: _table_basic_pb2.number_array
    para_pre_double: _table_basic_pb2.number_array
    para_s_pre_base: _table_basic_pb2.number_array
    para_time_to: _table_basic_pb2.number_array
    para_time_back: _table_basic_pb2.number_array
    def __init__(self, id: _Optional[int] = ..., para_offset: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_sca_double: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_sca_base: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_pre_dis: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_pre_double: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_s_pre_base: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_time_to: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., para_time_back: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ...) -> None: ...

class FollowTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FollowTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FollowTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FollowTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FollowTableBase]] = ...) -> None: ...
