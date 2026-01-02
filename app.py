import streamlit as st
import base64
import os
import random

# 1. CONFIGURARE PAGINĂ
st.set_page_config(page_title="LuxeSave Elite", page_icon="💎")

# CSS - Stilul Luxe (Inclusiv fundalul)
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
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(20px);
            padding: 20px; border-radius: 25px; border: 1px solid rgba(255,255,255,0.3);
            text-align: center; color: #1a1a1a;
        }}
        .price-tag {{
            color: #d32f2f; font-weight: 900; font-size: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# 2. INITIALIZARE SESIUNE (Sistemul de memorie)
if 'lista_cumparaturi' not in st.session_state:
    st.session_state.lista_cumparaturi = []

# 3. INTERFAȚĂ
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.title("LUXESAVE")
st.write("💎 ARCTIC ELITE INTELLIGENCE")

# --- SECȚIUNEA LISTĂ (Apare doar dacă ai produse) ---
if st.session_state.lista_cumparaturi:
    st.markdown("### 🛒 COȘUL TĂU:")
    total_plata = 0
    for produs in st.session_state.lista_cumparaturi:
        st.write(f"✅ {produs['nume']} ({produs['magazin']}) — {produs['pret']:.2f}€")
        total_plata += produs['pret']
    
    st.subheader(f"TOTAL: {total_plata:.2f}€")
    if st.button("🗑️ GOLEȘTE LISTA"):
        st.session_state.lista_cumparaturi = []
        st.rerun()
    st.markdown("---")

# --- CĂUTARE ---
cautare = st.text_input("", placeholder="Scrie ce vrei să cumperi (ex: Bier)...")

if cautare:
    # Simulăm ofertele
    pret_hofer = 0.45 if cautare.lower() == "bier" else round(random.uniform(0.7, 1.5), 2)
    pret_lidl = 0.49 if cautare.lower() == "bier" else round(random.uniform(0.7, 1.5), 2)

    # OFERTA 1: HOFER
    st.markdown(f"**HOFER** — <span class='price-tag'>{pret_hofer}€</span>", unsafe_allow_html=True)
    if st.button(f"ADĂUGĂ HOFER - {pret_hofer}€"):
        st.session_state.lista_cumparaturi.append({"nume": cautare, "magazin": "HOFER", "pret": pret_hofer})
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # OFERTA 2: LIDL
    st.markdown(f"**LIDL** — <span class='price-tag'>{pret_lidl}€</span>", unsafe_allow_html=True)
    if st.button(f"ADĂUGĂ LIDL - {pret_lidl}€"):
        st.session_state.lista_cumparaturi.append({"nume": cautare, "magazin": "LIDL", "pret": pret_lidl})
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
