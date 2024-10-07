# 🎯 **Flask OpenAI Assignment** 🚀

Welcome to the **Flask OpenAI Assignment** repository! This project demonstrates a containerized Flask application that interacts with a PostgreSQL database, powered by **Docker**. It includes a simple question-answering API, database integration using **SQLAlchemy**, and automated database migrations via **Alembic**. Unit tests are also implemented to ensure the robustness of the `/ask` API endpoint. 💪

---

## 🔥 **Key Features** 🔥
- 🌐 **REST API**: A `/ask` endpoint that processes questions and responds with a mocked answer.
- 🐳 **Fully Dockerized**: The entire stack (Flask app and PostgreSQL) runs inside Docker containers.
- 🗃️ **Database Integration**: PostgreSQL database with SQLAlchemy ORM for handling queries and persistence.
- 🚀 **Alembic Migrations**: Schema migrations handled effortlessly with Alembic.
- 🧪 **Unit Tests**: Robust unit tests for the `/ask` API, ensuring high code quality and reliability.
- 📈 **Scalable and Secure**: Easily scalable via Docker and secure with environment variable management.

---

## ⚙️ **Tech Stack** 🛠️
- **Flask**: Web framework for Python
- **PostgreSQL**: Relational database management system
- **SQLAlchemy**: ORM for handling database operations
- **Alembic**: Database migration tool
- **Docker**: Containerization for application and database
- **Pytest**: Testing framework for unit tests

---

## 📂 **Project Structure**
Here’s an overview of the project’s main files and directories:

```plaintext
📦 flask-openai-assignment
├── 📂 migrations            # Alembic migration files for database
├── 📂 tests                 # Unit tests for the app
├── 📄 Dockerfile            # Docker configuration for the Flask app
├── 📄 docker-compose.yml    # Docker Compose configuration to orchestrate containers
├── 📄 requirements.txt      # Python dependencies
├── 📄 app.py                # Main Flask application file
├── 📄 models.py             # Database models for SQLAlchemy
└── 📄 README.md             # Project documentation
```

---

## 🚀 **Getting Started** 🛠️

To get this project up and running on your local machine, follow the instructions below:

### **1. Clone the Repository**
```bash
git clone https://github.com/IbraheemGanayim/flask-openai-assignment.git
cd flask-openai-assignment
```

### **2. Set Up the Environment Variables**
- Create a `.env` file in the root directory and add the following:
  ```plaintext
  OPENAI_API_KEY=your_openai_api_key_here
  ```

### **3. Build and Run the Docker Containers**
Ensure that Docker is installed and running on your machine, then run:
```bash
docker-compose up --build
```
This command will:
- Build the Flask application container.
- Spin up the PostgreSQL database container.
- Automatically apply any database migrations using Alembic.

### **4. Access the Application**
- Once everything is up and running, the API will be accessible at:
  - **Flask App**: [http://localhost:5000](http://localhost:5000)
  
  Test the `/ask` endpoint by sending a **POST** request:
  ```bash
  curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is AI?"}'
  ```

---

## 🧪 **Running Tests** 🧪

To ensure everything works as expected, you can run unit tests inside the Flask container.

1. **Enter the Flask container**:
   ```bash
   docker exec -it flask-openai-assignment-web-1 /bin/sh
   ```

2. **Run the tests**:
   ```bash
   pytest
   ```

---

## 🔄 **Database Migrations**

Alembic is used to handle database migrations. You can generate and apply new migrations with the following commands:

1. **Create a new migration**:
   ```bash
   alembic revision --autogenerate -m "your migration message"
   ```

2. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

---

## 📊 **Project Workflow** 📊

This project follows a logical development workflow:
1. **Flask App Creation**: Basic Flask app setup with `/ask` endpoint.
2. **Docker Integration**: Dockerized the application for easy deployment and testing.
3. **PostgreSQL Integration**: Set up the PostgreSQL database with SQLAlchemy.
4. **Alembic Migrations**: Handled schema changes via Alembic migrations.
5. **Unit Testing**: Added unit tests for the API functionality to ensure correctness.
6. **Dockerized Testing**: Configured Docker to support running unit tests inside containers.

---

## 🛠️ **API Endpoints**

- **POST** `/ask`
  - **Description**: Submit a question and receive a mocked answer.
  - **Request**:
    ```json
    {
      "question": "What is AI?"
    }
    ```
  - **Response**:
    ```json
    {
      "question": "What is AI?",
      "answer": "This is a mocked response for: What is AI?"
    }
    ```

---

## 🔍 **Future Improvements**
- 🔒 **Authentication**: Add JWT-based authentication for API access.
- 📈 **Real Answers**: Integrate real answers using OpenAI API for dynamic responses.
- 🌐 **Frontend Interface**: Develop a simple UI using React or another frontend framework to interact with the API.

---

## 🙌 **Contributing**
Feel free to fork the repository, submit pull requests, or report issues! Contributions are welcome and appreciated. 🌟

---

### 🎉 **Thank You for Checking Out the Project!** 🎉
Feel free to reach out if you have any questions! 😊

---

### 🖥️ **Contact**
- **GitHub**: [Ibraheem Ganayim](https://github.com/IbraheemGanayim)
- **Email**: Ganayim.Ibraheem@gmail.com

---

Let me know if you'd like any additional changes or enhancements! 😄