import argparse

from infiniteremixer.utils.io import load_from_pickle, write_wav
from infiniteremixer.remix.audiochunkmerger import AudioChunkMerger
from infiniteremixer.remix.featureretriever import FeatureRetriever
from infiniteremixer.search.nnsearch import NNSearch
from infiniteremixer.remix.beatselector import BeatSelector
from infiniteremixer.remix.remixer import Remixer


# change these paths to run the script with your data
MAPPING_PATH = "/home/valerio/datasets/infinitemixer/mfcc_chromo/mapping.pkl"
FEATURES_PATH = "/home/valerio/datasets/infinitemixer/mfcc_chromo/dataset.pkl"
NEAREST_NEIGHBOUR_PATH = "/home/valerio/datasets/infinitemixer/mfcc_chromo/nearestneighbour.pkl"
SAMPLE_RATE = 22050


def generate_remix():
    parser = argparse.ArgumentParser()
    parser.add_argument("jump_rate",
                        help="rate at which you'd like to see remix jumps. "
                             "Must be between 0 and 1")
    parser.add_argument("number_of_beats",
                        help="number of beats for generated remix")
    parser.add_argument("save_path",
                        help="path where to save generated remix")
    args = parser.parse_args()

    jump_rate = float(args.jump_rate)
    num_of_beats = int(args.number_of_beats)
    save_path = args.save_path

    remixer, chunk_merger = _create_objects(jump_rate, num_of_beats)
    remix = remixer.generate_remix()
    print(f"Generated remix with {num_of_beats} beats")
    audio_remix = chunk_merger.concatenate(remix.file_paths)
    print(f"Merged beats together")
    write_wav(save_path, audio_remix, SAMPLE_RATE)
    print(f"Saved new remix to {SAMPLE_RATE}")


def _create_objects(jump_rate, number_of_beats):
    beats_file_paths = load_from_pickle(MAPPING_PATH)
    features = load_from_pickle(FEATURES_PATH)
    nearest_neighbour_model = load_from_pickle(NEAREST_NEIGHBOUR_PATH)

    chunk_merger = AudioChunkMerger()
    feature_retriever = FeatureRetriever()
    feature_retriever.mapping = beats_file_paths
    feature_retriever.features = features
    nn_search = NNSearch()
    nn_search.mapping = beats_file_paths
    nn_search.model = nearest_neighbour_model
    beat_selector = BeatSelector(jump_rate)
    beat_selector.nn_search = nn_search
    beat_selector.feature_retriever = feature_retriever
    beat_selector.beat_file_paths = beats_file_paths
    remixer = Remixer(number_of_beats)
    remixer.beat_selector = beat_selector

    return remixer, chunk_merger


if __name__ == "__main__":
    generate_remix()