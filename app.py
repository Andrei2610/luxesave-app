import streamlit as st
import base64
import os
import random

# 1. CONFIGURARE PAGINĂ
st.set_page_config(page_title="LuxeSave Elite", page_icon="💎", layout="centered")

st.markdown("""
    <style>
        [data-testid="stHeader"] { display: none !important; }
        header { visibility: hidden !important; }
        .main .block-container { padding-top: 0rem !important; margin-top: -30px !important; }
        footer { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# 2. FUNDAL VULPE
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

img_b64 = get_base64("vulpe.jpg")

# 3. DESIGN
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{img_b64}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .glass-card {{
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(40px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 30px; padding: 20px; text-align: center; margin-top: 30px;
    }}
    .store-box {{
        background: white; padding: 15px; border-radius: 15px; margin: 10px 0;
        display: flex; justify-content: space-between; align-items: center;
        border-left: 5px solid #c5a059;
    }}
</style>
""", unsafe_allow_html=True)

# 4. SESIUNE (Aici stocăm produsele)
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 5. INTERFAȚĂ
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<h1 style="color:#1a1a1a; letter-spacing:5px;">LUXESAVE</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#c5a059; font-weight:bold;">ARCTIC ELITE</p>', unsafe_allow_html=True)

# AFIȘARE LISTĂ (Dacă există produse)
if st.session_state.cart:
    st.markdown("---")
    st.markdown("### 🛒 LISTA TA:")
    total = 0
    for i, item in enumerate(st.session_state.cart):
        st.markdown(f"**{item['prod']}**: {item['price']:.2f}€")
        total += item['price']
    st.markdown(f"## TOTAL: {total:.2f}€")
    if st.button("Șterge tot"):
        st.session_state.cart = []
        st.rerun()
    st.markdown("---")

# CĂUTARE
query = st.text_input("", placeholder="Ce cauți astăzi?")

if query:
    # Generăm 2 oferte de test
    offerte = [
        {"mag": "HOFER", "pret": random.uniform(0.5, 2.0)},
        {"mag": "LIDL", "pret": random.uniform(0.5, 2.0)}
    ]
    
    for o in offerte:
        col_text, col_add = st.columns([3, 1])
        with col_text:
            st.markdown(f"""<div style="background:white; padding:10px; border-radius:10px;">
                <b>{o['mag']}</b>: {o['pret']:.2f}€
            </div>""", unsafe_allow_html=True)
        with col_add:
            # Butonul care adaugă în listă
            if st.button(f"Adaugă", key=f"btn_{o['mag']}_{o['pret']}"):
                st.session_state.cart.append({"prod": query, "price": o['pret']})
                st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
