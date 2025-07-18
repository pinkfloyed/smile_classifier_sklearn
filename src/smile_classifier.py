import os
import cv2
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

data_dir = r"D:\smile\data"
img_size = (64, 64)
classes = {"non_smile": 0, "smile": 1}

def save_as_jpg(img_path, output_dir):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error reading image: {img_path}")
        return None
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(img_path))[0] + ".jpg")
    cv2.imwrite(output_path, img)
    return output_path

def load_data(data_dir):
    data = []
    labels = []
    output_dir = os.path.join(data_dir, "converted")
    os.makedirs(output_dir, exist_ok=True) 
    for label, class_value in classes.items():
        class_dir = os.path.join(data_dir, label)
        if not os.path.isdir(class_dir):
            print(f"Directory {class_dir} does not exist!")
            continue
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            img_path = save_as_jpg(img_path, output_dir)
            if img_path is None:
                continue
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, img_size)
                data.append(img.flatten())
                labels.append(class_value)
    return np.array(data), np.array(labels)

print("Loading data...")
X, y = load_data(data_dir)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


svm_clf = SVC(kernel='linear', random_state=42)
dt_clf = DecisionTreeClassifier(random_state=42)
rf_clf = RandomForestClassifier(random_state=42)

voting_clf = VotingClassifier(estimators=[
    ('svm', svm_clf),
    ('decision_tree', dt_clf),
    ('random_forest', rf_clf)
], voting='hard')

print("Training model...")
voting_clf.fit(X_train, y_train)

print("Evaluating model...")
y_pred = voting_clf.predict(X_test)
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

os.makedirs("model", exist_ok=True)
with open("model/smile_classifier.pkl", "wb") as model_file:
    pickle.dump(voting_clf, model_file)

with open("model/scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Voting Classifier and scaler saved as 'model/smile_classifier.pkl' and 'model/scaler.pkl'.")
