# ==============================================
# ✨ BECCA STYLE & DESIGN ✨
# Haute Couture & Créations
# TOUBIWO ANGE REBECCA
# ==============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Becca Style & Design",
    page_icon="✂️",
    layout="wide"
)

# -------------------- CSS --------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #FFF5F5 0%, #FFFFFF 100%);
    }
    h1 {
        color: #800020 !important;
        font-family: 'Georgia', serif !important;
        text-align: center !important;
        font-size: 3.2rem !important;
    }
    h3, .stSubheader {
        color: #4A3728 !important;
        font-family: 'Georgia', serif !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #800020, #CD5C5C) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
    }
    [data-testid="stMetric"] {
        background: #FFF5F5 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: 1px solid #CD5C5C !important;
        border-left: 6px solid #800020 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #800020 !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] {
        color: #4A0000 !important;
        font-size: 2rem !important;
    }
    .stForm {
        background: white !important;
        border-radius: 20px !important;
        padding: 30px !important;
        border: 1px solid #F0E0E0 !important;
    }
    .comment-box {
        background: #FFF5F5 !important;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #800020;
        color: #4A3728 !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- BARRE LATÉRALE --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/684/684809.png", width=80)
    st.markdown("---")
    st.markdown("### BECCA STYLE & DESIGN")
    st.markdown("*Haute Couture & Créations*")
    st.markdown("---")
    st.markdown("**Directrice :** Toubiwo Ange Rebecca")
    st.markdown("*Fondatrice*")
    st.markdown("---")
    st.markdown("### Nos Ateliers")
    st.markdown("• Douala - Bonapriso")
    st.markdown("• Yaoundé - Bastos")
    st.markdown("• Bafoussam - Centre")
    st.markdown("• Limbé - Bord de mer")
    st.markdown("• Garoua - Centre ville")
    st.markdown("---")
    st.markdown("### ⚙️ Paramètres")
    mode_demo = st.checkbox("Afficher les données de démonstration", value=True)
    if mode_demo:
        st.success("Mode démo : 20 commandes")
    else:
        st.info("Mode réel : vos données")

# -------------------- TITRE --------------------
st.title("BECCA STYLE & DESIGN")
st.markdown("### Gestion des Ateliers de Haute Couture")

# -------------------- CHEMIN DU FICHIER --------------------
DATA_FILE = os.path.join("data", "commandes_couture.csv")

# -------------------- LISTES --------------------
ATELIERS = [
    "Douala - Bonapriso", "Yaoundé - Bastos", "Bafoussam - Centre",
    "Limbé - Bord de mer", "Garoua - Centre ville"
]

TYPES_TENUES = [
    "Robe de mariée", "Costume de marié", "Tenue de témoin / demoiselle d'honneur",
    "Tenue de mariage traditionnel", "Tenue de dot", "Kaba Ngondo", "Sanja", "Toghu",
    "Boubou africain", "Ensemble pagne wax", "Tenue traditionnelle sur mesure",
    "Robe de soirée longue", "Robe de cocktail", "Costume de gala", "Ensemble jupe + bustier",
    "Tailleur femme", "Robe de bureau", "Costume homme", "Chemise sur mesure",
    "Robe d'été", "Ensemble pantalon + top", "Jupe portefeuille", "Accessoire de luxe"
]

TISSUS = [
    "Soie sauvage", "Dentelle de Calais", "Velours", "Bazin riche", "Wax haut de gamme",
    "Satin", "Crêpe", "Lin", "Coton égyptien", "Tissu traditionnel (Ndop, Obom)",
    "Mousseline", "Organza", "Broderie anglaise"
]

# -------------------- FONCTIONS --------------------
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

# -------------------- COLONNES --------------------
col1, col2 = st.columns([1, 2])

# ==============================================
# PARTIE GAUCHE : COLLECTE
# ==============================================
with col1:
    st.subheader("📝 Nouvelle Commande")

    with st.form("formulaire_commande", clear_on_submit=True):
        atelier = st.selectbox("Atelier", ATELIERS)
        prenom = st.text_input("Nom de la cliente", placeholder="Ex: Marie")
        age = st.number_input("Âge", min_value=15, max_value=90, value=30, step=1)

        nb_tenues = st.selectbox("Nombre de tenues", [1, 2, 3], index=0)

        st.markdown("**Tenue 1**")
        type_tenue1 = st.selectbox("Type de tenue", TYPES_TENUES, key="t1")
        tissu1 = st.selectbox("Tissu", TISSUS, key="tis1")
        budget1 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b1")
        delai1 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d1")

        if nb_tenues >= 2:
            st.markdown("**Tenue 2**")
            type_tenue2 = st.selectbox("Type de tenue", TYPES_TENUES, key="t2")
            tissu2 = st.selectbox("Tissu", TISSUS, key="tis2")
            budget2 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b2")
            delai2 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d2")

        if nb_tenues >= 3:
            st.markdown("**Tenue 3**")
            type_tenue3 = st.selectbox("Type de tenue", TYPES_TENUES, key="t3")
            tissu3 = st.selectbox("Tissu", TISSUS, key="tis3")
            budget3 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b3")
            delai3 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d3")

        satisfaction = st.slider("Satisfaction (1 à 5)", 1, 5, 4)
        recommandation = st.radio("Recommanderait ?", ["Oui", "Non"], horizontal=True)

        if st.form_submit_button("💾 Enregistrer"):
            if prenom == "":
                st.error("Le nom est requis.")
            else:
                nouvelle = pd.DataFrame([{
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom,
                    "age": age, "type_tenue": type_tenue1, "tissu": tissu1, "budget": budget1,
                    "delai": delai1, "satisfaction": satisfaction, "recommandation": recommandation
                }])
                if nb_tenues >= 2:
                    n2 = pd.DataFrame([{"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom, "age": age, "type_tenue": type_tenue2, "tissu": tissu2, "budget": budget2, "delai": delai2, "satisfaction": satisfaction, "recommandation": recommandation}])
                    nouvelle = pd.concat([nouvelle, n2], ignore_index=True)
                if nb_tenues >= 3:
                    n3 = pd.DataFrame([{"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom, "age": age, "type_tenue": type_tenue3, "tissu": tissu3, "budget": budget3, "delai": delai3, "satisfaction": satisfaction, "recommandation": recommandation}])
                    nouvelle = pd.concat([nouvelle, n3], ignore_index=True)
                sauvegarder_commande(nouvelle)
                st.success(f"✅ {prenom} enregistrée ({nb_tenues} tenue(s))")

    # --- ANNULATION ---
    if os.path.exists(DATA_FILE):
        df_data = pd.read_csv(DATA_FILE)
        if not df_data.empty:
            st.markdown("---")
            st.markdown("### ⚠️ Zone de correction")
            derniere = df_data.iloc[-1]
            st.markdown(f"""
                <div style="background-color: #FFF3CD; border: 1px solid #FFC107; border-radius: 10px; padding: 15px; color: #856404;">
                    <b>Dernière commande :</b> {derniere['prenom']} - {derniere['type_tenue']} ({derniere['atelier']})
                </div>
            """, unsafe_allow_html=True)
            if st.button("🗑️ Annuler cette commande", use_container_width=True):
                df_data = df_data.iloc[:-1]
                df_data.to_csv(DATA_FILE, index=False)
                st.success("✅ Commande supprimée.")
                st.rerun()

# ==============================================
# PARTIE DROITE : ANALYSE DESCRIPTIVE
# ==============================================
with col2:
    st.subheader("📊 Analyse Descriptive des Données")

    df = charger_donnees()

    if mode_demo:
        st.success("🟢 Mode démo activé – 20 commandes exemples.")
        df = pd.DataFrame([
            {"date":"2026-04-01","atelier":"Douala - Bonapriso","prenom":"Marie","age":28,"type_tenue":"Robe de mariée","tissu":"Dentelle de Calais","budget":450000,"delai":30,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-02","atelier":"Douala - Bonapriso","prenom":"Jeanne","age":35,"type_tenue":"Tailleur femme","tissu":"Lin","budget":85000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-03","atelier":"Douala - Bonapriso","prenom":"Carine","age":22,"type_tenue":"Robe de cocktail","tissu":"Satin","budget":120000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-04","atelier":"Douala - Bonapriso","prenom":"Sandrine","age":31,"type_tenue":"Robe de soirée longue","tissu":"Soie sauvage","budget":195000,"delai":21,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-05","atelier":"Yaoundé - Bastos","prenom":"Paul","age":40,"type_tenue":"Costume homme","tissu":"Coton égyptien","budget":150000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-06","atelier":"Yaoundé - Bastos","prenom":"Chantal","age":31,"type_tenue":"Kaba Ngondo","tissu":"Wax haut de gamme","budget":95000,"delai":7,"satisfaction":3,"recommandation":"Non"},
            {"date":"2026-04-07","atelier":"Yaoundé - Bastos","prenom":"Sylvie","age":45,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":200000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-08","atelier":"Yaoundé - Bastos","prenom":"Thomas","age":33,"type_tenue":"Costume de marié","tissu":"Soie sauvage","budget":350000,"delai":28,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-09","atelier":"Bafoussam - Centre","prenom":"Pauline","age":50,"type_tenue":"Sanja","tissu":"Tissu traditionnel","budget":110000,"delai":10,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-10","atelier":"Bafoussam - Centre","prenom":"Alice","age":27,"type_tenue":"Robe de soirée longue","tissu":"Velours","budget":175000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-11","atelier":"Bafoussam - Centre","prenom":"Roger","age":55,"type_tenue":"Costume homme","tissu":"Lin","budget":130000,"delai":14,"satisfaction":3,"recommandation":"Oui"},
            {"date":"2026-04-12","atelier":"Bafoussam - Centre","prenom":"Brigitte","age":47,"type_tenue":"Ensemble jupe + bustier","tissu":"Wax haut de gamme","budget":135000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-13","atelier":"Limbé - Bord de mer","prenom":"Estelle","age":29,"type_tenue":"Robe d'été","tissu":"Coton égyptien","budget":65000,"delai":7,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-14","atelier":"Limbé - Bord de mer","prenom":"Flora","age":38,"type_tenue":"Ensemble pagne wax","tissu":"Wax haut de gamme","budget":90000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-15","atelier":"Limbé - Bord de mer","prenom":"Marc","age":42,"type_tenue":"Chemise sur mesure","tissu":"Lin","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-16","atelier":"Limbé - Bord de mer","prenom":"Nadine","age":25,"type_tenue":"Robe de cocktail","tissu":"Mousseline","budget":105000,"delai":12,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-17","atelier":"Garoua - Centre ville","prenom":"Aïcha","age":26,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":220000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-18","atelier":"Garoua - Centre ville","prenom":"Mariam","age":34,"type_tenue":"Tenue de mariage traditionnel","tissu":"Tissu traditionnel","budget":300000,"delai":30,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-19","atelier":"Garoua - Centre ville","prenom":"Fati","age":42,"type_tenue":"Accessoire de luxe","tissu":"Soie sauvage","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-20","atelier":"Garoua - Centre ville","prenom":"Ousmane","age":38,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":250000,"delai":21,"satisfaction":5,"recommandation":"Oui"},
        ])
    elif df.empty:
        st.info("Aucune commande. Remplissez le formulaire ou activez le mode démo.")

    # ----- INDICATEURS -----
    st.markdown("#### Indicateurs de Performance")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Commandes", len(df))
    with m2:
        if 'budget' in df.columns and len(df) > 0:
            st.metric("Budget Moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
        else:
            st.metric("Budget Moyen", "0 FCFA")
    with m3:
        if 'satisfaction' in df.columns and len(df) > 0:
            st.metric("Satisfaction", f"{df['satisfaction'].mean():.1f}/5")
        else:
            st.metric("Satisfaction", "N/A")
    with m4:
        if 'recommandation' in df.columns and len(df) > 0:
            taux = (df['recommandation'] == "Oui").mean() * 100
            st.metric("Recommandation", f"{taux:.0f}%")
        else:
            st.metric("Recommandation", "N/A")

    st.markdown("""
        <div class="comment-box">
            <b>📊 Interprétation :</b> Ces indicateurs résument l'activité des 5 ateliers.
            Un taux de recommandation élevé (>80%) indique des clientes satisfaites et fidèles.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ----- GRAPHIQUES DESCRIPTIFS -----
    st.markdown("### 📊 Analyse Descriptive")

    colA, colB = st.columns(2)
    with colA:
        st.markdown("#### Top 5 des Tissus")
        top_tissus = df['tissu'].value_counts().head(5)
        if len(top_tissus) > 0:
            fig1, ax1 = plt.subplots(figsize=(5, 5))
            couleurs = ['#800020', '#CD5C5C', '#D4A574', '#8B6F47', '#6B8E23']
            ax1.pie(top_tissus.values, labels=top_tissus.index, autopct='%1.1f%%', colors=couleurs)
            st.pyplot(fig1)

    with colB:
        st.markdown("#### Top 5 des Tenues")
        top_tenues = df['type_tenue'].value_counts().head(5)
        if len(top_tenues) > 0:
            fig2, ax2 = plt.subplots(figsize=(5, 5))
            couleurs = ['#800020', '#CD5C5C', '#D4A574', '#8B6F47', '#6B8E23']
            ax2.pie(top_tenues.values, labels=top_tenues.index, autopct='%1.1f%%', colors=couleurs)
            st.pyplot(fig2)

    st.markdown("---")
    st.markdown("#### Performance des Ateliers")

    colC, colD = st.columns(2)
    with colC:
        st.markdown("##### Satisfaction par Atelier")
        satisf_atelier = df.groupby('atelier')['satisfaction'].mean().sort_values(ascending=False)
        fig4, ax4 = plt.subplots(figsize=(5, 4))
        couleurs = ['#800020', '#CD5C5C', '#D4A574', '#8B6F47', '#6B8E23']
        bars = ax4.bar(satisf_atelier.index, satisf_atelier.values, color=couleurs)
        ax4.set_ylabel('Satisfaction (/5)')
        ax4.set_ylim(0, 5)
        plt.xticks(rotation=45, ha='right')
        for bar, val in zip(bars, satisf_atelier.values):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{val:.1f}', ha='center', fontweight='bold')
        st.pyplot(fig4)

    with colD:
        st.markdown("##### Commandes par Atelier")
        cmd_atelier = df['atelier'].value_counts()
        fig5, ax5 = plt.subplots(figsize=(5, 4))
        bars = ax5.bar(cmd_atelier.index, cmd_atelier.values, color=couleurs[:len(cmd_atelier)])
        ax5.set_ylabel('Nombre de Commandes')
        plt.xticks(rotation=45, ha='right')
        for bar, val in zip(bars, cmd_atelier.values):
            ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(val), ha='center', fontweight='bold')
        st.pyplot(fig5)

    st.markdown("---")
    st.markdown("#### Données Brutes")
    df_affiche = df.sort_values('date', ascending=False).reset_index(drop=True)
    df_affiche.index = df_affiche.index + 1
    st.dataframe(df_affiche, use_container_width=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Télécharger (CSV)", data=csv, file_name='becca_export.csv', mime='text/csv')

# -------------------- CITATION --------------------
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #800020, #CD5C5C); border-radius: 15px; color: white; margin: 20px 0;">
        <p style="font-size: 1.3rem; font-family: Georgia, serif; font-style: italic;">
            "Le style est une façon de dire qui vous êtes sans avoir à parler."
        </p>
        <p style="font-size: 0.9rem; margin-top: 10px;">— Becca Style & Design</p>
    </div>
""", unsafe_allow_html=True)

# -------------------- PIED DE PAGE --------------------
st.markdown("""
    <div style='text-align: center; color: grey; font-size: 12px; margin-top: 20px;'>
        <p>© 2026 <b>Becca Style & Design</b> - Tous droits réservés</p>
        <p>Toubiwo Ange Rebecca - Fondatrice & Directrice Artistique</p>
    </div>
""", unsafe_allow_html=True)