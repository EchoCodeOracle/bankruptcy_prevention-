import streamlit as st
import pickle

# Load the trained model
with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)


def predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk, threshold=0.5):
    overall_score = (industrial_risk + management_risk + financial_flexibility + credibility + competitiveness + operating_risk) / 6.0
    if overall_score < threshold:
        return "**Bankruptcy [0]**"
    else:
        return "**Non-Bankruptcy [1]**"

def main():
    st.title('Bankruptcy Detector')

    st.write("This app predicts whether a company is at risk of bankruptcy or not.")

    # Sidebar inputs
    st.sidebar.header('Input Parameters')
    industrial_risk = st.sidebar.selectbox('Industrial Risk', [0.0, 0.5, 1.0], index=1)
    management_risk = st.sidebar.selectbox('Management Risk', [0.0, 0.5, 1.0], index=1)
    financial_flexibility = st.sidebar.selectbox('Financial Flexibility', [0.0, 0.5, 1.0], index=1)
    credibility = st.sidebar.selectbox('Credibility', [0.0, 0.5, 1.0], index=1)
    competitiveness = st.sidebar.selectbox('Competitiveness', [0.0, 0.5, 1.0], index=1)
    operating_risk = st.sidebar.selectbox('Operating Risk', [0.0, 0.5, 1.0], index=1)
    threshold = st.sidebar.selectbox('Threshold', [0.0, 0.5, 1.0], index=1)


    # Prediction
    prediction = predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk, threshold)
    st.write(f"Prediction: **{prediction}**")


if __name__ == '__main__':
    main()
