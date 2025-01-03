# `inaSpeechSegmenter` API client

This is a client for the `inaSpeechSegmenter` [API](https://github.com/Danand/inaSpeechSegmenter-api). This client serves as a wrapper around the original `inaSpeechSegmenter` toolkit, providing a convenient interface for integrating its features into your own applications.

Please note that this project is not a direct fork of the original `inaSpeechSegmenter` repository. It is designed to work with the `inaSpeechSegmenter` API, utilizing the capabilities of the original toolkit as an underlying technology.

For more information about the original `inaSpeechSegmenter`, visit the [`inaSpeechSegmenter` GitHub repository](https://github.com/ina-foss/inaSpeechSegmenter).

## About `inaSpeechSegmenter`

- **CNN-based Toolkit**: Utilizes Convolutional Neural Networks for audio segmentation.
- **Voice Activity Detection**: Identifies active speech segments in audio.
- **Speaker Gender Segmentation**: Classifies speech segments by gender.
- **Multimedia Support**: Processes audio zones into speech, music, and noise.
- **Tool Integration**: Available as a Python package and Docker image.
- **Open Source Recognition**: Achieved top ranks in VAD challenges and used in gender representation studies.

## Installing

```bash
pip install inaSpeechSegmenter-client
```

## Usage

```python
# Import:

from inaSpeechSegmenter_client.segmenter_client import SegmenterClient

# Create client instance:

segmenter_client = SegmenterClient(
    api_url="http://127.0.0.1:8888", # Your API url here.
)

# Let's say you have loaded audio file:

audio_file_name: str = audio_file.name
audio_bytes: bytes = audio_file.getbuffer()

try:
    response_data = segmenter_client.get_segments(
        audio_file_name=audio_file_name,
        audio_bytes=audio_bytes,
    )

    response_json = response_data.model_dump_json()

    # Example output:
    #
    # {
    #   "segments": [
    #     {
    #       "end_time": 1.86,
    #       "label": "noise",
    #       "start_time": 0
    #     },
    #     {
    #       "end_time": 2.3000000000000003,
    #       "label": "noEnergy",
    #       "start_time": 1.86
    #     },
    #     {
    #       "end_time": 5.26,
    #       "label": "noise",
    #       "start_time": 2.3000000000000003
    #     },
    #     {
    #       "end_time": 8.14,
    #       "label": "female",
    #       "start_time": 5.26
    #     }
    #   ]
    # }

    print(response_json)
except Exception as exception:
    # Log error if needed:
    logger.error(exception)
```

## Citing

`inaSpeechSegmenter` has been presented at the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 2018 conference in Calgary, Canada. If you use this toolbox in your research, you can cite the following work in your publications:

```bibtex
@inproceedings{ddoukhanicassp2018,
  author = {Doukhan, David and Carrive, Jean and Vallet, Félicien and Larcher, Anthony and Meignier, Sylvain},
  title = {An Open-Source Speaker Gender Detection Framework for Monitoring Gender Equality},
  year = {2018},
  organization={IEEE},
  booktitle={Acoustics Speech and Signal Processing (ICASSP), 2018 IEEE International Conference on}
}
```

inaSpeechSegmenter won [MIREX 2018 speech detection challenge](http://www.music-ir.org/mirex/wiki/2018:Music_and_or_Speech_Detection_Results)
Details on the speech detection submodule can be found bellow:

```bibtex
@inproceedings{ddoukhanmirex2018,
  author = {Doukhan, David and Lechapt, Eliott and Evrard, Marc and Carrive, Jean},
  title = {INA’S MIREX 2018 MUSIC AND SPEECH DETECTION SYSTEM},
  year = {2018},
  booktitle={Music Information Retrieval Evaluation eXchange (MIREX 2018)}
}
```

## Credits

This work has been partially funded by the French National Research Agency (project GEM : Gender Equality Monitor : ANR-19-CE38-0012) and by European Union's Horizon 2020 research and innovation programme (project [MeMAD](https://memad.eu) : H2020 grant agreement No 780069).

The code used to extract mel bands features is copy-pasted from [SIDEKIT project](https://git-lium.univ-lemans.fr/Larcher/sidekit)

Relevant contributions to the project were done by:

- [Eliott Lechapt](https://github.com/elechapt)
- [Cyril Lashkevich](https://github.com/notorca)
- [Rémi Uro](https://github.com/r-uro)
- [Simon Devauchelle](https://github.com/simonD3V)
- [Valentin Pelloin](https://github.com/valentinp72)
