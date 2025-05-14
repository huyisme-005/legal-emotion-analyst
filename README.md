# legal-emotion-analyst
# Legal Emotion Analyzer

A fullstack project that captures voice input, transcribes it, and analyzes emotions in legal conversations.  
Built with Next.js (frontend), Django REST Framework (backend), Docker, and Hugging Face Transformers for emotion detection.

## Features

- 🎤 Record voice from browser
- 🔗 Send audio to backend for transcription & emotion analysis
- 🤗 Backend uses Hugging Face Transformers for emotion detection
- 📊 Display emotion results with a modern UI
- 🐳 Easy deployment with Docker Compose or Netlify

## Quick Start

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- (Optional) Node.js and Python for local dev

### Run Fullstack with Docker

docker compose build
docker compose up

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend (API): [http://localhost:8000/api/analyze/](http://localhost:8000/api/analyze/)

### Deploy Frontend on Netlify

cd apps/frontend
npm install -g netlify-cli
npm install
npm run build
netlify deploy --prod

### Project Structure

- `apps/frontend/` - Next.js frontend (with custom HTML and CSS)
- `apps/backend/` - Django backend API (with Hugging Face Transformers)

## SECRET_KEY and Security

- `SECRET_KEY` is used by Django for cryptographic signing (sessions, cookies, CSRF, etc).
- **Never commit your real SECRET_KEY to version control.**
- In production, set it via the `DJANGO_SECRET_KEY` environment variable or a secrets manager.
- If you change the key, all signed data (sessions, password reset tokens) become invalid.

## Hugging Face Integration

- The backend uses the `transformers` library and loads a pre-trained emotion classification model from Hugging Face Hub.

---

## License

## Several problems
1. The frontend could record the audio, but still haven't been able to transcribe it.
2. Backend deployment hasn't been done yet.
3. Whenever the backend is run, the error "GET /favicon.ico HTTP/1.1" 500 Internal Server Error always occurs.

MIT