# ==============================================
# ✨ BECCA STYLE & DESIGN ✨
# Analyse de Données - Haute Couture
# Projet ETUDE EC2
# TOUBIWO ANGE BECCA
# ==============================================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Becca Style & Design | Analyse de Données",
    page_icon="📊",
    layout="wide"
)

# -------------------- STYLE PROFESSIONNEL ÉPURÉ --------------------
st.markdown("""
    <style>
    .stApp {
        background: #F8F9FA;
    }
    h1 {
        color: #2C3E50 !important;
        font-family: 'Segoe UI', 'Arial', sans-serif !important;
        text-align: center !important;
        font-size: 2.8rem !important;
        letter-spacing: 2px;
        border-bottom: 2px solid #2C3E50;
        padding-bottom: 15px;
    }
    h3 {
        color: #34495E !important;
        font-family: 'Arial', sans-serif !important;
    }
    .stButton > button {
        background: #2C3E50 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px 20px !important;
    }
    .stButton > button:hover {
        background: #1A252F !important;
    }
    [data-testid="stMetric"] {
        background: white !important;
        border-radius: 10px !important;
        padding: 20px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        border-left: 4px solid #2C3E50 !important;
    }
    .stForm {
        background: white !important;
        border-radius: 10px !important;
        padding: 30px !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05) !important;
        border: 1px solid #E0E0E0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- BARRE LATÉRALE --------------------
with st.sidebar:
    st.markdown("### BECCA STYLE & DESIGN")
    st.markdown("Direction de l'Analyse Stratégique")
    st.markdown("---")
    st.markdown(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown("---")
    st.markdown("*Responsable :* TOUBIWO ANGE BECCA")
    st.markdown("*Projet :* TP INF232 EC2")

# -------------------- TITRE --------------------
st.title("BECCA STYLE & DESIGN")
st.markdown("### Plateforme d'Analyse de Données - Module de Gestion des Ateliers")
st.markdown("---")

# -------------------- CHEMIN DU FICHIER DE DONNÉES --------------------
DATA_FILE = os.path.join("data", "commandes_couture.csv")

# -------------------- LISTES DES CHOIX --------------------
ATELIERS = [
    "Douala - Bonapriso", "Yaoundé - Bastos", "Bafoussam - Centre",
    "Limbé - Bord de mer", "Garoua - Centre ville"
]

TYPES_TENUES = [
    "Robe de mariée", "Costume de marié", "Tenue de cérémonie traditionnelle",
    "Costume professionnel", "Robe de soirée", "Ensemble sur mesure"
]

TISSUS = [
    "Soie sauvage", "Dentelle de Calais", "Velours", "Bazin riche",
    "Wax haut de gamme", "Satin", "Lin", "Coton égyptien"
]

# -------------------- FONCTIONS DE GESTION DES DONNÉES --------------------
def charger_donnees():
    if os.path.exists(DATA_FILE):
        try: return pd.read_csv(DATA_FILE)
        except: return pd.DataFrame()
    return pd.DataFrame()

def sauvegarder_commande(data):
    df_existant = charger_donnees()
    df_final = pd.concat([df_existant, data], ignore_index=True)
    os.makedirs("data", exist_ok=True)
    df_final.to_csv(DATA_FILE, index=False)
    return True

# -------------------- CRÉATION DE L'APP (2 COLONNES) --------------------
col1, col2 = st.columns([1, 2])

# ==============================================
# PARTIE GAUCHE : MODULE DE COLLECTE
# ==============================================
with col1:
    st.subheader("Saisie des Commandes")
    st.markdown("Formulaire de collecte terrain")
    
    with st.form("formulaire_commande", clear_on_submit=True):
        atelier = st.selectbox("Atelier", ATELIERS)
        prenom = st.text_input("Identifiant Client")
        age = st.number_input("Age", min_value=15, max_value=90, value=30, step=1)
        type_tenue = st.selectbox("Type de Tenue", TYPES_TENUES)
        tissu = st.selectbox("Tissu Principal", TISSUS)
        budget = st.number_input("Budget Total (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000)
        delai = st.number_input("Delai de Confection (jours)", min_value=1, max_value=90, value=14, step=1)
        satisfaction = st.slider("Score de Satisfaction", 1, 5, 4)
        recommandation = st.radio("Recommanderait l'atelier ?", ["Oui", "Non"], horizontal=True)
        
        if st.form_submit_button("Enregistrer la Commande"):
            if prenom == "":
                st.error("Erreur : L'identifiant client est requis.")
            else:
                nouvelle_ligne = pd.DataFrame([{
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom,
                    "age": age, "type_tenue": type_tenue, "tissu": tissu, "budget": budget,
                    "delai": delai, "satisfaction": satisfaction, "recommandation": recommandation
                }])
                sauvegarder_commande(nouvelle_ligne)
                st.success(f"Commande enregistrée avec succès.")
                st.balloons()

# ==============================================
# PARTIE DROITE : MODULE D'ANALYSE
# ==============================================
with col2:
    st.subheader("Module d'Analyse Des Données")
    
    df = charger_donnees()
    
    if df.empty:
        st.warning("Aucune donnée collectée. Veuillez remplir le formulaire de collecte pour alimenter les analyses.")
        # On met un jeu de données exemple pour une première visualisation
        st.info("Affichage des analyses avec un jeu de données exemple.")
        # Créer des données exemple
        dates = pd.date_range(start="2026-01-01", periods=50, freq='7D')
        ateliers_ex = np.random.choice(ATELIERS, 50)
        budgets_ex = np.random.normal(150000, 50000, 50).astype(int)
        satis_ex = np.random.normal(3.8, 0.8, 50).clip(1, 5).round(1)
        df = pd.DataFrame({
            "date": dates, "atelier": ateliers_ex, "prenom": "Client Ex", "age": 35,
            "type_tenue": "Robe", "tissu": "Soie", "budget": budgets_ex,
            "delai": 14, "satisfaction": satis_ex, "recommandation": "Oui"
        })
    
    # ----- INDICATEURS CLES -----
    st.markdown("#### Indicateurs de Performance Clés")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Total Commandes", len(df))
    with kpi2:
        st.metric("Budget Moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
    with kpi3:
        st.metric("Satisfaction Moyenne", f"{df['satisfaction'].mean():.1f}/5")
    with kpi4:
        taux_reco = (df['recommandation'] == "Oui").mean() * 100
        st.metric("Taux de Recommandation", f"{taux_reco:.0f}%")
    
    st.markdown("---")
    
    # ----- ANALYSES AVANCEES (EC2) -----
    tab_ec2, tab_brutes = st.tabs(["Analyses EC2", "Données Brutes"])
    
    with tab_ec2:
        st.markdown("### Analyse de Données du Cours EC2")
        
        # 1. DISTRIBUTION DES BUDGETS
        st.markdown("#### Distribution et Effectif Cumulé des Budgets")
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.hist(df['budget'], bins=20, color='#2C3E50', edgecolor='white', alpha=0.7, label='Effectif par tranche')
        ax1.set_xlabel("Budget (FCFA)")
        ax1.set_ylabel("Effectif")
        ax1.set_title("Histogramme de la distribution des budgets")
        st.pyplot(fig1)
        
        # 2. COURBE DE REGRESSION (BUDGET VS SATISFACTION)
        st.markdown("#### Régression Linéaire : Budget vs Satisfaction Client")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        x = df['budget']
        y = df['satisfaction']
        ax2.scatter(x, y, alpha=0.5)
        
        if len(x) > 1:
            slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
            line = slope * x + intercept
            ax2.plot(x, line, color='red', linewidth=2)
            ax2.annotate(f'y={slope:.4f}x+{intercept:.2f}\nR²={r_value**2:.2f}', xy=(0.05, 0.9), xycoords='axes fraction', bbox=dict(facecolor='yellow', alpha=0.5))
        
        ax2.set_xlabel("Budget (FCFA)")
        ax2.set_ylabel("Score de Satisfaction")
        ax2.set_title("Analyse de Corrélation : Budget investi et Satisfaction")
        st.pyplot(fig2)
        st.caption("Cette courbe de régression permet de comprendre si un budget plus élevé est statistiquement lié à une meilleure satisfaction client.\n- R² s'approche de 1 : Forte corrélation\n- R² s'approche de 0 : Aucune corrélation")
        
        # 3. ANALYSE DES TOP PERFORMERS
        st.markdown("#### Performance Comparative des Ateliers")
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        atelier_perf = df.groupby('atelier').agg({'satisfaction': 'mean', 'budget': 'count'}).reset_index()
        ax3.bar(atelier_perf['atelier'], atelier_perf['satisfaction'], color='#34495E')
        ax3.set_xlabel("Atelier")
        ax3.set_ylabel("Score de Satisfaction Moyen")
        ax3.set_title("Satisfaction Moyenne par Atelier (Analyse Comparative)")
        st.pyplot(fig3)
    
    with tab_brutes:
        st.subheader("Base de Données Brutes")
        st.dataframe(df.sort_values('date', ascending=False), use_container_width=True)

# -------------------- PIED DE PAGE --------------------
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: grey; font-size: 12px; margin-top: 20px;'>
        <p>© 2026 <b>Becca Style & Design</b> - Module d'Analyse EC2</p>
        <p>TP INF232 EC2 - TOUBIWO ANGE BECCA</p>
    </div>
""", unsafe_allow_html=True)
