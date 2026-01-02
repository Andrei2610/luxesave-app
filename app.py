import streamlit as st
import base64
import os
import random
import urllib.parse

# 1. CONFIGURARE PAGINĂ
st.set_page_config(page_title="LuxeSave Elite", page_icon="💎", layout="centered")

# ELIMINARE BARA ALBĂ
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
</style>
""", unsafe_allow_html=True)

# 4. INITIALIZARE COȘ (Fix pentru listă)
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 5. INTERFAȚĂ PRINCIPALĂ
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div style="color:#1a1a1a; letter-spacing:10px; font-size:26px; font-weight:200;">LUXESAVE</div>', unsafe_allow_html=True)
st.markdown('<div style="color:#c5a059; font-size:9px; font-weight:800; letter-spacing:4px;">Arctic Elite Intelligence</div>', unsafe_allow_html=True)

# Panou Status
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<small>SAVINGS</small><br><b>284€</b>', unsafe_allow_html=True)
with c2: st.markdown('<small>STATUS</small><br><b style="color:#c5a059;">PREMIUM</b>', unsafe_allow_html=True)
with c3: 
    show_list = st.button(f"🛒 LISTĂ ({len(st.session_state.cart)})")

# Notificare Proximitate
st.markdown('<div style="background:rgba(197,160,89,0.9); color:#000; padding:5px; border-radius:10px; font-size:10px; font-weight:bold; margin-bottom:10px;">📍 SMART ALERT: Hofer (300m) - Bere la 0.45€!</div>', unsafe_allow_html=True)

# Daily Deals
st.markdown("<div style='text-align:left; color:#1a1a1a; font-weight:bold; font-size:12px;'>🔥 TOP CHILIPIRURI:</div>", unsafe_allow_html=True)
d1, d2, d3 = st.columns(3)
with d1: st.markdown('<div class="premium-deal">🍺 BIER<br><b>0.45€</b></div>', unsafe_allow_html=True)
with d2: st.markdown('<div class="premium-deal">🥛 MILCH<br><b>0.85€</b></div>', unsafe_allow_html=True)
with d3: st.markdown('<div class="premium-deal">🧈 BUTTER<br><b>1.45€</b></div>', unsafe_allow_html=True)

# 6. CĂUTARE ȘI REZULTATE
query = st.text_input("", placeholder="Caută produs...")

if query:
    stores = [{"name": "HOFER", "price": 0.45 if query.lower() == "bier" else random.uniform(0.6, 1.2)},
              {"name": "LIDL", "price": 0.49 if query.lower() == "bier" else random.uniform(0.7, 1.3)}]
    
    for s in stores:
        col_item, col_btn = st.columns([4, 1])
        with col_item:
            st.markdown(f"""<div class="store-item"><b>{s['name']}</b> <span style="color:#d32f2f; font-weight:900;">{s['price']:.2f}€</span></div>""", unsafe_allow_html=True)
        with col_btn:
            if st.button("🛒", key=f"btn_{s['name']}_{s['price']}"):
                st.session_state.cart.append({"prod": query, "price": s['price']})
                st.rerun()

# 7. AFIȘARE LISTĂ CUMPĂRĂTURI
if show_list and st.session_state.cart:
    st.markdown('<div style="background:rgba(0,0,0,0.8); color:white; padding:15px; border-radius:20px; margin-top:10px; text-align:left;">', unsafe_allow_html=True)
    st.markdown("### Coșul tău Arctic:")
    total = 0
    for item in st.session_state.cart:
        st.write(f"✅ {item['prod']} - {item['price']:.2f}€")
        total += item['price']
    st.markdown(f"<h2 style='color:#c5a059;'>TOTAL: {total:.2f}€</h2>", unsafe_allow_html=True)
    if st.button("Golește"):
        st.session_state.cart = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
