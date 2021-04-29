import argparse

from sklearn.neighbors import NearestNeighbors

from infiniteremixer.utils.io import load_from_pickle, save_to_pickle


def fit_nearest_neighbours():
    """The "fit_nearest_neighbour" entry point trains a nearest neighbour
    object using sklearn and pickles it.

    To use this entry point type:

    $ fit_nearest_neighbours dataset/path save/path
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_path",
                        help="path to dataset file")
    parser.add_argument("save_path",
                        help="path where to save trained nearest neighbour "
                             "model")
    args = parser.parse_args()

    dataset = load_from_pickle(args.dataset_path)
    print(f"Loaded dataset from {args.dataset_path}")
    print(f"Dataset array has shape {dataset.shape}")
    nearest_neighbour = NearestNeighbors()
    nearest_neighbour.fit(dataset)
    print("Created nearest neighbour")
    save_to_pickle(args.save_path, nearest_neighbour)
    print(f"Saved nearest neighbour model to {args.save_path}")
