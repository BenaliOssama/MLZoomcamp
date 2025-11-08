import pickle

# Load the saved pipeline
with open('pipeline_v1.bin', 'rb') as f:
    model = pickle.load(f)

# Record to score
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Predict the probability of conversion (class 1)
proba = model.predict_proba([record])[0, 1]

print("Conversion probability:", round(proba, 3))

