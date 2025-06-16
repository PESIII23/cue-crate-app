# CueCrate Backend

CueCrate is a backend service built with **FastAPI** and **Docker**. It provides robust API endpoints for interacting with the Spotify API, PostgreSQL, and Elasticsearch, making it easy to build music-related applications.

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/cuecrate.git
cd cuecrate
```

---

### 2. **Configure Environment Variables**

Create a `.env` file in the `backend/` directory with your Spotify credentials:

```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

You can use `.env.example` as a template.

---

### 3. **Run the Full Stack with Docker Compose (Recommended)**

This will start the backend, PostgreSQL, and Elasticsearch with a single command.

```sh
docker-compose up --build
```

- The FastAPI backend will be available at [http://localhost:8000](http://localhost:8000)
- PostgreSQL will be available on port `5432`
- Elasticsearch will be available on port `9200`

To stop all services, press `Ctrl+C` and then run:

```sh
docker-compose down
```

---

### 4. **Run the Backend Locally (Without Docker Compose)**

#### **Install dependencies**

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### **Start the server**

```sh
uvicorn app.main:app --reload
```

> **Note:** You will need to run PostgreSQL and Elasticsearch separately if you are not using Docker Compose.

---

## 📝 API Usage

- **Interactive API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Example Endpoints:**
  - `GET /spotify/search/artist?q=ARTIST_NAME` — Search for artists
  - `GET /spotify/search/track?q=TRACK_NAME` — Search for tracks

You can use tools like **curl**, **Postman**, or your browser to interact with these endpoints.

---

## 🛠️ Project Structure

```
cuecrate/
  backend/
    app/
      api/
        spotify_routes.py      # FastAPI endpoints for Spotify
      services/
        spotify.py             # Spotify API helper functions
        spotify_auth.py        # Spotify authentication logic
      main.py                  # FastAPI app setup
    requirements.txt
    Dockerfile
    .env.example
  docker-compose.yml
```

---

## 🧑‍💻 Development Guidelines

- **Environment Variables:**  
  Store sensitive credentials in `.env` (never commit this file).
- **Adding Endpoints:**  
  Place new API endpoints in `app/api/`.
- **Business Logic:**  
  Add Spotify or other service logic in `app/services/`.
- **Testing:**  
  Use the `/docs` endpoint for quick manual testing, or add automated tests as needed.

---

## 🐳 Useful Docker Commands

- **List images:**  
  `docker images`
- **List containers:**  
  `docker ps -a`
- **Stop a container:**  
  `docker stop <container_id>`
- **Remove a container:**  
  `docker rm <container_id>`
- **Stop all services:**  
  `docker-compose down`
- **Start all services:**  
  `docker-compose up --build`

---

## 📢 Notes & Best Practices

- **Never commit your `.env` file.**  
  Use `.env.example` to share variable names with collaborators.
- **For production deployments:**  
  Remove `--reload` from the Dockerfile CMD and review security settings for all services.
- **Need help?**  
  Open an issue or pull request on GitHub.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---
