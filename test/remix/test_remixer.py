import pytest

from infiniteremixer.remix.remixer import Remixer
from infiniteremixer.remix.remix import Remix
from infiniteremixer.remix.beat import Beat


@pytest.fixture
def remixer():
    return Remixer(10)


def test_remixer_is_instantiated(remixer):
    assert isinstance(remixer, Remixer)


def test_remix_is_generated(remixer, mocker):
    mocker.patch("infiniteremixer.remix.remixer.Remixer._choose_beat",
                 return_value=Beat.from_file_path("dir/track_name_1.wav"))
    remix = remixer.generate_remix()
    assert isinstance(remix, Remix)
    assert len(remix) == 10
    assert remix[0] == Beat.from_file_path("dir/track_name_1.wav")