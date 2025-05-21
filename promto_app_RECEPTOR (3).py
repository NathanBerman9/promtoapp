
import streamlit as st

st.set_page_config(page_title="PROMTO Receptor", layout="centered")
st.title("PROMTO – Formulario Receptor")

with st.form("form_receptor"):
    st.subheader("🫀 Estudios cardiológicos")
    fecha_eco = st.date_input("Fecha de ecocardiograma")
    fevi = st.text_input("FEVI (%)")
    psap = st.text_input("PSAP (mmHg)")
    valvulopatia = st.selectbox("¿Valvulopatías u otras alteraciones?", ["No", "Sí"])
    observaciones_valvulopatia = ""
    if valvulopatia == "Sí":
        observaciones_valvulopatia = st.text_area("Observaciones de ecocardiograma")

    fecha_ekg = st.date_input("Fecha de electrocardiograma")
    ekg_normal = st.selectbox("¿ECG sin datos patológicos?", ["Sí", "No"])
    observaciones_ekg = ""
    if ekg_normal == "No":
        observaciones_ekg = st.text_area("Observaciones de ECG")

    st.form_submit_button("Guardar (función temporal)")
