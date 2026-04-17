import stru_buff_d_b_data_pb2 as _stru_buff_d_b_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffDBInfo(_message.Message):
    __slots__ = ("max_id", "all_buff_db_data")
    class AllBuffDbDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_buff_d_b_data_pb2.BuffDBData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_buff_d_b_data_pb2.BuffDBData, _Mapping]] = ...) -> None: ...
    MAX_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_BUFF_DB_DATA_FIELD_NUMBER: _ClassVar[int]
    max_id: int
    all_buff_db_data: _containers.MessageMap[int, _stru_buff_d_b_data_pb2.BuffDBData]
    def __init__(self, max_id: _Optional[int] = ..., all_buff_db_data: _Optional[_Mapping[int, _stru_buff_d_b_data_pb2.BuffDBData]] = ...) -> None: ...
