from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayHelper(_message.Message):
    __slots__ = ("displayed_helper_list", "completed_guide")
    class DisplayedHelperListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class CompletedGuideEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    DISPLAYED_HELPER_LIST_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_GUIDE_FIELD_NUMBER: _ClassVar[int]
    displayed_helper_list: _containers.ScalarMap[int, bool]
    completed_guide: _containers.ScalarMap[int, bool]
    def __init__(self, displayed_helper_list: _Optional[_Mapping[int, bool]] = ..., completed_guide: _Optional[_Mapping[int, bool]] = ...) -> None: ...
