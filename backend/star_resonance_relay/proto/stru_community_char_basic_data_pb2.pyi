import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import stru_basic_data_pb2 as _stru_basic_data_pb2
import stru_profession_data_pb2 as _stru_profession_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityCharBasicData(_message.Message):
    __slots__ = ("basic_data", "avatar_info", "profession_data")
    BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    basic_data: _stru_basic_data_pb2.BasicData
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    profession_data: _stru_profession_data_pb2.ProfessionData
    def __init__(self, basic_data: _Optional[_Union[_stru_basic_data_pb2.BasicData, _Mapping]] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., profession_data: _Optional[_Union[_stru_profession_data_pb2.ProfessionData, _Mapping]] = ...) -> None: ...
