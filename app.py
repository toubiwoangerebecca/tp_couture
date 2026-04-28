# ==============================================
# ✨ BECCA STYLE & DESIGN ✨
# Haute Couture & Créations
# ==============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Becca Style & Design",
    page_icon="👗",
    layout="wide"
)

# -------------------- CSS PROFESSIONNEL --------------------
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
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    h3, .stSubheader {
        color: #4A3728 !important;
        font-family: 'Georgia', serif !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #800020, #CD5C5C) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 0.85rem !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
    }
    .stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(128,0,32,0.4) !important;
    }
    [data-testid="stMetric"] {
        background: white !important;
        border-radius: 15px !important;
        padding: 15px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08) !important;
        border-left: 4px solid #800020 !important;
    }
    .stForm {
        background: white !important;
        border-radius: 20px !important;
        padding: 30px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        border: 1px solid #F0E0E0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- BARRE LATÉRALE --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1943/1943678.png", width=80)
    st.markdown("---")
    st.markdown("### BECCA STYLE & DESIGN")
    st.markdown("*Haute Couture & Créations*")
    st.markdown("---")
    st.markdown("**Directrice :** Rebecca TOUBIWO")
    st.markdown("*Fondatrice*")
    st.markdown("---")
    st.markdown("### Nos Ateliers")
    st.markdown("• Douala - Bonapriso")
    st.markdown("• Yaoundé - Bastos")
    st.markdown("• Bafoussam - Centre")
    st.markdown("• Limbé - Bord de mer")
    st.markdown("• Garoua - Centre ville")
    st.markdown("---")
    st.markdown("### ⚙️ Paramètres d'affichage")
    mode_demo = st.checkbox("Afficher les données de démonstration", value=True)
    if mode_demo:
        st.success("Mode démo activé – 20 exemples")
    else:
        st.info("Données réelles affichées")

# -------------------- TITRE --------------------
st.title("BECCA STYLE & DESIGN")
st.markdown("### Gestion des Ateliers de Haute Couture")

st.markdown("""
    <div style="text-align: center; display: flex; align-items: center; justify-content: center; gap: 10px; margin: 20px 0;">
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
        <span style="color: #800020; font-size: 1.2rem;">✦</span>
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
    </div>
""", unsafe_allow_html=True)

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
    st.subheader("Nouvelle Commande")
    st.markdown("*Formulaire de saisie*")
    
    with st.form("formulaire_commande", clear_on_submit=True):
        atelier = st.selectbox("Atelier", ATELIERS)
        prenom = st.text_input("Nom du client", placeholder="Ex: Marie")
        age = st.number_input("Âge", min_value=15, max_value=90, value=30, step=1)
        
        st.markdown("---")
        st.markdown("### Tenues commandées")
        
        nb_tenues = st.selectbox("Nombre de tenues commandées", [1, 2, 3], index=0)
        
        st.markdown("**Tenue 1**")
        type_tenue1 = st.selectbox("Type de tenue", TYPES_TENUES, key="t1")
        tissu1 = st.selectbox("Tissu principal", TISSUS, key="tis1")
        budget1 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b1")
        delai1 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d1")
        
        if nb_tenues >= 2:
            st.markdown("**Tenue 2**")
            type_tenue2 = st.selectbox("Type de tenue", TYPES_TENUES, key="t2")
            tissu2 = st.selectbox("Tissu principal", TISSUS, key="tis2")
            budget2 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b2")
            delai2 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d2")
        
        if nb_tenues >= 3:
            st.markdown("**Tenue 3**")
            type_tenue3 = st.selectbox("Type de tenue", TYPES_TENUES, key="t3")
            tissu3 = st.selectbox("Tissu principal", TISSUS, key="tis3")
            budget3 = st.number_input("Budget (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000, key="b3")
            delai3 = st.number_input("Délai (jours)", min_value=1, max_value=90, value=14, step=1, key="d3")
        
        st.markdown("---")
        
        satisfaction = st.slider("Satisfaction client (1 à 5)", 1, 5, 4)
        recommandation = st.radio("Recommanderait l'atelier ?", ["Oui", "Non"], horizontal=True)
        
        if st.form_submit_button("Enregistrer la Commande"):
            if prenom == "":
                st.error("Le nom du client est requis.")
            else:
                nouvelle = pd.DataFrame([{
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom,
                    "age": age, "type_tenue": type_tenue1, "tissu": tissu1, "budget": budget1,
                    "delai": delai1, "satisfaction": satisfaction, "recommandation": recommandation
                }])
                
                if nb_tenues >= 2:
                    nouvelle2 = pd.DataFrame([{
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom,
                        "age": age, "type_tenue": type_tenue2, "tissu": tissu2, "budget": budget2,
                        "delai": delai2, "satisfaction": satisfaction, "recommandation": recommandation
                    }])
                    nouvelle = pd.concat([nouvelle, nouvelle2], ignore_index=True)
                
                if nb_tenues >= 3:
                    nouvelle3 = pd.DataFrame([{
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "atelier": atelier, "prenom": prenom,
                        "age": age, "type_tenue": type_tenue3, "tissu": tissu3, "budget": budget3,
                        "delai": delai3, "satisfaction": satisfaction, "recommandation": recommandation
                    }])
                    nouvelle = pd.concat([nouvelle, nouvelle3], ignore_index=True)
                
                sauvegarder_commande(nouvelle)
                st.success(f"Commande de {prenom} enregistrée avec succès ({nb_tenues} tenue(s)) !")
    
    # --- BOUTON D'ANNULATION ---
    if os.path.exists(DATA_FILE):
        df_data = pd.read_csv(DATA_FILE)
        if not df_data.empty:
            st.markdown("---")
            st.markdown("### ⚠️ Zone de correction")
            derniere = df_data.iloc[-1]
            st.warning(f"**Dernière commande :** {derniere['prenom']} - {derniere['type_tenue']} ({derniere['atelier']})")
            if st.button("🗑️ Annuler cette commande", use_container_width=True):
                df_data = df_data.iloc[:-1]
                df_data.to_csv(DATA_FILE, index=False)
                st.success("Commande supprimée avec succès.")
                st.rerun()

# ==============================================
# PARTIE DROITE : ANALYSE
# ==============================================
with col2:
    st.subheader("Analyse des Données")
    
    df = charger_donnees()
    
    if mode_demo:
        st.success("Mode démonstration activé – 20 commandes exemples.")
        df = pd.DataFrame([
            {"date":"2026-04-01 10:00","atelier":"Douala - Bonapriso","prenom":"Marie","age":28,"type_tenue":"Robe de mariée","tissu":"Dentelle de Calais","budget":450000,"delai":30,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-02 11:00","atelier":"Douala - Bonapriso","prenom":"Jeanne","age":35,"type_tenue":"Tailleur femme","tissu":"Lin","budget":85000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-03 12:00","atelier":"Douala - Bonapriso","prenom":"Carine","age":22,"type_tenue":"Robe de cocktail","tissu":"Satin","budget":120000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-04 13:00","atelier":"Douala - Bonapriso","prenom":"Sandrine","age":31,"type_tenue":"Robe de soirée longue","tissu":"Soie sauvage","budget":195000,"delai":21,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-05 10:30","atelier":"Yaoundé - Bastos","prenom":"Paul","age":40,"type_tenue":"Costume homme","tissu":"Coton égyptien","budget":150000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-06 11:30","atelier":"Yaoundé - Bastos","prenom":"Chantal","age":31,"type_tenue":"Kaba Ngondo","tissu":"Wax haut de gamme","budget":95000,"delai":7,"satisfaction":3,"recommandation":"Non"},
            {"date":"2026-04-07 12:30","atelier":"Yaoundé - Bastos","prenom":"Sylvie","age":45,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":200000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-08 13:30","atelier":"Yaoundé - Bastos","prenom":"Thomas","age":33,"type_tenue":"Costume de marié","tissu":"Soie sauvage","budget":350000,"delai":28,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-09 10:00","atelier":"Bafoussam - Centre","prenom":"Pauline","age":50,"type_tenue":"Sanja","tissu":"Tissu traditionnel (Ndop, Obom)","budget":110000,"delai":10,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-10 11:00","atelier":"Bafoussam - Centre","prenom":"Alice","age":27,"type_tenue":"Robe de soirée longue","tissu":"Velours","budget":175000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-11 12:00","atelier":"Bafoussam - Centre","prenom":"Roger","age":55,"type_tenue":"Costume homme","tissu":"Lin","budget":130000,"delai":14,"satisfaction":3,"recommandation":"Oui"},
            {"date":"2026-04-12 13:00","atelier":"Bafoussam - Centre","prenom":"Brigitte","age":47,"type_tenue":"Ensemble jupe + bustier","tissu":"Wax haut de gamme","budget":135000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-13 10:30","atelier":"Limbé - Bord de mer","prenom":"Estelle","age":29,"type_tenue":"Robe d'été","tissu":"Coton égyptien","budget":65000,"delai":7,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-14 11:30","atelier":"Limbé - Bord de mer","prenom":"Flora","age":38,"type_tenue":"Ensemble pagne wax","tissu":"Wax haut de gamme","budget":90000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-15 12:30","atelier":"Limbé - Bord de mer","prenom":"Marc","age":42,"type_tenue":"Chemise sur mesure","tissu":"Lin","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-16 13:30","atelier":"Limbé - Bord de mer","prenom":"Nadine","age":25,"type_tenue":"Robe de cocktail","tissu":"Mousseline","budget":105000,"delai":12,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-17 10:00","atelier":"Garoua - Centre ville","prenom":"Aïcha","age":26,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":220000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-18 11:00","atelier":"Garoua - Centre ville","prenom":"Mariam","age":34,"type_tenue":"Tenue de mariage traditionnel","tissu":"Tissu traditionnel (Ndop, Obom)","budget":300000,"delai":30,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-19 12:00","atelier":"Garoua - Centre ville","prenom":"Fati","age":42,"type_tenue":"Accessoire de luxe","tissu":"Soie sauvage","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-20 13:00","atelier":"Garoua - Centre ville","prenom":"Ousmane","age":38,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":250000,"delai":21,"satisfaction":5,"recommandation":"Oui"},
        ])
    elif df.empty:
        st.info("Aucune commande enregistrée. Remplissez le formulaire ou activez le mode démo.")
    
    # ----- INDICATEURS -----
    st.markdown("#### Indicateurs de Performance")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Commandes", len(df))
    with m2:
        st.metric("Budget Moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
    with m3:
        st.metric("Satisfaction Moyenne", f"{df['satisfaction'].mean():.1f}/5")
    with m4:
        taux = (df['recommandation'] == "Oui").mean() * 100
        st.metric("Recommandation", f"{taux:.0f}%")
    
    st.markdown("---")
    
    # ----- MENU ALIGNÉ (5 boutons) -----
    col_menu1, col_menu2, col_menu3, col_menu4, col_menu5 = st.columns(5)
    
    with col_menu1:
        if st.button("Tendances", use_container_width=True, key="btn_tend"):
            st.session_state['section'] = 'tendances'
    with col_menu2:
        if st.button("Régression", use_container_width=True, key="btn_reg"):
            st.session_state['section'] = 'regression'
    with col_menu3:
        if st.button("PCA", use_container_width=True, key="btn_pca"):
            st.session_state['section'] = 'pca'
    with col_menu4:
        if st.button("Classification", use_container_width=True, key="btn_class"):
            st.session_state['section'] = 'classification'
    with col_menu5:
        if st.button("Clustering", use_container_width=True, key="btn_clust"):
            st.session_state['section'] = 'clustering'
    
    if 'section' not in st.session_state:
        st.session_state['section'] = 'tendances'
    
    st.markdown("---")
    
    # ----- AFFICHAGE SELON LA SECTION -----
    if st.session_state['section'] == 'tendances':
        st.markdown("### Tendances & Camemberts")
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
        st.markdown("#### Performance Ateliers")
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
        st.markdown("#### Données Brutes")
        st.dataframe(df.sort_values('date', ascending=False), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Télécharger (CSV)", data=csv, file_name='becca_export.csv', mime='text/csv')
    
    elif st.session_state['section'] == 'regression':
        st.markdown("### Régression Linéaire")
        tab_reg1, tab_reg2 = st.tabs(["Régression Simple", "Régression Multiple"])
        
        with tab_reg1:
            st.markdown("#### Budget vs Satisfaction")
            fig, ax = plt.subplots(figsize=(8, 4))
            x = df['budget'].values
            y = df['satisfaction'].values
            ax.scatter(x, y, alpha=0.6, color='#800020', s=80)
            if len(x) > 1:
                A = np.vstack([x, np.ones(len(x))]).T
                pente, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
                ax.plot(x, pente * x + intercept, color='red', linewidth=2)
                y_pred = pente * x + intercept
                ss_res = np.sum((y - y_pred) ** 2)
                ss_tot = np.sum((y - np.mean(y)) ** 2)
                r2 = 1 - (ss_res / ss_tot)
                ax.set_title(f"R² = {r2:.3f} | y = {pente:.6f}x + {intercept:.2f}")
            st.pyplot(fig)
        
        with tab_reg2:
            st.markdown("#### Budget + Âge → Satisfaction")
            if len(df) >= 5:
                X = df[['budget', 'age']].values
                y = df['satisfaction'].values
                modele = LinearRegression()
                modele.fit(X, y)
                y_pred = modele.predict(X)
                
                coef_df = pd.DataFrame({'Variable': ['Budget', 'Âge'], 'Coefficient': modele.coef_})
                st.dataframe(coef_df)
                st.metric("R²", f"{r2_score(y, y_pred):.3f}")
            else:
                st.info("Données insuffisantes.")
    
    elif st.session_state['section'] == 'pca':
        st.markdown("### PCA - Profils Clients")
        if len(df) >= 5:
            features = ['budget', 'age', 'satisfaction', 'delai']
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(df[features].dropna())
            pca = PCA(n_components=2)
            pca_result = pca.fit_transform(X_scaled)
            df_pca = pd.DataFrame({'PC1': pca_result[:, 0], 'PC2': pca_result[:, 1], 'Atelier': df['atelier'].values[:len(pca_result)]})
            fig = px.scatter(df_pca, x='PC1', y='PC2', color='Atelier', title=f"PCA (PC1: {pca.explained_variance_ratio_[0]*100:.0f}%, PC2: {pca.explained_variance_ratio_[1]*100:.0f}%)")
            st.plotly_chart(fig, use_container_width=True, key="pca_chart")
        else:
            st.info("Données insuffisantes.")
    
    elif st.session_state['section'] == 'classification':
        st.markdown("### Classification - Recommandation")
        if len(df) >= 10:
            df['cible'] = (df['recommandation'] == 'Oui').astype(int)
            X = df[['budget', 'age', 'satisfaction']].values
            y = df['cible'].values
            rf = RandomForestClassifier(n_estimators=50, random_state=42)
            rf.fit(X, y)
            importance = pd.DataFrame({'Variable': ['Budget', 'Âge', 'Satisfaction'], 'Importance': rf.feature_importances_})
            fig = px.bar(importance, x='Importance', y='Variable', orientation='h')
            st.plotly_chart(fig, use_container_width=True, key="importance_chart")
            st.subheader("🔮 Prédire")
            test_budget = st.number_input("Budget", value=150000)
            test_age = st.slider("Âge", 15, 90, 30)
            test_sat = st.slider("Satisfaction", 1, 5, 4)
            if st.button("Prédire"):
                pred = rf.predict([[test_budget, test_age, test_sat]])[0]
                st.success("✅ Recommanderait") if pred == 1 else st.warning("❌ Ne recommanderait pas")
        else:
            st.info("Données insuffisantes.")
    
    elif st.session_state['section'] == 'clustering':
        st.markdown("### Clustering - Segmentation Clients")
        if len(df) >= 8:
            features = ['budget', 'age', 'satisfaction']
            scaler = StandardScaler()
            X = scaler.fit_transform(df[features].dropna())
            k = st.slider("Nombre de segments", 2, 4, 3)
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            clusters = kmeans.fit_predict(X)
            df['Segment'] = clusters[:len(df)]
            fig = px.scatter(df, x='budget', y='satisfaction', color=clusters.astype(str), title=f"Segmentation en {k} groupes")
            st.plotly_chart(fig, use_container_width=True, key="clustering_chart")
            st.subheader("Profil des segments")
            st.dataframe(df.groupby('Segment')[['budget', 'age', 'satisfaction']].mean())
        else:
            st.info("Données insuffisantes.")

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
    </div>
""", unsafe_allow_html=True)