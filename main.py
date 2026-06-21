import streamlit as st
from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()

st.set_page_config(
    page_title="AI Stock Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Stock Analysis Dashboard")
st.caption("Powered by CrewAI + Gemini")

stock = st.text_input(
    "Enter Stock Ticker",
    placeholder="AAPL, TSLA, NVDA, MSFT"
)

if st.button("Analyze", use_container_width=True):

    if stock == "":
        st.warning("Please enter a stock ticker.")
    else:

        with st.spinner("Fetching live market data..."):

            result = stock_crew.kickoff(
                inputs={"stock": stock.upper()}
            )

        st.success("Analysis Completed ✅")

        st.divider()

        st.subheader(f"📊 Analysis for {stock.upper()}")

        st.markdown(
            f"""
<div style='background-color:#F8F9FA;padding:20px;border-radius:12px;border:1px solid #E5E5E5;'>

{result.raw}

</div>
""",
            unsafe_allow_html=True
        )