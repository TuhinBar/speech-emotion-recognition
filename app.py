from fastapi import FastAPI, File, UploadFile
import uvicorn
import pickle
from models import SER
import librosa
import numpy as np
import soundfile
model= pickle.load(open('modelForPrediction.pkl','rb'))


app = FastAPI()
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

@app.get("/")
def read_root():
    return {"This is a speech emotion recognition API", "Please use /docs for more information"}

# Post route to send audio file for prediction


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save audio file to disk
    file_name = file.filename
    with open(file_name, "wb") as audio:
        audio.write(file.file.read())
    # Extract features from audio file
    feature = extract_feature(file_name, mfcc=True, chroma=True, mel=True)
    # Reshape feature to make it compatible with model
    feature = feature.reshape(1, -1)
    # Get prediction
    prediction = model.predict(feature)
    # Get probability
    accuracy = np.max(model.predict_proba(feature))
    # Get emotion
    emotion = str(prediction[0])
    # Return prediction
    return SER(emotion=emotion, confidence=format(accuracy*100))

if __name__ == "__main__":
    uvicorn.run(app)
