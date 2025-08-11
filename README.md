# 😄 SmileVision_AI_Smile_Classification

## 📌 Overview
This project uses a Voting Classifier to classify images as "Smiling" or "Not Smiling." The Voting Classifier combines predictions from:
- Support Vector Classifier (SVC)
- Decision Tree Classifier
- Random Forest Classifier

The backend is implemented using FastAPI, with MySQL as the database for storing classification history.

---

## ✨ Features
- **Image Classification**: Upload images to classify them as "Smiling" or "Not Smiling."
- **History Tracking**: View a history of classified images.
- **Database Integration**: Persistent storage of classification results using MySQL.
- **Containerized Deployment**: Easy deployment using Docker and Docker Compose.

---

## 🗂 Project Structure

```text
Smile_classifier/
├── env/                                  # Virtual environment (optional, not in repo)
├── smile_classifier_sklearn/
│   ├── app/                              # Application-specific modules (currently empty)
│   ├── data/                             # Dataset storage (empty or raw data files)
│   ├── model/                            # Saved trained models & scalers
│   │   ├── scaler.pkl                    # StandardScaler for preprocessing
│   │   └── smile_classifier.pkl          # Trained Voting Classifier model
│   ├── src/                              # Source code
│   │   ├── model/                        # Model-specific helper code (empty for now)
│   │   └── smile_classifier_sklearn/     # Core backend logic
│   │       ├── database.py               # MySQL connection & operations
│   │       ├── inference.py              # Model inference (predict smile/not smile)
│   │       └── smile_classifier.py       # Model training code
│   ├── static/                           # Frontend static assets
│   │   ├── css/                          # Stylesheets
│   │   ├── images/                       # Image assets (icons, logos)
│   │   └── uploads/                      # Uploaded user images
│   ├── templates/                        # HTML pages
│   │   ├── classify.html                 # Image upload & classification
│   │   ├── history.html                  # Classification history
│   │   ├── home.html                     # Homepage
│   │   └── navbar.html                   # Navigation bar partial
│   ├── __init__.py                       # Marks package
│   ├── docker-compose.yml                # Docker Compose configuration
│   ├── Dockerfile                        # Docker build for FastAPI app
│   ├── requirements.txt                  # Python dependencies
│   └── README.md                         # Project documentation
├── main.py                               # FastAPI entry point

```

--- 

## 🚀 Getting Started

### Prerequisites
- 🐳 [Docker](https://www.docker.com/)
- 🐙 [Docker Compose](https://docs.docker.com/compose/)

### 📤 Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project-root
2. Build and start the containers:
   ```bash
   docker-compose up --build
3. 🌐 Access the application in your browser at:
   ```bash
   http://127.0.0.1:5000
4. To stop the containers:
   ```bash
   docker-compose down

---

## 📡 API Endpoints

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

### 🧠 Model Training
- The model is trained using a dataset of smiling and non-smiling images.
- Images are resized to **64x64 pixels** and scaled using **StandardScaler**.
- The Voting Classifier combines predictions from:
  - Support Vector Classifier (SVC)
  - Decision Tree Classifier
  - Random Forest Classifier
- The trained model and scaler are saved as pickle files for inference.

### 🗄 Database
- **MySQL** is used for persistent storage of classification history.
- The database runs on port **3306**.
- Docker Compose sets up a MySQL container with the following credentials:
  - **Root Password**: `root`
  - **Database Name**: `smiledatabase`

### 🐳 Containerization
- The application is containerized using **Docker**.
- The `docker-compose.yml` file sets up the FastAPI application and MySQL database.

---

## 📤 Technologies Used
- **Backend**: FastAPI
- **Machine Learning**: Scikit-learn
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Containerization**: Docker, Docker Compose

---

## 📸 Screenshots

### Figure 1 : This displays home page of SmileVision_AI

<img width="1364" height="501" alt="home" src="https://github.com/user-attachments/assets/7577223e-9418-4371-bd42-a48da3c0e0f1" />

### Figure 2 : User can upload images to classify smile or not

<img width="1365" height="609" alt="classify" src="https://github.com/user-attachments/assets/57550f82-9342-4d15-bec8-d44de3855421" />

### Figure 3 : User uploads image and shows classification result

<img width="557" height="605" alt="sample" src="https://github.com/user-attachments/assets/0e21718c-0d1a-4b7b-a8b3-fb6fea38a2cc" />

### Figure 4 : This displays history page with image, classification history and timestamp

<img width="1365" height="423" alt="history" src="https://github.com/user-attachments/assets/7f2c4f7a-f3c5-4c15-8a05-f213b722562e" />

---

## 🔮 Future Enhancements
1. 📱  Extend support for additional image classifications.
2. 🔑 Add user authentication for personalized history.
3. 🤖 Upgrade to deep learning (CNN) for higher accuracy.
4. 📱  Improve model performance using advanced deep learning techniques.
5. ☁️ Cloud deployment with CI/CD.

---

## 📜 License
This project is licensed under the MIT License.

