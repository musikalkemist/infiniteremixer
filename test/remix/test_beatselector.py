import pytest

from infiniteremixer.remix.beatselector import BeatSelector
from infiniteremixer.remix.beat import Beat


@pytest.fixture
def beat_selector():
    beat_selector = BeatSelector(0.5)
    beat_selector.beat_file_paths = [
        "dir/track_name1_1.wav",
        "dir/track_name1_2.wav",
        "dir/track_name2_1.wav"
    ]
    return beat_selector


def test_beat_selector_is_instantiated(beat_selector):
    assert isinstance(beat_selector, BeatSelector)


def test_beat_is_chosen_randomly(beat_selector):
    beat = beat_selector._choose_beat_randomly()
    assert beat.file_path in beat_selector.beat_file_paths


def test_jump_threshold_is_calculated(beat_selector):
    threshold = beat_selector._calculate_jump_threshold(2)
    expected_threshold = 0.1505149
    assert threshold == pytest.approx(expected_threshold)


def test_check_is_beat_jump(beat_selector):
    trues = 0
    for i in range(1000):
        if beat_selector._is_beat_jump(2):
            trues += 1
    assert 120 < trues < 175


def test_next_beat_in_track_is_chosen(beat_selector):
    beat = Beat.from_file_path("dir/track_name1_1.wav")
    expected_beat = Beat.from_file_path("dir/track_name1_2.wav")
    next_beat = beat_selector._get_next_beat_in_track_if_possible_or_random(
        beat)
    assert next_beat == expected_beat


