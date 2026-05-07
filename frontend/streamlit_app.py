import streamlit as st

st.set_page_config(page_title="FinBridge AI")

st.title("FinBridge AI")
st.subheader("AI-Powered Alternative Credit Scoring")

st.header("Borrower Details")

bill_score = st.slider("Mobile Bill Consistency", 0, 100, 80)
ecommerce = st.slider("E-Commerce Reliability", 0, 100, 75)
location = st.slider("Location Stability", 0, 100, 90)

if st.button("Generate Credit Score"):
    score = int((bill_score + ecommerce + location) / 3 * 8)

    st.success(f"Alternative Credit Score: {score}")

    if score > 700:
        st.success("Loan Approved")
    else:
        st.error("Further Review Required")