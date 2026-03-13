import streamlit as st
import pandas as pd

# --- PROFESSIONAL BACKEND LOGIC ---
class MediFindEngine:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def search_medicine(self, name):
        """Dárini atı boyınsha izlew hám filtrlew"""
        results = self.df[self.df['Dári atı'].str.contains(name, case=False)]
        return results.sort_values(by='Bahası_Int') # Arzanın birinshi kórsetiw

    def get_statistics(self):
        """Sistema boyınsha statistika"""
        return {
            "top_pharmacy": self.df.loc[self.df['Reyting'].idxmax()]['Dárixana'],
            "avg_price": self.df['Bahası_Int'].mean(),
            "total_meds": len(self.df)
        }

# --- DATA WITH COMPLEX STRUCTURE ---
raw_data = {
    'Dári atı': ['Paracetamol', 'Analgin', 'Citramon', 'Aspirin', 'Noshpa', 'Qupen'],
    'Dárixana': ['Dawlet Farm', 'Mir Apteka', 'Aybolit', 'Ajiniyaz', 'Shıpa Nur', 'Nur Apteka'],
    'Bahası_Int': [5000, 3000, 4500, 6000, 12000, 70000],
    'Reyting': [4.8, 4.2, 3.9, 4.5, 4.9, 5.0],
    'Status': ['Open', 'Open', 'Closed', 'Open', 'Open','Open'],
    'lat': [42.4601, 42.4550, 42.4650, 42.4700, 42.4500, 42.300],
    'lon': [59.6122, 59.6050, 59.6250, 59.6350, 59.5900, 59.6000]
}

# Inicializaciya
engine = MediFindEngine(raw_data)

# --- FRONTEND (Streamlit) ---
st.title("💊 MediFind ")

# Statistika bólimi (Hákislerge unaydı)
stats = engine.get_statistics()
col1, col2, col3 = st.columns(3)
col1.metric("Jámi dáriler", stats['total_meds'])
col2.metric("Ortasha baha", f"{int(stats['avg_price'])} som")
col3.metric("Eń jaqsı dárixana", stats['top_pharmacy'])

# İzlew
query = st.text_input("🔍 Dári atın jazıń:", placeholder="Mısalı: Paracetamol")

if query:
    search_results = engine.search_medicine(query)
    if not search_results.empty:
        st.success(f"{len(search_results)} nátiyje tabıldı.")
        
        # Professional karta kórinisi
        for _, row in search_results.iterrows():
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #008080; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
                    <h4>{row['Dári atı']} — {row['Bahası_Int']} som</h4>
                    <p>🏢 <b>Dárixana:</b> {row['Dárixana']} | ⭐ <b>Reyting:</b> {row['Reyting']}</p>
                    <p>🟢 <b>Status:</b> {row['Status']}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("Dári tabılmadı.")

# Siziń Figma dizaynıńız
st.write("---")
st.image("design1.png", caption="System UI Architecture")
