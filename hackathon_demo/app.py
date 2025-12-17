import streamlit as st
import json
import pandas as pd
import time
import plotly.graph_objects as go
from fpdf import FPDF

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="BidMaster AI Enterprise", layout="wide", page_icon="⚡")

# --- CUSTOM CSS FOR "COMMAND CENTER" LOOK ---
st.markdown("""
<style>
    .main-header {font-size: 2rem; color: #1E1E1E; font-weight: 800;}
    .status-log {font-family: 'Courier New'; font-size: 0.8rem; color: #00FF00; background-color: #000; padding: 10px; height: 150px; overflow-y: scroll; border-radius: 5px;}
    .metric-box {border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: #fff; text-align: center;}
    .stButton>button {width: 100%; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

def generate_pdf(rfp_data, match_data, price_data):
    """Generates a physical PDF file for download"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="BidMaster AI - Automated Proposal Draft", ln=1, align='C')
    pdf.line(10, 20, 200, 20)
    pdf.ln(20)
    
    pdf.set_font("Arial", 'B', size=10)
    pdf.cell(200, 10, txt=f"Ref: {rfp_data['id']}", ln=1)
    
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Selected SKU: {match_data['SKU']}", ln=1)
    pdf.cell(200, 10, txt=f"Technical Match Score: {match_data['Match Score']}%", ln=1)
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', size=10)
    pdf.cell(200, 10, txt="Commercial Summary:", ln=1)
    for item in price_data:
        pdf.cell(200, 10, txt=f"{item['Item']}: {item['Cost (USD)']}", ln=1)
        
    return pdf.output(dest='S').encode('latin-1')

def simulate_agent_logs():
    """Simulates a live terminal log"""
    logs = st.empty()
    log_messages = [
        "[SYSTEM] Initializing Multi-Agent Swarm...",
        "[SALES_AGENT] Connecting to GOV_PORTAL_API...",
        "[SALES_AGENT] Found 14 active tenders. Filtering for 'Cables'...",
        "[SALES_AGENT] Target Acquired: GOV-PWR-2025-09",
        "[ORCHESTRATOR] Handing off to Technical Agent...",
        "[TECH_AGENT] Parsing PDF Requirement Specs...",
        "[TECH_AGENT] Vectorizing text embedding...",
        "[TECH_AGENT] Querying ChromaDB (15,000 SKUs)...",
        "[TECH_AGENT] Calculating Cosine Similarity...",
        "[TECH_AGENT] GAP DETECTED: Voltage rating mismatch.",
        "[PRICING_AGENT] Fetching Copper LME Index Live Price...",
        "[SYSTEM] Optimization Complete."
    ]
    processed_logs = ""
    for msg in log_messages:
        processed_logs += f"{msg}\n"
        logs.markdown(f'<div class="status-log">{processed_logs.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
        time.sleep(0.3) 

# --- DATA LOADING (Reusing your files) ---
def load_data():
    try:
        with open('data/rfp_sample.txt', 'r') as f: rfp_text = f.read()
        with open('data/datasheet_A.json', 'r') as f: sku_a = json.load(f)
        with open('data/datasheet_B.json', 'r') as f: sku_b = json.load(f)
        pricing = pd.read_csv('data/pricing.csv')
        return rfp_text, sku_a, sku_b, pricing
    except:
        return None, None, None, None

# --- MAIN UI ---

# Sidebar: Live System Status
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712009.png", width=50)
    st.markdown("### Agent Status")
    if 'scan_run' not in st.session_state:
        st.info("System Standby")
    else:
        st.success("Agents Active")
    
    st.markdown("---")
    st.markdown("**Active Agents:**")
    st.checkbox("Sales Agent (Scanner)", value=True, disabled=True)
    st.checkbox("Tech Agent (RAG)", value=True, disabled=True)
    st.checkbox("Pricing Agent (ERP)", value=True, disabled=True)

st.markdown('<div class="main-header">⚡ BidMaster AI <span style="font-size:1rem; color:grey"> | Enterprise Edition</span></div>', unsafe_allow_html=True)

# Main Action Button
if st.button("🚀 EXECUTE AUTONOMOUS WORKFLOW"):
    st.session_state['scan_run'] = True
    simulate_agent_logs()

if 'scan_run' in st.session_state:
    rfp_text, sku_a, sku_b, pricing_df = load_data()
    
    # Create Tabs for a "Complex" UI feel
    tab1, tab2, tab3 = st.tabs(["📊 Executive Dashboard", "🔧 Technical Analysis", "💰 Commercials & Export"])
    
    # --- TAB 1: DASHBOARD ---
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="RFP Match Confidence", value="92%", delta="High Probability")
        with col2:
            st.metric(label="Estimated Margin", value="18.5%", delta="+2.1% vs Avg")
        with col3:
            st.metric(label="Response Time", value="4.2s", delta="-99% vs Manual")
            
        st.markdown("### 🏆 Win Probability Model")
        # Cool Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 85,
            title = {'text': "AI Win Prediction Score"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#FFC20E"},
                     'steps': [
                         {'range': [0, 50], 'color': "lightgray"},
                         {'range': [50, 80], 'color': "gray"}],
                     'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
        st.plotly_chart(fig, use_container_width=True)

    # --- TAB 2: TECHNICAL ---
    with tab2:
        st.markdown("### 🔍 Semantic Spec Matching")
        
        # Comparison Matrix (The "Smart" Table)
        st.info("The AI extracted 12 parameters. Below is the automated comparison.")
        
        comp_data = {
            "Parameter": ["Voltage", "Conductor", "Insulation", "Armour", "Sheath Type"],
            "RFP Requirement": ["1100 V", "Copper", "XLPE", "Strip", "FRLS PVC"],
            "Best Match (Internal SKU)": ["1100 V", "Copper", "XLPE", "Galv. Steel", "FRLS PVC"],
            "Status": ["✅ Match", "✅ Match", "✅ Match", "⚠️ Partial", "✅ Match"]
        }
        df_comp = pd.DataFrame(comp_data)
        
        # Color coding function
        def color_status(val):
            color = '#d4edda' if 'Match' in val else '#f8d7da'
            return f'background-color: {color}'

        st.dataframe(df_comp.style.applymap(color_status, subset=['Status']), use_container_width=True)
        
        st.markdown("#### ⚠️ Gap Analysis Report")
        with st.expander("View Detected Deviations", expanded=True):
            st.warning("**Deviation 1:** RFP requests 'Strip' Armour. Standard SKU uses 'Galvanized Steel'.")
            st.caption("AI Recommendation: Submit with deviation note. Historical acceptance rate for this deviation is 95%.")

    # --- TAB 3: COMMERCIALS ---
    with tab3:
        st.markdown("### 💸 Dynamic Pricing Engine")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            # Pricing Table
            mat_cost = 450 * 5000
            test_cost = 1500
            total = mat_cost + test_cost
            
            p_data = [
                {"Item": "Cable Supply (5km)", "Cost (USD)": f"${mat_cost:,}"},
                {"Item": "Testing & Logistics", "Cost (USD)": f"${test_cost:,}"},
                {"Item": "TOTAL PROPOSAL VALUE", "Cost (USD)": f"${total:,}"}
            ]
            st.table(pd.DataFrame(p_data))
            
        with col2:
            st.markdown("#### Actions")
            # PDF Download Button (The Real "Output")
            pdf_bytes = generate_pdf({'id': 'GOV-PWR-2025-09'}, {'SKU': sku_a['sku_id'], 'Match Score': 100}, p_data)
            st.download_button(
                label="📄 Download Official PDF Bid",
                data=pdf_bytes,
                file_name="Bid_Proposal_Draft.pdf",
                mime="application/pdf"
            )
            st.button("📧 Email to Sales Manager")