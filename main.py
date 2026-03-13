import streamlit as st
import pandas as pd

# 1. Dizayn: Bet bası
st.set_page_config(page_title="MediFind", page_icon="💊")
st.title("🔍 MediFind — Demo")

# 2. Dári maǵlıwmatları (Baza)
data = {
    'Dári atı': ['Paracetamol', 'Analgin', 'Citramon'],
    'Dárixana': ['Arzon Apteka', 'Grand Farm', 'Salamatlıq'],
    'Bahası': ['5 000 som', '3 000 som', '4 500 som'],
    'lat': [42.4601, 42.4550, 42.4650],
    'lon': [59.6122, 59.6050, 59.6250]
}
df = pd.DataFrame(data)

# 3. Izlew interfeysi
query = st.text_input("Dári atın jazıń:")

if query:
    res = df[df['Dári atı'].str.contains(query, case=False)]
    if not res.empty:
        st.success(f"Tabıldı: {query}")
        st.table(res[['Dári atı', 'Dárixana', 'Bahası']])
    else:
        st.error("Dári tabılmadı")

# 4. Karta
st.subheader("📍 Jaqın átiraptaǵı dárixanalar")
st.map(df[['lat', 'lon']])

