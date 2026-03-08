import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from model_fetcher import get_free_models
from health_check import check_model_health
from router import SmartLLMRouter

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(
    page_title="Smart LLM Router",
    page_icon="🚀",
    layout="wide"
)

# st.title("🚀 Smart LLM Router Dashboard")

# Centered Title using HTML
st.markdown("<h1 style='text-align: center;'>🚀 Smart LLM Router Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Automated routing for open-source LLMs</p>", unsafe_allow_html=True)
# -------------------------------
# Session State
# -------------------------------
if "models" not in st.session_state:
    st.session_state.models = []
if "health_results" not in st.session_state:
    st.session_state.health_results = []

# -------------------------------
# System Controls (Side-by-Side)
# -------------------------------
# This creates the "line by line" horizontal layout for the main action buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🔎 Fetch Free Models", use_container_width=True):
        with st.spinner("Fetching..."):
            st.session_state.models = get_free_models()

with col2:
    if st.button("❤️ Run Health Check", use_container_width=True):
        if st.session_state.models:
            with st.spinner("Checking health..."):
                # Checking first 5 for speed
                st.session_state.health_results = [check_model_health(m) for m in st.session_state.models[:5]]
        else:
            st.warning("Please fetch models first.")

# -------------------------------
# Display Model Info (Optional collapse)
# -------------------------------
if st.session_state.models or st.session_state.health_results:
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        if st.session_state.models:
            with st.expander("📦 Available Models", expanded=False):
                for m in st.session_state.models[:10]:
                    st.write(f"✅ `{m}`")
    
    with info_col2:
        if st.session_state.health_results:
            with st.expander("✅ Health Status", expanded=False):
                for r in st.session_state.health_results:
                    color = "green" if r["healthy"] else "red"
                    st.markdown(f":{color}[{r['model']}] - {round(r['latency'], 2)}s")

# -------------------------------
# Interaction Area
# -------------------------------
st.divider()
st.subheader("💬 Ask Question")

# Model Selection Dropdown
selected_model = "Auto Smart Routing"
if st.session_state.models:
    selected_model = st.selectbox(
        "Select Specific Model (Optional)",
        options=["Auto Smart Routing"] + st.session_state.models
    )

prompt = st.text_input(
    "Enter Prompt",
    placeholder="Explain Artificial Intelligence simply..."
)

if st.button("🚀 Send Query", use_container_width=True):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        # Changed text as requested: "processing..hold on"
        with st.spinner("processing..hold on"):
            try:
                router = SmartLLMRouter()
                
                if selected_model != "Auto Smart Routing":
                    answer = router.ask_with_specific_model(prompt, selected_model)
                else:
                    answer = router.ask(prompt)

                # Printing response directly without extra status labels
                st.markdown("---")
                st.subheader("🤖 Response")
                st.write(answer)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")