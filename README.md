# Documentation

# Speech Emotion Recognition
## Introduction
- This repository handles building and training Speech Emotion Recognition System.
- The basic idea behind this tool is to build and train/test a suited machine learning ( as well as deep learning ) algorithm that could recognize and detects human emotions from speech.
- This is useful for many industry fields such as making product recommendations, affective computing, etc.
- Check this [tutorial](https://www.thepythoncode.com/article/building-a-speech-emotion-recognizer-using-sklearn) for more information.
## Requirements
- **Python 3.6+**
### Python Packages
- **tensorflow**
- **librosa==0.6.3**
- **numpy**
- **soundfile==0.9.0**
- **scikit-learn==0.24.2**
- **pyaudio==0.2.11**
- **FastAPI**
- **uvicorn**


Install these libraries by the following command:
```
pip3 install -r requirements.txt
```

### Dataset
- [**RAVDESS**](https://zenodo.org/record/1188976) : The **R**yson **A**udio-**V**isual **D**atabase of **E**motional **S**peech and **S**ong that contains 24 actors (12 male, 12 female), vocalizing two lexically-matched statements in a neutral North American accent.



### Emotions available
There are 9 emotions available: "neutral", "calm", "happy" "sad", "angry", "fear", "disgust", "ps" (pleasant surprise) and "boredom".
## Feature Extraction
Feature extraction is the main part of the speech emotion recognition system. It is basically accomplished by changing the speech waveform to a form of parametric representation at a relatively lesser data rate.

In this repository, we have used the most used features that are available in [librosa](https://github.com/librosa/librosa) library including:
- [MFCC](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- Chromagram 
- MEL Spectrogram Frequency (mel)
- Contrast
- Tonnetz (tonal centroid features)

## Previews
- Jupyter Notebook
![Screenshot (221)](https://user-images.githubusercontent.com/85868593/202259600-2b87f96c-6e60-439c-bec9-e03bf49375d8.png)
![Screenshot (222)](https://user-images.githubusercontent.com/85868593/202259653-b3ebe927-e775-4269-a9ac-b9cd428d2e96.png)
![Screenshot (223)](https://user-images.githubusercontent.com/85868593/202259736-44e04c8d-4d24-49c5-814b-461ef50f2675.png)
![ss224](https://user-images.githubusercontent.com/85868593/202259698-6a1e4a3b-9ccd-49c3-b7c4-5505c82c7d2f.png)
![Screenshot (225)](https://user-images.githubusercontent.com/85868593/202260139-a639929f-85d1-457f-9e01-fb4ddc1167d2.png)

- FastApi routes
![Screenshot (225)](https://user-images.githubusercontent.com/85868593/202260278-df2f1e54-45ec-4aae-9958-b1482069f400.png)
![Screenshot (226)](https://user-images.githubusercontent.com/85868593/202260291-111063a8-b4be-4009-95f5-01b009f1234e.png)

- Models
![Screenshot (227)](https://user-images.githubusercontent.com/85868593/202260346-e62b0708-30b1-4d72-935c-b77393005e83.png)

- `localhost/docs` SwaggerUI
![Screenshot (228)](https://user-images.githubusercontent.com/85868593/202260586-03765fd8-db69-4330-9e54-1c26f3e4fcfa.png)

- Testing with realtime audio
![Screenshot (229)](https://user-images.githubusercontent.com/85868593/202260674-f74278e5-5b9d-4320-9304-24bd4367a221.png)

