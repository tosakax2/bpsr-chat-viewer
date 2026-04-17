import enum_e_body_size_pb2 as _enum_e_body_size_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicShowInfo(_message.Message):
    __slots__ = ("char_id", "name", "gender", "body_size", "level", "cur_talent_pool_id", "union_hunt_rand_idx", "is_newbie", "is_backflow")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_TALENT_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    UNION_HUNT_RAND_IDX_FIELD_NUMBER: _ClassVar[int]
    IS_NEWBIE_FIELD_NUMBER: _ClassVar[int]
    IS_BACKFLOW_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    name: str
    gender: int
    body_size: _enum_e_body_size_pb2.EBodySize
    level: int
    cur_talent_pool_id: int
    union_hunt_rand_idx: int
    is_newbie: bool
    is_backflow: bool
    def __init__(self, char_id: _Optional[int] = ..., name: _Optional[str] = ..., gender: _Optional[int] = ..., body_size: _Optional[_Union[_enum_e_body_size_pb2.EBodySize, str]] = ..., level: _Optional[int] = ..., cur_talent_pool_id: _Optional[int] = ..., union_hunt_rand_idx: _Optional[int] = ..., is_newbie: bool = ..., is_backflow: bool = ...) -> None: ...
