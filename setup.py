import setuptools

with open("requirements.txt", "r") as fp:
    required = fp.read().splitlines()

setuptools.setup(
    name="infiniteremixer",
    version="0.0.1",
    author="Valerio Velardo",
    author_email="valerio@thesoundofai.com",
    description="An app that generates infinite re-mixes of groups of songs",
    url="https://github.com/musikalkemist/infiniteremixer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",
    install_requires=required,
    entry_points={
        "console_scripts": [
            "segment = infiniteremixer.segmentation.segment:segment",
            "create_dataset = infiniteremixer.data.createdataset:create_dataset",
            "fit_nearest_neighbours = infiniteremixer.search.fitnearestneighbours:fit_nearest_neighbours",
            "generate_remix = infiniteremixer.remix.generateremix:generate_remix"
        ]
    },
    extras_require={
        "test": [
            "pytest",
            "pytest-mock"
        ]
    }
)
