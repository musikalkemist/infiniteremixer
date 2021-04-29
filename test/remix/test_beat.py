from infiniteremixer.remix.beat import Beat


def test_beat_is_instantiated():
    beat = Beat("path", 1, "track")
    assert isinstance(beat, Beat)


def test_beat_is_instantiated_from_path_correctly():
    file_path = "dir/track_name.mp3_32.wav"
    beat = Beat.from_file_path(file_path)
    assert beat.number == 32
    assert beat.file_path == file_path
    assert beat.track == "track_name.mp3"


def test_track_is_derived_from_file_path():
    file_path = "dir/track_name.mp3_32.wav"
    expected_track = "track_name.mp3"
    track = Beat._get_track_from_file_path(file_path)
    assert track == expected_track


def test_beat_number_is_derived_from_file_path():
    file_path = "dir/track_name.mp3_31231232.wav"
    expected_beat_number = 31231232
    beat_number = Beat._get_beat_number_from_file_path(file_path)
    assert beat_number == expected_beat_number


def test_file_path_with_replaed_number_is_returned():
    file_path = "dir/track_name.mp3_31231232.wav"
    new_number = 100
    expected_file_path = "dir/track_name.mp3_100.wav"
    new_file_path = Beat.replace_number_in_file_path(file_path, new_number)
    assert new_file_path == expected_file_path