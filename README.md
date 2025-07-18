# Smile Classification Project

## Overview
This project uses a Voting Classifier to classify images as "Smiling" or "Not Smiling." The Voting Classifier combines predictions from:
- Support Vector Classifier (SVC)
- Decision Tree Classifier
- Random Forest Classifier

The backend is implemented using FastAPI, with MySQL as the database for storing classification history.

---

## Features
- **Image Classification**: Upload images to classify them as "Smiling" or "Not Smiling."
- **History Tracking**: View a history of classified images.
- **Database Integration**: Persistent storage of classification results using MySQL.
- **Containerized Deployment**: Easy deployment using Docker and Docker Compose.

---

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project-root
2. Build and start the containers:
   ```bash
   docker-compose up --build
3. Access the application in your browser at:
   ```bash
   http://127.0.0.1:5000
4. To stop the containers:
   ```bash
   docker-compose down

## API Endpoints

### 1. Home Page
- **URL**: `/`
- **Method**: `GET`
- **Description**: Displays the home page.

### 2. Classify Image
- **URL**: `/classify`
- **Method**: `POST`
- **Description**: Upload an image and classify it as "Smiling" or "Not Smiling."

### 3. View History
- **URL**: `/history`
- **Method**: `GET`
- **Description**: Displays the history of classified images.

---

## Technical Details

### Model Training
- The model is trained using a dataset of smiling and non-smiling images.
- Images are resized to **64x64 pixels** and scaled using **StandardScaler**.
- The Voting Classifier combines predictions from:
  - Support Vector Classifier (SVC)
  - Decision Tree Classifier
  - Random Forest Classifier
- The trained model and scaler are saved as pickle files for inference.

### Database
- **MySQL** is used for persistent storage of classification history.
- The database runs on port **3306**.
- Docker Compose sets up a MySQL container with the following credentials:
  - **Root Password**: `root`
  - **Database Name**: `smiledatabase`

### Containerization
- The application is containerized using **Docker**.
- The `docker-compose.yml` file sets up the FastAPI application and MySQL database.

---

## Technologies Used
- **Backend**: FastAPI
- **Machine Learning**: Scikit-learn
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Containerization**: Docker, Docker Compose

---

## Future Enhancements
1. Extend support for additional image classifications.
2. Add user authentication for personalized history.
3. Improve model performance using advanced deep learning techniques.

---

## License
This project is licensed under the MIT License.
