import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CutsceneTableBase(_message.Message):
    __slots__ = ("id", "name_design", "res_path", "content_hiding", "is_cutscene_editor", "can_skip", "validate_skip", "black_mask", "allow_input", "is_save_play_state", "check_play_key_index", "end_sync_actor_type", "end_sync_actor_id", "end_sync_actor_pos", "end_sync_actor_rotation", "check_play_type", "audio_state", "binding_scene", "player_sync_type", "player_sync_pos", "player_sync_rotation")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_DESIGN_FIELD_NUMBER: _ClassVar[int]
    RES_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HIDING_FIELD_NUMBER: _ClassVar[int]
    IS_CUTSCENE_EDITOR_FIELD_NUMBER: _ClassVar[int]
    CAN_SKIP_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_SKIP_FIELD_NUMBER: _ClassVar[int]
    BLACK_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INPUT_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_PLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_PLAY_KEY_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_SYNC_ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    END_SYNC_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    END_SYNC_ACTOR_POS_FIELD_NUMBER: _ClassVar[int]
    END_SYNC_ACTOR_ROTATION_FIELD_NUMBER: _ClassVar[int]
    CHECK_PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STATE_FIELD_NUMBER: _ClassVar[int]
    BINDING_SCENE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SYNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SYNC_POS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SYNC_ROTATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name_design: str
    res_path: str
    content_hiding: int
    is_cutscene_editor: bool
    can_skip: int
    validate_skip: bool
    black_mask: _table_basic_pb2.int_array
    allow_input: _table_basic_pb2.int_array
    is_save_play_state: bool
    check_play_key_index: int
    end_sync_actor_type: _table_basic_pb2.int_array
    end_sync_actor_id: _table_basic_pb2.int_array
    end_sync_actor_pos: _table_basic_pb2.vector3_array
    end_sync_actor_rotation: _table_basic_pb2.number_array
    check_play_type: int
    audio_state: str
    binding_scene: int
    player_sync_type: int
    player_sync_pos: _table_basic_pb2.number_array
    player_sync_rotation: float
    def __init__(self, id: _Optional[int] = ..., name_design: _Optional[str] = ..., res_path: _Optional[str] = ..., content_hiding: _Optional[int] = ..., is_cutscene_editor: bool = ..., can_skip: _Optional[int] = ..., validate_skip: bool = ..., black_mask: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., allow_input: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_save_play_state: bool = ..., check_play_key_index: _Optional[int] = ..., end_sync_actor_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., end_sync_actor_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., end_sync_actor_pos: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., end_sync_actor_rotation: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., check_play_type: _Optional[int] = ..., audio_state: _Optional[str] = ..., binding_scene: _Optional[int] = ..., player_sync_type: _Optional[int] = ..., player_sync_pos: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., player_sync_rotation: _Optional[float] = ...) -> None: ...

class CutsceneTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CutsceneTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CutsceneTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CutsceneTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CutsceneTableBase]] = ...) -> None: ...
