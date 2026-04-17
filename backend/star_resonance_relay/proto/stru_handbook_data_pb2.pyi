import stru_hand_book_struct_pb2 as _stru_hand_book_struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HandbookData(_message.Message):
    __slots__ = ("unlock_note_important_role_map", "unlock_note_reading_book_map", "unlock_note_dictionary_map", "unlock_note_post_card_map", "unlock_note_month_card_map")
    class UnlockNoteImportantRoleMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hand_book_struct_pb2.HandBookStruct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hand_book_struct_pb2.HandBookStruct, _Mapping]] = ...) -> None: ...
    class UnlockNoteReadingBookMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hand_book_struct_pb2.HandBookStruct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hand_book_struct_pb2.HandBookStruct, _Mapping]] = ...) -> None: ...
    class UnlockNoteDictionaryMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hand_book_struct_pb2.HandBookStruct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hand_book_struct_pb2.HandBookStruct, _Mapping]] = ...) -> None: ...
    class UnlockNotePostCardMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hand_book_struct_pb2.HandBookStruct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hand_book_struct_pb2.HandBookStruct, _Mapping]] = ...) -> None: ...
    class UnlockNoteMonthCardMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hand_book_struct_pb2.HandBookStruct
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hand_book_struct_pb2.HandBookStruct, _Mapping]] = ...) -> None: ...
    UNLOCK_NOTE_IMPORTANT_ROLE_MAP_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_NOTE_READING_BOOK_MAP_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_NOTE_DICTIONARY_MAP_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_NOTE_POST_CARD_MAP_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_NOTE_MONTH_CARD_MAP_FIELD_NUMBER: _ClassVar[int]
    unlock_note_important_role_map: _containers.MessageMap[int, _stru_hand_book_struct_pb2.HandBookStruct]
    unlock_note_reading_book_map: _containers.MessageMap[int, _stru_hand_book_struct_pb2.HandBookStruct]
    unlock_note_dictionary_map: _containers.MessageMap[int, _stru_hand_book_struct_pb2.HandBookStruct]
    unlock_note_post_card_map: _containers.MessageMap[int, _stru_hand_book_struct_pb2.HandBookStruct]
    unlock_note_month_card_map: _containers.MessageMap[int, _stru_hand_book_struct_pb2.HandBookStruct]
    def __init__(self, unlock_note_important_role_map: _Optional[_Mapping[int, _stru_hand_book_struct_pb2.HandBookStruct]] = ..., unlock_note_reading_book_map: _Optional[_Mapping[int, _stru_hand_book_struct_pb2.HandBookStruct]] = ..., unlock_note_dictionary_map: _Optional[_Mapping[int, _stru_hand_book_struct_pb2.HandBookStruct]] = ..., unlock_note_post_card_map: _Optional[_Mapping[int, _stru_hand_book_struct_pb2.HandBookStruct]] = ..., unlock_note_month_card_map: _Optional[_Mapping[int, _stru_hand_book_struct_pb2.HandBookStruct]] = ...) -> None: ...
