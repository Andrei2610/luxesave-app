import streamlit as st
import base64
import os

# 1. FORȚĂM MEMORIA SĂ EXISTE
if 'cos' not in st.session_state:
    st.session_state['cos'] = []

st.set_page_config(page_title="LuxeSave Elite", page_icon="💎")

# 2. FUNDAL ȘI STIL
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
            background-size: cover;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px; border-radius: 20px; color: black;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.title("💎 LUXESAVE")

# 3. AFIȘARE LISTĂ (Chiar sus de tot)
st.write("### 🛒 COȘUL TĂU:")
if not st.session_state['cos']:
    st.info("Coșul este gol. Caută produse mai jos.")
else:
    total = 0
    for i, p in enumerate(st.session_state['cos']):
        st.write(f"{i+1}. {p['nume']} - {p['pret']}€")
        total += p['pret']
    st.success(f"**TOTAL DE PLATĂ: {total:.2f}€**")
    if st.button("🗑️ Golește Coșul"):
        st.session_state['cos'] = []
        st.rerun()

st.markdown("---")

# 4. FORMULAR DE CĂUTARE ȘI ADĂUGARE
# Folosim 'with st.form' pentru a bloca resetarea memoriei
query = st.text_input("Ce cauți?")

if query:
    with st.form(key='search_form'):
        st.write(f"Oferte pentru: {query}")
        
        # Simulăm prețuri
        p_hofer = 0.45 if query.lower() == "bier" else 1.25
        p_lidl = 0.49 if query.lower() == "bier" else 1.35
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("🏠 **HOFER**")
            st.write(f"{p_hofer}€")
            add_hofer = st.form_submit_button(label="Adaugă Hofer")
            
        with col2:
            st.write("🏠 **LIDL**")
            st.write(f"{p_lidl}€")
            add_lidl = st.form_submit_button(label="Adaugă Lidl")

        # LOGICA DE SALVARE (Se execută doar la submit)
        if add_hofer:
            st.session_state['cos'].append({"nume": f"{query} (Hofer)", "pret": p_hofer})
            st.rerun()
        if add_lidl:
            st.session_state['cos'].append({"nume": f"{query} (Lidl)", "pret": p_lidl})
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
