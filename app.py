import streamlit as st
import numpy as np
import joblib

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

def load_model(file_path):
    try:
        model = joblib.load(file_path)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

model = load_model('credit_card_model.pkl')

def predict_fraud(input_data):
    # Convert input data to numpy array and reshape it
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

st.title('Credit Card Fraud Detection')
st.write("""
# Predict whether a transaction is normal or fraudulent
""")
user_input = st.text_area('Enter the transaction details separated by commas:', '')

if st.button('Predict'):
    # Check if the model is loaded
    if model is not None:
        try:
            input_data = [float(x) for x in user_input.split(',')]
            if len(input_data) == 29:
                prediction = predict_fraud(input_data)
                if prediction == 1:
                    st.error('This transaction is predicted to be Fraudulent.')
                else:
                    st.success('This transaction is predicted to be Normal.')
            else:
                st.error(f'Expected 29 features, but got {len(input_data)}. Please check your input.')
        except ValueError:
            st.error('Invalid input. Please ensure all values are numbers separated by commas.')
    else:
        st.error('Model could not be loaded. Please check the model file.')


# sample input to test the model: 0.0, -1.3598071336738, -0.0727811733098497, 2.53634673796914, 1.37815522427443, -0.338320769942518, 0.462387777762292, 0.239598554061257, 0.0986979012610507, 0.363786969611213, 0.0907941719789316, -0.551599533260813, -0.617800855762348, -0.991389847235408, -0.311169353699879, 1.46817697209427, -0.470400525259478, 0.207971241929242, 0.0257905801985591, 0.403992960255733, 0.251412098239705, -0.018306777944153, 0.277837575558899, -0.110473910188767, 0.0669280749146731, 0.128539358273528, -0.189114843888824, 0.133558376740387, -0.0210530534538215