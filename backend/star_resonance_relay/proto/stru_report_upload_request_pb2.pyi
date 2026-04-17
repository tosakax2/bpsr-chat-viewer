import enum_e_report_category_type_pb2 as _enum_e_report_category_type_pb2
import enum_e_report_reason_type_pb2 as _enum_e_report_reason_type_pb2
import enum_e_report_scene_type_pb2 as _enum_e_report_scene_type_pb2
import stru_report_base_info_pb2 as _stru_report_base_info_pb2
import stru_report_chat_pb2 as _stru_report_chat_pb2
import stru_report_home_pb2 as _stru_report_home_pb2
import stru_report_picture_pb2 as _stru_report_picture_pb2
import stru_report_union_pb2 as _stru_report_union_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportUploadRequest(_message.Message):
    __slots__ = ("scene_type", "category_type", "reason_type", "report_desc", "report_base_info", "report_chat", "report_picture", "report_union", "report_home")
    SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPORT_DESC_FIELD_NUMBER: _ClassVar[int]
    REPORT_BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    REPORT_CHAT_FIELD_NUMBER: _ClassVar[int]
    REPORT_PICTURE_FIELD_NUMBER: _ClassVar[int]
    REPORT_UNION_FIELD_NUMBER: _ClassVar[int]
    REPORT_HOME_FIELD_NUMBER: _ClassVar[int]
    scene_type: _enum_e_report_scene_type_pb2.EReportSceneType
    category_type: _enum_e_report_category_type_pb2.EReportCategoryType
    reason_type: _containers.RepeatedScalarFieldContainer[_enum_e_report_reason_type_pb2.EReportReasonType]
    report_desc: str
    report_base_info: _stru_report_base_info_pb2.ReportBaseInfo
    report_chat: _stru_report_chat_pb2.ReportChat
    report_picture: _stru_report_picture_pb2.ReportPicture
    report_union: _stru_report_union_pb2.ReportUnion
    report_home: _stru_report_home_pb2.ReportHome
    def __init__(self, scene_type: _Optional[_Union[_enum_e_report_scene_type_pb2.EReportSceneType, str]] = ..., category_type: _Optional[_Union[_enum_e_report_category_type_pb2.EReportCategoryType, str]] = ..., reason_type: _Optional[_Iterable[_Union[_enum_e_report_reason_type_pb2.EReportReasonType, str]]] = ..., report_desc: _Optional[str] = ..., report_base_info: _Optional[_Union[_stru_report_base_info_pb2.ReportBaseInfo, _Mapping]] = ..., report_chat: _Optional[_Union[_stru_report_chat_pb2.ReportChat, _Mapping]] = ..., report_picture: _Optional[_Union[_stru_report_picture_pb2.ReportPicture, _Mapping]] = ..., report_union: _Optional[_Union[_stru_report_union_pb2.ReportUnion, _Mapping]] = ..., report_home: _Optional[_Union[_stru_report_home_pb2.ReportHome, _Mapping]] = ...) -> None: ...
