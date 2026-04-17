import stru_recruit_info_pb2 as _stru_recruit_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetRecruitInfoRequest(_message.Message):
    __slots__ = ("union_id", "recruit_info", "slogan")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    RECRUIT_INFO_FIELD_NUMBER: _ClassVar[int]
    SLOGAN_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    recruit_info: _stru_recruit_info_pb2.RecruitInfo
    slogan: str
    def __init__(self, union_id: _Optional[int] = ..., recruit_info: _Optional[_Union[_stru_recruit_info_pb2.RecruitInfo, _Mapping]] = ..., slogan: _Optional[str] = ...) -> None: ...
