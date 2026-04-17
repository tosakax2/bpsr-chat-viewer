import stru_action_group_action_clip_pb2 as _stru_action_group_action_clip_pb2
import stru_action_group_face_clip_pb2 as _stru_action_group_face_clip_pb2
import enum_e_action_group_track_type_pb2 as _enum_e_action_group_track_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupTrack(_message.Message):
    __slots__ = ("track_type", "action_clip_list", "face_clip_list")
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    FACE_CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    track_type: _enum_e_action_group_track_type_pb2.EActionGroupTrackType
    action_clip_list: _containers.RepeatedCompositeFieldContainer[_stru_action_group_action_clip_pb2.ActionGroupActionClip]
    face_clip_list: _containers.RepeatedCompositeFieldContainer[_stru_action_group_face_clip_pb2.ActionGroupFaceClip]
    def __init__(self, track_type: _Optional[_Union[_enum_e_action_group_track_type_pb2.EActionGroupTrackType, str]] = ..., action_clip_list: _Optional[_Iterable[_Union[_stru_action_group_action_clip_pb2.ActionGroupActionClip, _Mapping]]] = ..., face_clip_list: _Optional[_Iterable[_Union[_stru_action_group_face_clip_pb2.ActionGroupFaceClip, _Mapping]]] = ...) -> None: ...
