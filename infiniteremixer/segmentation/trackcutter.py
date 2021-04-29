def cut(signal, delimiters):
    """Divide a signal into segments based on delimiters.

    :param signal: (np.ndarray) Time series to cut
    :param delimiters: (np.ndarray) Delimiters expressed in samples

    :return: (list of np.ndarray) Segments of the track
    """
    segments = []
    start_sample = 0
    for delimiter in delimiters:
        stop_sample = delimiter
        segment = signal[start_sample:stop_sample]
        segments.append(segment)
        start_sample = stop_sample
    last_segment = signal[start_sample:]
    segments.append(last_segment)
    return segments
