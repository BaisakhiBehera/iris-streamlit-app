import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('logistic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Map numerical prediction to species name
species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Show top image
st.image("iris_flower.jpg", width=700, caption="Iris Flower Species")

# Title and subtitle
st.markdown('<div class="title">Iris Flower Species Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Powered by Machine Learning · Built with Streamlit</div>', unsafe_allow_html=True)

# Input sliders
st.markdown("### Enter Flower Measurements")
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Predict Button
if st.button("Predict Species"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    predicted_species = species[prediction[0]]

    st.markdown(f"""
        <div class="result-box">
            🌸 Predicted Species: <br><br> <span style="font-size: 26px;">{predicted_species}</span>
        </div>
    """, unsafe_allow_html=True)

# Sidebar Info
st.sidebar.title("About the App")
st.sidebar.info("""
This app uses a **Logistic Regression** model  
trained on the classic **Iris dataset** to predict  
the species of a flower based on its measurements.

- **Model**: Logistic Regression  
- **Accuracy**: ~97.78%  
- **Author**: Baisakhi  
""")
