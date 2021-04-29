import os
from dataclasses import dataclass


@dataclass
class Beat:
    """This class represents the beat of a track."""

    file_path: str
    track: str
    number: int

    @classmethod
    def from_file_path(cls, file_path):
        track = Beat._get_track_from_file_path(file_path)
        beat_number = Beat._get_beat_number_from_file_path(file_path)
        return Beat(file_path, track, beat_number)

    @staticmethod
    def replace_number_in_file_path(file_path, number):
        number_and_format = file_path.split("_")[-1]
        format = file_path.split(".")[-1]
        new_number_and_format = f"{number}.{format}"
        path_head = file_path[:-len(number_and_format)]
        new_file_path = path_head + new_number_and_format
        return new_file_path

    @staticmethod
    def _get_beat_number_from_file_path(file_path):
        file_name = os.path.split(file_path)[1]
        number_and_format = file_name.split("_")[-1]
        number = number_and_format.split(".")[0]
        return int(number)

    @staticmethod
    def _get_track_from_file_path(file_path):
        file_name = os.path.split(file_path)[1]
        number_and_format = file_name.split("_")[-1]
        num_characters_to_drop = len(number_and_format) + 1
        track = file_name[:-num_characters_to_drop]
        return track