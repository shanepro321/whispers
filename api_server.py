from flask import Flask, request, jsonify
from whisperkit.pipelines import WhisperKit, WhisperCpp, WhisperMLX

pipe = WhisperKit(whisper_version="openai/whisper-large-v3", out_dir="/Users/shane/PycharmProjects/whisper3/whisper")
print(pipe("audio.wav"))
