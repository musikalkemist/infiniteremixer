import librosa


def estimate_beats(signal, sr):
    """Beat tracker that uses librosa facilities under the hood.

    :param signal: (np.ndarray) Audio time series to analyse
    :param sr: (int) Sample rate

    :return: (np.ndarray) Estimated beat events measured in samples
    """
    beats =  librosa.beat.beat_track(signal, sr, units="samples")[1]
    return beats


def estimate_beats_and_tempo(signal, sr):
    """Beat tracker that extracts beat events and global tempo. It uses
    librosa facilities under the hood.

    :param signal: (np.ndarray) Audio time series to analyse
    :param sr: (int) Sample rate

    :return: (float) Estimated global tempo (in beats per minute)
    :return: (np.ndarray) Estimated beat events measured in samples
    """
    tempo, beats = librosa.beat.beat_track(signal, sr, units="samples")
    return beats, tempo