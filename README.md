# CueCrate Backend

This is the backend for CueCrate, built with FastAPI and Docker. It provides API endpoints for interacting with the Spotify API and other services.

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/cuecrate.git
cd cuecrate/backend
```

---

### 2. **Set Up Environment Variables**

Create a `.env` file in the `backend/` directory with your Spotify credentials:

```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

---

### 3. **Run with Docker (Recommended)**

#### **Build the Docker image**

From the project root (`cuecrate/`):

```sh
docker build -f backend/Dockerfile -t cuecrate-backend backend/
```
Or from inside the `backend/` folder:
```sh
docker build -t cuecrate-backend .
```

#### **Run the Docker container**

```sh
docker run --env-file .env -p 8000:8000 cuecrate-backend
```

---

### 4. **Run Locally (Without Docker)**

#### **Install dependencies**

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### **Start the server**

```sh
uvicorn app.main:app --reload
```

---

## 📝 API Usage

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Example endpoints:**
  - `GET /spotify/search/artist?q=ARTIST_NAME`
  - `GET /spotify/search/track?q=TRACK_NAME`

---

## 🛠️ Project Structure

```
backend/
  app/
    api/
      spotify_routes.py   # FastAPI endpoints
    services/
      spotify.py          # Spotify API helper functions
      spotify_auth.py     # Spotify authentication logic
    main.py               # FastAPI app setup
  requirements.txt
  Dockerfile
  .env.example
```

---

## 🧑‍💻 Development

- Edit `.env` for your environment variables.
- Add new endpoints in `app/api/`.
- Add new Spotify logic in `app/services/`.

---

## 🐳 Docker Commands

- **List images:** `docker images`
- **List containers:** `docker ps -a`
- **Stop a container:** `docker stop <container_id>`
- **Remove a container:** `docker rm <container_id>`

---

## 📢 Notes

- Do **not** commit your `.env` file. Use `.env.example` for sharing variable names.
- For any issues, please open an issue or pull request.

---
