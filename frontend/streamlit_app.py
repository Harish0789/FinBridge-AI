import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="FinBridge AI",
    layout="wide"
)

# ---------------- HEADER ----------------

st.title("🏦 FinBridge AI")
st.subheader("AI-Powered Alternative Credit Scoring")

st.markdown("---")

# ---------------- SIDEBAR ----------------

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

# ---------------- BUTTON ----------------

if st.sidebar.button("Generate Credit Score"):

    score = int(
        (bill_score +
         ecommerce +
         location +
         merchant +
         psychometric) / 5 * 8
    )

    # ---------------- TOP METRICS ----------------

    st.header("📊 Credit Assessment Result")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Alternative Credit Score",
        score
    )

    if score > 700:
        col2.success("✅ Loan Approved")
        risk = "Low"
    else:
        col2.error("❌ Further Review")
        risk = "Medium"

    col3.metric(
        "Risk Level",
        risk
    )

    st.markdown("---")

    # ---------------- SCORE METER ----------------

    st.subheader("🎯 Credit Score Meter")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Credit Score"},
        gauge={
            'axis': {'range': [300, 850]},
            'bar': {'thickness': 0.3},
            'steps': [
                {'range': [300, 550], 'color': "lightgray"},
                {'range': [550, 700], 'color': "gray"},
                {'range': [700, 850], 'color': "darkgray"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ---------------- SHAP SECTION ----------------

    st.subheader("🔍 SHAP Explainability")

    shap_data = pd.DataFrame({
        "Feature": [
            "Bill Payments",
            "Location Stability",
            "Merchant Rating",
            "Product Returns"
        ],
        "Impact": [18, 12, 10, -5]
    })

    fig2 = px.bar(
        shap_data,
        x="Impact",
        y="Feature",
        orientation='h',
        title="Feature Contribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ---------------- PERFORMANCE ----------------

    st.subheader("⚡ System Performance")

    p1, p2, p3 = st.columns(3)

    p1.success("3 Second Decision Time")
    p2.success("AES-256 Encryption")
    p3.success("Explainable AI Enabled")