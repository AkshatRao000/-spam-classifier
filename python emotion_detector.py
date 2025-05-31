import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('emotion_dataset.csv')

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['Text'])
y = data['Emotion']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test prediction
input_text = ["I can't stop crying"]
input_vec = vectorizer.transform(input_text)
prediction = model.predict(input_vec)

print("Detected Emotion:", prediction[0])
