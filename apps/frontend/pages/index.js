/**
 * Main page: records audio, sends to backend, displays emotion analysis.
 * UI/UX enhanced with HTML/CSS.
 */

import React, { useState, useRef } from "react";

export default function Home() {
  // State for recording and result
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState(null);
  const [emotion, setEmotion] = useState(null);
  const [error, setError] = useState("");
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  // Start recording
  const startRecording = async () => {
    setRecording(true);
    setEmotion(null);
    setError("");
    audioChunksRef.current = [];
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new window.MediaRecorder(stream);

      mediaRecorderRef.current.ondataavailable = (e) => {
        audioChunksRef.current.push(e.data);
      };

      mediaRecorderRef.current.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
        setAudioURL(URL.createObjectURL(audioBlob));

        // Send audio to backend for analysis
        const formData = new FormData();
        formData.append("audio", audioBlob, "recording.wav");

        try {
          const res = await fetch("http://localhost:8000/api/analyze/", {
            method: "POST",
            body: formData,
          });
          if (!res.ok) throw new Error("Backend error");
          const data = await res.json();
          setEmotion(data);
        } catch (err) {
          setError("Failed to analyze audio. Please try again.");
        }
      };

      mediaRecorderRef.current.start();

      // Stop recording after 5 seconds for demo
      setTimeout(() => {
        mediaRecorderRef.current.stop();
        setRecording(false);
      }, 5000);
    } catch (err) {
      setRecording(false);
      setError("Microphone access denied or not available.");
    }
  };

  return (
    <div className="container">
      <header>
        <h1>Legal Emotion Analyzer</h1>
        <p className="subtitle">
          Record a short legal conversation and see the emotional landscape, powered by AI.
        </p>
      </header>

      <main>
        <button
          className={`record-btn ${recording ? "active" : ""}`}
          onClick={startRecording}
          disabled={recording}
        >
          {recording ? (
            <span>
              <span className="dot" /> Recording...
            </span>
          ) : (
            "Start Recording"
          )}
        </button>
        <p className="hint">Recording lasts 5 seconds for demo purposes.</p>

        {audioURL && (
          <section className="audio-section">
            <h3>Playback:</h3>
            <audio src={audioURL} controls />
          </section>
        )}

        {emotion && (
          <section className="result-section">
            <h3>Emotion Analysis:</h3>
            <div className="transcript">
              <strong>Transcript:</strong> {emotion.transcript}
            </div>
            <div className="emotions">
              <strong>Detected Emotions:</strong>
              <ul>
                {emotion.emotions.map((e, idx) => (
                  <li key={idx}>
                    <span className="emotion-label">{e.label}</span>
                    <span className="emotion-score">
                      {(e.score * 100).toFixed(1)}%
                    </span>
                  </li>
                ))}
              </ul>
            </div>
            <div className="suggestion">
              <strong>Mediation Suggestion:</strong> {emotion.mediation_suggestion}
            </div>
          </section>
        )}

        {error && <div className="error">{error}</div>}
      </main>

      <footer>
        <small>
          &copy; {new Date().getFullYear()} Legal Emotion Analyzer &mdash; Powered by Next.js, Django, Hugging Face
        </small>
      </footer>
    </div>
  );
}
