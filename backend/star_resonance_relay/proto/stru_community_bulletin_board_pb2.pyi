import stru_community_bulletin_board_operator_char_pb2 as _stru_community_bulletin_board_operator_char_pb2
import stru_community_bulletin_board_target_char_pb2 as _stru_community_bulletin_board_target_char_pb2
import enum_e_community_bulletin_board_type_pb2 as _enum_e_community_bulletin_board_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBulletinBoard(_message.Message):
    __slots__ = ("type", "operator_char", "target_char", "time", "content")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_CHAR_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHAR_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_community_bulletin_board_type_pb2.ECommunityBulletinBoardType
    operator_char: _stru_community_bulletin_board_operator_char_pb2.CommunityBulletinBoardOperatorChar
    target_char: _stru_community_bulletin_board_target_char_pb2.CommunityBulletinBoardTargetChar
    time: int
    content: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[_enum_e_community_bulletin_board_type_pb2.ECommunityBulletinBoardType, str]] = ..., operator_char: _Optional[_Union[_stru_community_bulletin_board_operator_char_pb2.CommunityBulletinBoardOperatorChar, _Mapping]] = ..., target_char: _Optional[_Union[_stru_community_bulletin_board_target_char_pb2.CommunityBulletinBoardTargetChar, _Mapping]] = ..., time: _Optional[int] = ..., content: _Optional[_Iterable[str]] = ...) -> None: ...
