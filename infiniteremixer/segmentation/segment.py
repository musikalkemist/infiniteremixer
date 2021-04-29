import argparse

from infiniteremixer.segmentation.segmentextractor import SegmentExtractor


def segment():
    """The "segment" entry point can be run to divide a group of songs in a
    directory into its beats and to save the relative segments as audio
    files in another directory.

    To run the script type:

    $ segment path/to/dir/with/files path/to/save/dir/for/beats -r 44100
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dir",
                        help="directory with audio files to segment into "
                             "beats")
    parser.add_argument("save_dir",
                        help="directory where to save generated audio files "
                             "for beats")
    parser.add_argument("-r", "--sample_rate",
                        help="sample rate for processing audio files",
                        default=22050)

    args = parser.parse_args()
    segment_extractor = SegmentExtractor(args.sample_rate)
    segment_extractor.create_and_save_segments(args.dir, args.save_dir)