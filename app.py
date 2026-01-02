import streamlit as st
import base64
import os
import random

# 1. SETĂRI PAGINĂ
st.set_page_config(page_title="LuxeSave Elite", page_icon="💎")

# 2. MEMORIE (SESSION STATE) - Aceasta este "inima" listei tale
if 'cos' not in st.session_state:
    st.session_state.cos = []

# 3. FUNDAL VULPE
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

img_b64 = get_base64("vulpe.jpg")

st.markdown(f"""
    <style>
        [data-testid="stHeader"] {{ display: none !important; }}
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{img_b64}");
            background-size: cover; background-attachment: fixed;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(25px);
            padding: 25px; border-radius: 30px; 
            border: 1px solid rgba(255,255,255,0.4);
            text-align: center; color: #000;
        }}
    </style>
""", unsafe_allow_html=True)

# 4. INTERFAȚĂ
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.title("💎 LUXESAVE")
st.write("ARCTIC ELITE INTELLIGENCE")

# --- AFIȘARE LISTĂ (Dacă avem ceva în ea) ---
if st.session_state.cos:
    st.markdown("### 🛒 LISTA TA ACTUALĂ:")
    total = 0
    for produs in st.session_state.cos:
        st.write(f"✅ {produs['nume']} — {produs['pret']:.2f}€")
        total += produs['pret']
    st.subheader(f"TOTAL: {total:.2f}€")
    
    if st.button("🗑️ GOLEȘTE TOT"):
        st.session_state.cos = []
        st.rerun()
    st.markdown("---")

# --- ZONA DE CĂUTARE ȘI ADĂUGARE ---
query = st.text_input("Ce cauți azi?", placeholder="Ex: Bier, Milch...")

if query:
    # Generăm prețuri fixe pentru sesiune
    pret_h = 0.45 if query.lower() == "bier" else 0.89
    pret_l = 0.49 if query.lower() == "bier" else 0.95

    st.write(f"Rezultate pentru: **{query}**")
    
    # Folosim butoane simple, dar cu logica de salvare forțată
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**HOFER**")
        st.markdown(f"## {pret_h}€")
        if st.button(f"ADĂUGĂ HOFER"):
            st.session_state.cos.append({"nume": f"{query} (Hofer)", "pret": pret_h})
            st.rerun()

    with col2:
        st.markdown(f"**LIDL**")
        st.markdown(f"## {pret_l}€")
        if st.button(f"ADĂUGĂ LIDL"):
            st.session_state.cos.append({"nume": f"{query} (Lidl)", "pret": pret_l})
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
