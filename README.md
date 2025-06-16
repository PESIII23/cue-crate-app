# CueCrate

CueCrate is a full-stack music application project. The backend is built with **FastAPI** and **Docker**, providing robust API endpoints for interacting with the Spotify API, PostgreSQL, and Elasticsearch. The frontend is built with **React**. This setup makes it easy to build, test, and deploy music-related applications.

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/cuecrate.git
cd cuecrate
```

---

### 2. **Configure Environment Variables**

1. **Duplicate the `.env.example` file in the `backend/` directory and rename it to `.env`:**

   **Mac/Linux:**
   ```sh
   cp backend/.env.example backend/.env
   ```

   **Windows (Command Prompt):**
   ```cmd
   copy backend\.env.example backend\.env
   ```

2. **Open `backend/.env` and replace the placeholder values with your actual credentials and configuration, as provided in the project Google Doc.**

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

**Mac/Linux:**
```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Windows (Command Prompt):**
```cmd
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### **Start the server**

```sh
uvicorn app.main:app --reload
```

> **Note:** You will need to run PostgreSQL and Elasticsearch separately if you are not using Docker Compose.

---

### 5. **Run the Frontend (React)**

**Mac/Linux/Windows:**
```sh
cd frontend
npm install
npm start
```
The frontend will typically be available at [http://localhost:3000](http://localhost:3000).

---

## 📝 API Usage

- **Interactive API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Example Endpoints:**
  - `GET /spotify/search/artist?query=ARTIST_NAME` — Search for artists
  - `GET /spotify/search/track?query=TRACK_NAME` — Search for tracks

You can use tools like **curl**, **Postman**, or your browser to interact with these endpoints.

---

## 🛠️ Project Structure

```
cuecrate/
  backend/
    app/
      routes/
        spotify_routes.py         # FastAPI endpoints for Spotify
      services/
        spotify_search_service.py # Spotify search logic
        spotify_auth_service.py   # Spotify authentication logic
      main.py                     # FastAPI app setup
      models.py                   # (if you have Pydantic models)
    requirements.txt
    Dockerfile
    .env.example
    .env
  frontend/
    src/
      components/
      App.jsx
      index.js
    package.json
    ...
  docker-compose.yml
  README.md
```

---

## 📦 Dependencies

### **Backend**
- fastapi
- uvicorn[standard]
- sqlalchemy
- asyncpg
- requests
- python-dotenv
- elasticsearch

### **Frontend**
- react
- react-dom
- react-router-dom
- axios
- (see `frontend/package.json` for full list)

---

## 🧑‍💻 Development Guidelines

- **Environment Variables:**  
  Store sensitive credentials in `.env` (never commit this file).
- **Adding Endpoints:**  
  Place new API endpoints in `app/routes/`.
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
