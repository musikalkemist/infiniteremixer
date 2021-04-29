import pytest
import numpy as np

from infiniteremixer.remix.audiochunkmerger import AudioChunkMerger


@pytest.fixture
def chunk_manager():
    return AudioChunkMerger()


def test_chunk_manager_is_instantiated(chunk_manager):
    assert isinstance(chunk_manager, AudioChunkMerger)


def test_audio_chunks_are_concatenated(chunk_manager, mocker):
    mocker.patch("infiniteremixer.remix.audiochunkmerger.AudioChunkMerger"
                 ".load_audio_file",
                 return_value=np.array([1, 2]))
    audio_file_paths = [
        "dummy_audio_file1.wav",
        "dummy_audio_file2.wav",
        "dummy_audio_file3.wav"
    ]
    concatenated_signal = chunk_manager.concatenate(audio_file_paths)
    assert np.array_equal(concatenated_signal, np.array([1, 2, 1, 2, 1, 2]))