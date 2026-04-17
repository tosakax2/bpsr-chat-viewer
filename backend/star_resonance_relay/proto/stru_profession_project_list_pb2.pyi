import stru_profession_project_common_sync_data_pb2 as _stru_profession_project_common_sync_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionProjectList(_message.Message):
    __slots__ = ("profession_project_list", "current_project_id")
    class ProfessionProjectListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData, _Mapping]] = ...) -> None: ...
    PROFESSION_PROJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    profession_project_list: _containers.MessageMap[int, _stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData]
    current_project_id: int
    def __init__(self, profession_project_list: _Optional[_Mapping[int, _stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData]] = ..., current_project_id: _Optional[int] = ...) -> None: ...
