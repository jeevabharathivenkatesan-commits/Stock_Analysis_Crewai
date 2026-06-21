import streamlit as st
from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Stock Analyzer",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("📈 AI Stock Analysis Dashboard")
st.caption("Powered by CrewAI + Gemini")

# -----------------------------
# INPUT
# -----------------------------
stock = st.text_input(
    "Enter Stock Ticker",
    placeholder="AAPL, TSLA, NVDA, MSFT"
)

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze", use_container_width=True):

    if not stock:
        st.warning("Please enter a stock ticker.")
        st.stop()

    try:

        with st.spinner("Fetching market data and generating analysis..."):

            result = stock_crew.kickoff(
                inputs={
                    "stock": stock.upper()
                }
            )

        st.success("Analysis Completed ✅")

        st.divider()

        st.subheader(f"📊 Analysis for {stock.upper()}")

        # -----------------------------
        # DISPLAY REPORT
        # -----------------------------
        with st.container(border=True):

            st.markdown(result.raw)

        # -----------------------------
        # DEBUG SECTION (Optional)
        # -----------------------------
        with st.expander("🔍 Debug Output"):

            st.write("Result Type:")
            st.write(type(result.raw))

            st.write("Raw Output:")
            st.code(result.raw)

    except Exception as e:

        st.error("Error while generating analysis")
        st.exception(e)
