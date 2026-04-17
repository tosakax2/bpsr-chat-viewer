from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacialLibraryTableBase(_message.Message):
    __slots__ = ("id", "facial_name", "remark", "face_clip", "mouth_clip", "eye_clip", "brow_clip", "nose_clip", "DFM_Brow", "DFM_Eye", "ADJ_Brow", "ADJ_Eye", "ADJ_Nose", "ADJ_Mouth", "ADJ_Face", "preview_picture")
    ID_FIELD_NUMBER: _ClassVar[int]
    FACIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    FACE_CLIP_FIELD_NUMBER: _ClassVar[int]
    MOUTH_CLIP_FIELD_NUMBER: _ClassVar[int]
    EYE_CLIP_FIELD_NUMBER: _ClassVar[int]
    BROW_CLIP_FIELD_NUMBER: _ClassVar[int]
    NOSE_CLIP_FIELD_NUMBER: _ClassVar[int]
    DFM_BROW_FIELD_NUMBER: _ClassVar[int]
    DFM_EYE_FIELD_NUMBER: _ClassVar[int]
    ADJ_BROW_FIELD_NUMBER: _ClassVar[int]
    ADJ_EYE_FIELD_NUMBER: _ClassVar[int]
    ADJ_NOSE_FIELD_NUMBER: _ClassVar[int]
    ADJ_MOUTH_FIELD_NUMBER: _ClassVar[int]
    ADJ_FACE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_PICTURE_FIELD_NUMBER: _ClassVar[int]
    id: int
    facial_name: str
    remark: str
    face_clip: str
    mouth_clip: str
    eye_clip: str
    brow_clip: str
    nose_clip: str
    DFM_Brow: str
    DFM_Eye: str
    ADJ_Brow: str
    ADJ_Eye: str
    ADJ_Nose: str
    ADJ_Mouth: str
    ADJ_Face: str
    preview_picture: str
    def __init__(self, id: _Optional[int] = ..., facial_name: _Optional[str] = ..., remark: _Optional[str] = ..., face_clip: _Optional[str] = ..., mouth_clip: _Optional[str] = ..., eye_clip: _Optional[str] = ..., brow_clip: _Optional[str] = ..., nose_clip: _Optional[str] = ..., DFM_Brow: _Optional[str] = ..., DFM_Eye: _Optional[str] = ..., ADJ_Brow: _Optional[str] = ..., ADJ_Eye: _Optional[str] = ..., ADJ_Nose: _Optional[str] = ..., ADJ_Mouth: _Optional[str] = ..., ADJ_Face: _Optional[str] = ..., preview_picture: _Optional[str] = ...) -> None: ...

class FacialLibraryTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FacialLibraryTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FacialLibraryTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FacialLibraryTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FacialLibraryTableBase]] = ...) -> None: ...
