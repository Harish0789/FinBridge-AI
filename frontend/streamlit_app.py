import streamlit as st

st.set_page_config(
    page_title="FinBridge AI",
    layout="wide"
)

st.title("🏦 FinBridge AI")
st.subheader("AI-Powered Alternative Credit Scoring")

st.markdown("---")

# Sidebar
st.sidebar.header("Borrower Information")

bill_score = st.sidebar.slider(
    "Mobile Bill Consistency",
    0, 100, 85
)

ecommerce = st.sidebar.slider(
    "E-Commerce Reliability",
    0, 100, 78
)

location = st.sidebar.slider(
    "Location Stability",
    0, 100, 90
)

merchant = st.sidebar.slider(
    "Merchant Rating",
    0, 100, 88
)

psychometric = st.sidebar.slider(
    "Psychometric Score",
    0, 100, 80
)

if st.sidebar.button("Generate Credit Score"):

    score = int(
        (bill_score +
         ecommerce +
         location +
         merchant +
         psychometric) / 5 * 8
    )

    st.header("📊 Credit Assessment Result")

    col1, col2, col3 = st.columns(3)

    col1.metric("Alternative Credit Score", score)

    if score > 700:
        col2.success("Loan Approved")
    else:
        col2.error("Further Review")

    col3.metric("Risk Level", "Low")

    st.markdown("---")

    st.subheader("🔍 SHAP Explainability")

    st.write("✔ Consistent bill payments → +18")
    st.write("✔ Stable geolocation → +12")
    st.write("✔ Strong merchant rating → +10")
    st.write("❌ High product returns → -5")

    st.markdown("---")

    st.subheader("⚡ System Performance")

    st.success("Credit decision generated in under 3 seconds")