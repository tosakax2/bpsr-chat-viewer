import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TalentTagTableBase(_message.Message):
    __slots__ = ("id", "des", "tag_type", "fight_res_id", "tag_name", "tag_icon", "tag_icon_bg", "tag_icon_mark", "simple_des", "details_des", "talent_associated_id", "fantasy_hole_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    TAG_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIGHT_RES_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_ICON_FIELD_NUMBER: _ClassVar[int]
    TAG_ICON_BG_FIELD_NUMBER: _ClassVar[int]
    TAG_ICON_MARK_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_DES_FIELD_NUMBER: _ClassVar[int]
    DETAILS_DES_FIELD_NUMBER: _ClassVar[int]
    TALENT_ASSOCIATED_ID_FIELD_NUMBER: _ClassVar[int]
    FANTASY_HOLE_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: str
    tag_type: int
    fight_res_id: int
    tag_name: _table_basic_pb2.mlstring
    tag_icon: str
    tag_icon_bg: str
    tag_icon_mark: str
    simple_des: _table_basic_pb2.mlstring
    details_des: _table_basic_pb2.mlstring
    talent_associated_id: _table_basic_pb2.int_array
    fantasy_hole_list: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., des: _Optional[str] = ..., tag_type: _Optional[int] = ..., fight_res_id: _Optional[int] = ..., tag_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., tag_icon: _Optional[str] = ..., tag_icon_bg: _Optional[str] = ..., tag_icon_mark: _Optional[str] = ..., simple_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., details_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., talent_associated_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., fantasy_hole_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class TalentTagTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TalentTagTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TalentTagTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TalentTagTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TalentTagTableBase]] = ...) -> None: ...
