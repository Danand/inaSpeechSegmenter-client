from inaSpeechSegmenter_client import VERSION

from setuptools import find_packages, setup

LONG_DESCRIPTION = open("README.md").read()

REQUIREMENTS = open("requirements.txt").read().split("\n")

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.10",
]

KEYWORDS = [
  "speech-segmentation",
  "audio-analysis",
  "music-detection",
  "noise-detection",
  "speech-detection",
  "speech-music",
  "gender-classification",
  "gender-representation",
  "speaker-gender",
  "speech",
  "music",
  "noise",
  "gender",
  "voice-activity-detection",
  "speech-activity-detection"
]

setup(
    name="inaSpeechSegmenter-client",
    version=VERSION,
    description="Common dependency for inaSpeechSegmenter API and client.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Andrey Danilov",
    author_email="danand@inbox.ru",
    url="https://github.com/Danand/inaSpeechSegmenter-client/",
    download_url="http://pypi.python.org/pypi/inaSpeechSegmenter-client/",
    packages=find_packages(),
    platforms=["Platform Independent"],
    license="MIT",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=REQUIREMENTS,
)
