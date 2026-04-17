import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PresentationEPFlowTableBase(_message.Message):
    __slots__ = ("id", "res_path", "flow_name", "flow_type", "get_option", "is_save_play_state", "check_play_key_index", "check_play_type", "is_default_camera_disabled", "content_hiding", "ignore_hiding_npc", "is_model_dialogue", "black_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    RES_PATH_FIELD_NUMBER: _ClassVar[int]
    FLOW_NAME_FIELD_NUMBER: _ClassVar[int]
    FLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_OPTION_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_PLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_PLAY_KEY_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHECK_PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_CAMERA_DISABLED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HIDING_FIELD_NUMBER: _ClassVar[int]
    IGNORE_HIDING_NPC_FIELD_NUMBER: _ClassVar[int]
    IS_MODEL_DIALOGUE_FIELD_NUMBER: _ClassVar[int]
    BLACK_MASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    res_path: str
    flow_name: str
    flow_type: str
    get_option: bool
    is_save_play_state: bool
    check_play_key_index: int
    check_play_type: int
    is_default_camera_disabled: bool
    content_hiding: int
    ignore_hiding_npc: _table_basic_pb2.int_array
    is_model_dialogue: bool
    black_mask: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., res_path: _Optional[str] = ..., flow_name: _Optional[str] = ..., flow_type: _Optional[str] = ..., get_option: bool = ..., is_save_play_state: bool = ..., check_play_key_index: _Optional[int] = ..., check_play_type: _Optional[int] = ..., is_default_camera_disabled: bool = ..., content_hiding: _Optional[int] = ..., ignore_hiding_npc: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_model_dialogue: bool = ..., black_mask: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class PresentationEPFlowTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PresentationEPFlowTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PresentationEPFlowTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PresentationEPFlowTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PresentationEPFlowTableBase]] = ...) -> None: ...
