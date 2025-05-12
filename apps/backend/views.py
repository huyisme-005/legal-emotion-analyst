"""
API views for emotion analysis using Hugging Face Transformers and Whisper for speech-to-text.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from transformers import pipeline
import whisper

import wave
import tempfile
import os

# Load the emotion detection pipeline once at module level for efficiency
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

# Load Whisper model once at module level for efficiency
whisper_model = whisper.load_model("base")  # You can use "small", "medium", "large" for better accuracy

class AnalyzeView(APIView):
    """
    Receives audio file, processes it, transcribes to text using Whisper,
    and performs emotion analysis using Hugging Face Transformers.
    """
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        audio_file = request.FILES.get('audio')
        if not audio_file:
            return Response({"error": "No audio file provided."}, status=400)

        # Save the uploaded audio to a temporary file for processing
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            for chunk in audio_file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name

        # --- Step 1: Basic audio processing (read duration, etc.) ---
        try:
            with wave.open(tmp_path, 'rb') as wav_file:
                n_channels = wav_file.getnchannels()
                sample_width = wav_file.getsampwidth()
                frame_rate = wav_file.getframerate()
                n_frames = wav_file.getnframes()
                duration = n_frames / float(frame_rate)
        except Exception as e:
            os.remove(tmp_path)
            return Response({"error": f"Failed to process audio file: {e}"}, status=400)

        # --- Step 2: Transcribe audio to text using Whisper ---
        try:
            result = whisper_model.transcribe(tmp_path)
            transcript = result["text"]
        except Exception as e:
            os.remove(tmp_path)
            return Response({"error": f"Failed to transcribe audio: {e}"}, status=500)

        # --- Step 3: Emotion analysis ---
        emotion_results = emotion_classifier(transcript)

        # Clean up temp file
        os.remove(tmp_path)

        # --- Step 4: Return results ---
        return Response({
            "audio_info": {
                "channels": n_channels,
                "sample_width": sample_width,
                "frame_rate": frame_rate,
                "duration_seconds": duration
            },
            "transcript": transcript,
            "emotions": emotion_results,
            "mediation_suggestion": "Acknowledge positive emotions and address sources of frustration."
        })
