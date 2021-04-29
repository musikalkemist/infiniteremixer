import pytest

from infiniteremixer.remix.remix import Remix
from infiniteremixer.remix.beat import Beat


@pytest.fixture
def remix():

    beat1 = Beat("path1", "track1", 1)
    beat2 = Beat("path2", "track1", 2)
    beat3 = Beat("path3", "track2", 3)
    beat4 = Beat("path4", "track3", 1)
    remix = Remix(beat1, beat2, beat3, beat4)
    return remix


def test_beat_is_instantiated():
    remix = Remix()
    assert isinstance(remix, Remix)


def test_get_lenght_of_remix(remix):
    assert len(remix) == 4


def test_last_beat_is_returned_correctly(remix):
    last_beat = remix.last_beat
    expected_last_beat = Beat("path4", "track3", 1)
    assert last_beat == expected_last_beat


def test_num_beats_with_last_track_is_returned_correctly(remix):
    num_beats_with_last_track = remix.num_beats_with_last_track
    assert num_beats_with_last_track == 2


def test_file_paths_for_remix_are_retrurned(remix):
    file_paths = remix.file_paths
    expected_file_paths = [
        "path1", "path2",
        "path3", "path4"
    ]
    assert file_paths == expected_file_paths





