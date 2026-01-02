import streamlit as st
import base64
import os
import random
import urllib.parse

# 1. CONFIGURARE PAGINĂ (Fără bară albă)
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

# 3. DESIGN LIQUID GLASS
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{img_b64}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .glass-card {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(45px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 35px; padding: 20px; text-align: center; margin-top: 50px;
    }}
    .stTextInput > div > div > input {{
        background: rgba(255, 255, 255, 0.5) !important;
        color: #000 !important; border-radius: 0px !important; height: 50px !important; text-align: center !important;
    }}
    .store-item {{
        background: rgba(255, 255, 255, 0.88);
        padding: 12px 18px; border-radius: 20px; margin-top: 10px;
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 3px solid #c5a059;
    }}
    .premium-deal {{
        background: linear-gradient(135deg, #000, #333);
        color: #c5a059; padding: 10px; border-radius: 15px; margin: 5px; font-size: 11px;
    }}
    .shopping-list-card {{
        background: rgba(0, 0, 0, 0.8); color: white; padding: 15px; border-radius: 20px; margin-top: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. INTERFAȚĂ PRINCIPALĂ
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div style="color:#1a1a1a; letter-spacing:10px; font-size:26px; font-weight:200;">LUXESAVE</div>', unsafe_allow_html=True)
st.markdown('<div style="color:#c5a059; font-size:9px; font-weight:800; letter-spacing:4px;">Arctic Elite Intelligence</div>', unsafe_allow_html=True)

# Panou Status
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.markdown('<small>SAVINGS</small><br><b>284€</b>', unsafe_allow_html=True)
with col2: st.markdown('<small>STATUS</small><br><b style="color:#c5a059;">PREMIUM</b>', unsafe_allow_html=True)
with col3: 
    if st.button("✨ LISTĂ"):
        st.session_state.show_list = not st.session_state.get('show_list', False)

# FUNCȚIA 3: NOTIFICARE PROXIMITATE (Simulare)
st.markdown("""<div style="background:rgba(197,160,89,0.9); color:#000; padding:5px; border-radius:10px; font-size:10px; font-weight:bold; margin-bottom:10px;">
    📍 SMART ALERT: Ești aproape de Hofer (300m) - Berea e la 0.45€!
</div>""", unsafe_allow_html=True)

# FUNCȚIA "DAILY DEALS" (Top 3 Chilipiruri)
st.markdown("<div style='text-align:left; color:#1a1a1a; font-weight:bold; font-size:12px;'>🔥 TOP 3 CHILIPIRURI AZI:</div>", unsafe_allow_html=True)
d1, d2, d3 = st.columns(3)
with d1: st.markdown('<div class="premium-deal">🍺 BIER<br><b>0.45€</b><br><small>HOFER</small></div>', unsafe_allow_html=True)
with d2: st.markdown('<div class="premium-deal">🥛 MILCH<br><b>0.85€</b><br><small>LIDL</small></div>', unsafe_allow_html=True)
with d3: st.markdown('<div class="premium-deal">🧈 BUTTER<br><b>1.45€</b><br><small>SPAR</small></div>', unsafe_allow_html=True)

# 5. LOGICA DE CĂUTARE
st.markdown("<br>", unsafe_allow_html=True)
query = st.text_input("", placeholder="Caută Categorie sau Produs...")

# Coșul de cumpărături (Funcția 2)
if 'cart' not in st.session_state: st.session_state.cart = []

if query:
    q = query.lower()
    stores_data = [{"name": "HOFER", "price": random.uniform(0.60, 1.20)}, {"name": "LIDL", "price": random.uniform(0.65, 1.30)}]
    
    for s in stores_data:
        search_q = urllib.parse.quote(f"{s['name']} supermarket Austria")
        map_url = f"https://www.google.com/maps/search/{search_q}"
        
        st.markdown(f"""
            <div class="store-item">
                <div style="text-align:left;">
                    <b style="color:#000;">{s['name']}</b><br>
                    <small style="font-size:9px; color:#555;">Cel mai mic preț pentru {query}</small>
                </div>
                <div style="display:flex; align-items:center; gap:5px;">
                    <span style="font-weight:900; font-size:18px; color:#d32f2f;">{s['price']:.2f}€</span>
                    <a href="{map_url}" target="_blank"><button style="background:#000; color:#c5a059; border:none; padding:5px 8px; border-radius:8px; font-size:9px;">MAPA</button></a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"🛒 Adaugă {s['name']} ({s['price']:.2f}€)", key=f"add_{s['name']}_{s['price']}"):
            st.session_state.cart.append(s['price'])

# Afișare Shopping List (Funcția 2)
if st.session_state.get('show_list', False):
    total = sum(st.session_state.cart)
    st.markdown(f"""<div class="shopping-list-card">
        <h3>Lista Arctic Shopping</h3>
        <p>Produse în coș: {len(st.session_state.cart)}</p>
        <h2 style="color:#c5a059;">TOTAL: {total:.2f}€</h2>
        <small>Economisești 12.40€ față de prețul de piață!</small>
    </div>""", unsafe_allow_html=True)
    if st.button("Golește Lista"):
        st.session_state.cart = []
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)