from .midi.events import *
from .csv_converters import *
from .midi_converters import *

midi_to_csv_map = {
    NoteOffEvent: from_NoteOffEvent,
    NoteOnEvent: from_NoteOnEvent,
    AfterTouchEvent: from_AfterTouchEvent,
    ControlChangeEvent: from_ControlChangeEvent,
    ProgramChangeEvent: from_ProgramChangeEvent,
    ChannelAfterTouchEvent: from_ChannelAfterTouchEvent,
    PitchWheelEvent: from_PitchWheelEvent,
    SequenceNumberMetaEvent: from_SequenceNumberMetaEvent,
    ProgramNameEvent: from_ProgramNameEvent,
    TextMetaEvent: from_TextMetaEvent,
    CopyrightMetaEvent: from_CopyrightMetaEvent,
    TrackNameEvent: from_TrackNameEvent,
    InstrumentNameEvent: from_InstrumentNameEvent,
    LyricsEvent: from_LyricsEvent,
    MarkerEvent: from_MarkerEvent,
    CuePointEvent: from_CuePointEvent,
    ChannelPrefixEvent: from_ChannelPrefixEvent,
    PortEvent: from_PortEvent,
    EndOfTrackEvent: from_EndOfTrackEvent,
    DeviceNameEvent: from_DeviceNameEvent,
    TrackLoopEvent: from_TrackLoopEvent,
    SetTempoEvent: from_SetTempoEvent,
    SmpteOffsetEvent: from_SmpteOffsetEvent,
    TimeSignatureEvent: from_TimeSignatureEvent,
    KeySignatureEvent: from_KeySignatureEvent,
    SequencerSpecificEvent: from_SequencerSpecificEvent,
    SysexEvent: from_SysexEvent,
    SysexF7Event: from_SysexF7Event,
}

csv_to_midi_map = {
    "Note_off_c": to_NoteOffEvent,
    "Note_on_c": to_NoteOnEvent,
    "Poly_aftertouch_c": to_AfterTouchEvent,
    "Control_c": to_ControlChangeEvent,
    "Program_c": to_ProgramChangeEvent,
    "Channel_aftertouch_c": to_ChannelAfterTouchEvent,
    "Pitch_bend_c": to_PitchWheelEvent,
    "Sequence_number": to_SequenceNumberMetaEvent,
    "Program_name_t": to_ProgramNameEvent,
    "Text_t": to_TextMetaEvent,
    "Copyright_t": to_CopyrightMetaEvent,
    "Title_t": to_TrackNameEvent,
    "Instrument_name_t": to_InstrumentNameEvent,
    "Lyric_t": to_LyricsEvent,
    "Marker_t": to_MarkerEvent,
    "Cue_point_t": to_CuePointEvent,
    "Channel_prefix": to_ChannelPrefixEvent,
    "MIDI_port": to_PortEvent,
    "End_track": to_EndOfTrackEvent,
    "Device_name_t": to_DeviceNameEvent,
    "Loop_track": to_TrackLoopEvent,
    "Tempo": to_SetTempoEvent,
    "SMPTE_offset": to_SmpteOffsetEvent,
    "Time_signature": to_TimeSignatureEvent,
    "Key_signature": to_KeySignatureEvent,
    "Sequencer_specific": to_SequencerSpecificEvent,
    "System_exclusive": to_SysexEvent,
    "System_exclusive_F7": to_SysexF7Event,
}
