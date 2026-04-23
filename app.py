# ==============================================
# ✨ BECCA STYLE & DESIGN ✨
# Haute Couture & Créations
# Application de collecte et analyse de données
# TP INF232 EC2
# TOUBIWO ANGE BECCA
# ==============================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Becca Style & Design | Haute Couture",
    page_icon="👗",
    layout="wide"
)

# -------------------- STYLE PROFESSIONNEL PERSONNALISÉ --------------------
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
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
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
    div[data-testid="stExpander"] {
        background: white !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- BARRE LATÉRALE ÉLÉGANTE --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1943/1943678.png", width=80)
    st.markdown("---")
    st.markdown("### 👩‍💼 Direction")
    st.markdown("**TOUBIWO ANGE BECCA**")
    st.markdown("*Fondatrice & Directrice Artistique*")
    st.markdown("*Becca Style & Design - Douala*")
    st.markdown("---")
    st.markdown("### 🏢 Nos Ateliers")
    st.markdown("• Douala - Bonapriso")
    st.markdown("• Yaoundé - Bastos")
    st.markdown("• Bafoussam - Centre")
    st.markdown("• Limbé - Bord de mer")
    st.markdown("• Garoua - Centre ville")
    st.markdown("---")
    st.markdown(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown(f"⏰ {datetime.now().strftime('%H:%M')}")

# -------------------- TITRE ET INTRODUCTION --------------------
st.image("https://images.unsplash.com/photo-1590736969955-71cc94901144?w=1200&h=400", use_container_width=True)
st.title("👗 BECCA STYLE & DESIGN")
st.markdown("### ✨ Application de collecte et d'analyse des données clients")

st.markdown("""
    <div style="text-align: center; display: flex; align-items: center; justify-content: center; gap: 10px; margin: 20px 0;">
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
        <span style="color: #800020; font-size: 1.2rem;">✦</span>
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
    </div>
""", unsafe_allow_html=True)

# -------------------- CHEMIN DU FICHIER DE DONNÉES --------------------
DATA_FILE = os.path.join("data", "commandes_couture.csv")

# -------------------- LISTES DES CHOIX --------------------
ATELIERS = [
    "Douala - Bonapriso",
    "Yaoundé - Bastos",
    "Bafoussam - Centre",
    "Limbé - Bord de mer",
    "Garoua - Centre ville"
]

TYPES_TENUES = [
    "Robe de mariée", "Costume de marié", "Tenue de témoin / demoiselle d'honneur",
    "Tenue de mariage traditionnel", "Tenue de dot", "Kaba Ngondo", "Sanja", "Toghu",
    "Boubou africain", "Ensemble pagne wax", "Tenue traditionnelle sur mesure",
    "Robe de soirée longue", "Robe de cocktail", "Costume de gala", "Ensemble jupe + bustier",
    "Tailleur femme", "Robe de bureau", "Costume homme", "Chemise sur mesure",
    "Robe d'été", "Ensemble pantalon + top", "Jupe portefeuille", "Accessoire de luxe (foulard, pochette)"
]

TISSUS = [
    "Soie sauvage", "Dentelle de Calais", "Velours", "Bazin riche", "Wax haut de gamme",
    "Satin", "Crêpe", "Lin", "Coton égyptien", "Tissu traditionnel (Ndop, Obom)",
    "Mousseline", "Organza", "Broderie anglaise"
]

# -------------------- FONCTION POUR CHARGER LES DONNÉES --------------------
def charger_donnees():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return df
        except:
            return pd.DataFrame(columns=["date","atelier","prenom","age","type_tenue","tissu","budget","delai","satisfaction","recommandation"])
    else:
        return pd.DataFrame(columns=["date","atelier","prenom","age","type_tenue","tissu","budget","delai","satisfaction","recommandation"])

# -------------------- FONCTION POUR SAUVEGARDER --------------------
def sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation):
    nouvelle_ligne = pd.DataFrame([{
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "atelier": atelier, "prenom": prenom, "age": age,
        "type_tenue": type_tenue, "tissu": tissu, "budget": budget,
        "delai": delai, "satisfaction": satisfaction, "recommandation": recommandation
    }])
    df_existant = charger_donnees()
    df_final = pd.concat([df_existant, nouvelle_ligne], ignore_index=True)
    os.makedirs("data", exist_ok=True)
    df_final.to_csv(DATA_FILE, index=False)
    return True

# -------------------- CRÉATION DES DEUX COLONNES --------------------
colonne_gauche, colonne_droite = st.columns([1, 2])

# ==============================================
# PARTIE GAUCHE : FORMULAIRE DE SAISIE
# ==============================================
with colonne_gauche:
    st.subheader("📝 Nouvelle commande")
    st.markdown("*À remplir par le responsable d'atelier*")
    
    with st.form("formulaire_commande", clear_on_submit=True):
        atelier = st.selectbox("🏢 Atelier", ATELIERS)
        prenom = st.text_input("👤 Prénom du client / de la cliente", placeholder="Ex: Marie")
        age = st.number_input("🎂 Âge", min_value=15, max_value=90, value=30, step=1)
        type_tenue = st.selectbox("👗 Type de tenue commandée", TYPES_TENUES)
        tissu = st.selectbox("🧶 Tissu principal utilisé", TISSUS)
        budget = st.number_input("💰 Budget total (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000)
        delai = st.number_input("⏱️ Délai de confection (jours)", min_value=1, max_value=90, value=14, step=1)
        satisfaction = st.slider("⭐ Satisfaction client (1 à 5)", 1, 5, 4)
        recommandation = st.radio("👍 Recommanderait-il Becca Style & Design ?", ["Oui", "Non"], horizontal=True)
        
        envoyer = st.form_submit_button("📤 Enregistrer la commande", use_container_width=True)
        
        if envoyer:
            if prenom == "":
                st.error("❌ Veuillez entrer le prénom du client.")
            else:
                sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation)
                st.success(f"✅ Commande de {prenom} enregistrée avec succès !")
                st.balloons()
    
    # --- BOUTON D'ANNULATION DE LA DERNIÈRE COMMANDE ---
    if os.path.exists(DATA_FILE):
        df_data = pd.read_csv(DATA_FILE)
        if not df_data.empty:
            with st.expander("⚠️ Annuler la dernière commande", expanded=False):
                st.warning("Supprime la dernière commande enregistrée en cas d'erreur.")
                derniere_commande = df_data.iloc[-1]
                st.markdown(f"**Dernière commande :** {derniere_commande['prenom']} - {derniere_commande['type_tenue']} ({derniere_commande['atelier']})")
                if st.button("🗑️ Supprimer cette commande", key="supprimer_derniere"):
                    df_data = df_data.iloc[:-1]
                    df_data.to_csv(DATA_FILE, index=False)
                    st.success("✅ Dernière commande supprimée avec succès !")
                    st.rerun()

# ==============================================
# PARTIE DROITE : ANALYSE DES DONNÉES
# ==============================================
with colonne_droite:
    st.subheader("📊 Tableau de bord - Analyse des données collectées")
    
    df = charger_donnees()
    
    if df.empty:
        st.success("👋 Bienvenue chez **Becca Style & Design** ! Voici les données de démonstration. Utilisez le formulaire de gauche pour ajouter de nouvelles commandes.")
        # --- DONNÉES DE DÉMONSTRATION (15 commandes) ---
        df = pd.DataFrame([
            {"date":"2026-04-21 10:00","atelier":"Douala - Bonapriso","prenom":"Marie","age":28,"type_tenue":"Robe de mariée","tissu":"Dentelle de Calais","budget":450000,"delai":30,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 10:30","atelier":"Douala - Bonapriso","prenom":"Jeanne","age":35,"type_tenue":"Tailleur femme","tissu":"Lin","budget":85000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 11:00","atelier":"Douala - Bonapriso","prenom":"Carine","age":22,"type_tenue":"Robe de cocktail","tissu":"Satin","budget":120000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 11:30","atelier":"Yaoundé - Bastos","prenom":"Paul","age":40,"type_tenue":"Costume homme","tissu":"Coton égyptien","budget":150000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 12:00","atelier":"Yaoundé - Bastos","prenom":"Chantal","age":31,"type_tenue":"Kaba Ngondo","tissu":"Wax haut de gamme","budget":95000,"delai":7,"satisfaction":3,"recommandation":"Non"},
            {"date":"2026-04-21 12:30","atelier":"Yaoundé - Bastos","prenom":"Sylvie","age":45,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":200000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 13:00","atelier":"Yaoundé - Bastos","prenom":"Thomas","age":33,"type_tenue":"Costume de marié","tissu":"Soie sauvage","budget":350000,"delai":28,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 13:30","atelier":"Bafoussam - Centre","prenom":"Pauline","age":50,"type_tenue":"Sanja","tissu":"Tissu traditionnel (Ndop, Obom)","budget":110000,"delai":10,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 14:00","atelier":"Bafoussam - Centre","prenom":"Alice","age":27,"type_tenue":"Robe de soirée longue","tissu":"Velours","budget":175000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 14:30","atelier":"Bafoussam - Centre","prenom":"Roger","age":55,"type_tenue":"Costume homme","tissu":"Lin","budget":130000,"delai":14,"satisfaction":3,"recommandation":"Oui"},
            {"date":"2026-04-21 15:00","atelier":"Limbé - Bord de mer","prenom":"Estelle","age":29,"type_tenue":"Robe d'été","tissu":"Coton égyptien","budget":65000,"delai":7,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 15:30","atelier":"Limbé - Bord de mer","prenom":"Flora","age":38,"type_tenue":"Ensemble pagne wax","tissu":"Wax haut de gamme","budget":90000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 16:00","atelier":"Garoua - Centre ville","prenom":"Aïcha","age":26,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":220000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 16:30","atelier":"Garoua - Centre ville","prenom":"Mariam","age":34,"type_tenue":"Tenue de mariage traditionnel","tissu":"Tissu traditionnel (Ndop, Obom)","budget":300000,"delai":30,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 17:00","atelier":"Garoua - Centre ville","prenom":"Fati","age":42,"type_tenue":"Accessoire de luxe (foulard, pochette)","tissu":"Soie sauvage","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"}
        ])
    
    # ----- MÉTRIQUES GLOBALES -----
    st.markdown("#### 📈 Vue d'ensemble")
    met1, met2, met3, met4 = st.columns(4)
    with met1:
        st.metric("📋 Total commandes", len(df))
    with met2:
        st.metric("💰 Budget moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
    with met3:
        st.metric("⭐ Satisfaction moyenne", f"{df['satisfaction'].mean():.1f}/5")
    with met4:
        taux_reco = (df['recommandation'] == "Oui").mean() * 100
        st.metric("👍 Recommandation", f"{taux_reco:.0f}%")
    
    st.markdown("---")
    
    # ----- FILTRE PAR ATELIER -----
    st.markdown("#### 🔍 Analyse par atelier")
    ateliers_disponibles = ["Tous les ateliers"] + list(df['atelier'].unique())
    atelier_selectionne = st.selectbox("Filtrer par atelier :", ateliers_disponibles)
    
    if atelier_selectionne != "Tous les ateliers":
        df_filtre = df[df['atelier'] == atelier_selectionne]
    else:
        df_filtre = df
    
    # ----- GRAPHIQUES -----
    onglet1, onglet2, onglet3 = st.tabs(["📊 Comparaison ateliers", "📈 Tendances", "📋 Gestion des données"])
    
    with onglet1:
        colA, colB = st.columns(2)
        with colA:
            st.subheader("Satisfaction moyenne par atelier")
            satisf_par_atelier = df.groupby('atelier')['satisfaction'].mean().sort_values(ascending=False)
            fig1, ax1 = plt.subplots(figsize=(8, 4))
            couleurs = ['#800020', '#CD5C5C', '#D4A574', '#8B6F47', '#6B8E23']
            bars = ax1.bar(satisf_par_atelier.index, satisf_par_atelier.values, color=couleurs[:len(satisf_par_atelier)])
            ax1.set_ylabel('Satisfaction (/5)')
            ax1.set_ylim(0, 5)
            plt.xticks(rotation=45, ha='right')
            for bar, val in zip(bars, satisf_par_atelier.values):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{val:.1f}', ha='center', fontweight='bold')
            st.pyplot(fig1)
        with colB:
            st.subheader("Nombre de commandes par atelier")
            commandes_par_atelier = df['atelier'].value_counts()
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            bars = ax2.bar(commandes_par_atelier.index, commandes_par_atelier.values, color=couleurs[:len(commandes_par_atelier)])
            ax2.set_ylabel('Nombre de commandes')
            plt.xticks(rotation=45, ha='right')
            for bar, val in zip(bars, commandes_par_atelier.values):
                ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(val), ha='center', fontweight='bold')
            st.pyplot(fig2)
    
    with onglet2:
        colC, colD = st.columns(2)
        with colC:
            st.subheader("Top 5 des tissus")
            top_tissus = df['tissu'].value_counts().head(5)
            if len(top_tissus) > 0:
                fig3, ax3 = plt.subplots(figsize=(6, 4))
                ax3.pie(top_tissus.values, labels=top_tissus.index, autopct='%1.1f%%', colors=couleurs)
                ax3.set_title('Tissus les plus demandés')
                st.pyplot(fig3)
        with colD:
            st.subheader("Top 5 des tenues")
            top_tenues = df['type_tenue'].value_counts().head(5)
            if len(top_tenues) > 0:
                fig4, ax4 = plt.subplots(figsize=(6, 4))
                ax4.pie(top_tenues.values, labels=top_tenues.index, autopct='%1.1f%%', colors=couleurs)
                ax4.set_title('Tenues les plus commandées')
                st.pyplot(fig4)
    
    with onglet3:
        st.subheader("Données brutes")
        st.dataframe(df.sort_values('date', ascending=False), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger (CSV)", data=csv, file_name='export_becca_style_design.csv', mime='text/csv', use_container_width=True)

# -------------------- CITATION INSPIRANTE --------------------
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
        <p>© 2026 <b>Becca Style & Design</b> - TOUBIWO ANGE BECCA</p>
        <p>Application développée dans le cadre du TP INF232 EC2</p>
    </div>
""", unsafe_allow_html=True)
# Haute Couture & Créations
# Application de collecte et analyse de données
# TP INF232 EC2
# TOUBIWO ANGE BECCA
# ==============================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Becca Style & Design | Haute Couture",
    page_icon="👗",
    layout="wide"
)

# -------------------- STYLE PROFESSIONNEL PERSONNALISÉ --------------------
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
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
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
    div[data-testid="stExpander"] {
        background: white !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- BARRE LATÉRALE ÉLÉGANTE --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1943/1943678.png", width=80)
    st.markdown("---")
    st.markdown("### 👩‍💼 Direction")
    st.markdown("**TOUBIWO ANGE BECCA**")
    st.markdown("*Fondatrice & Directrice Artistique*")
    st.markdown("*Becca Style & Design - Douala*")
    st.markdown("---")
    st.markdown("### 🏢 Nos Ateliers")
    st.markdown("• Douala - Bonapriso")
    st.markdown("• Yaoundé - Bastos")
    st.markdown("• Bafoussam - Centre")
    st.markdown("• Limbé - Bord de mer")
    st.markdown("• Garoua - Centre ville")
    st.markdown("---")
    st.markdown(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
    st.markdown(f"⏰ {datetime.now().strftime('%H:%M')}")

# -------------------- TITRE ET INTRODUCTION --------------------
st.image("https://images.unsplash.com/photo-1590736969955-71cc94901144?w=1200&h=400", use_container_width=True)
st.title("👗 BECCA STYLE & DESIGN")
st.markdown("### ✨ Application de collecte et d'analyse des données clients")

st.markdown("""
    <div style="text-align: center; display: flex; align-items: center; justify-content: center; gap: 10px; margin: 20px 0;">
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
        <span style="color: #800020; font-size: 1.2rem;">✦</span>
        <hr style="flex: 1; border: 0.5px solid #800020; opacity: 0.3;">
    </div>
""", unsafe_allow_html=True)

# -------------------- CHEMIN DU FICHIER DE DONNÉES --------------------
DATA_FILE = os.path.join("data", "commandes_couture.csv")

# -------------------- LISTES DES CHOIX --------------------
ATELIERS = [
    "Douala - Bonapriso",
    "Yaoundé - Bastos",
    "Bafoussam - Centre",
    "Limbé - Bord de mer",
    "Garoua - Centre ville"
]

TYPES_TENUES = [
    "Robe de mariée", "Costume de marié", "Tenue de témoin / demoiselle d'honneur",
    "Tenue de mariage traditionnel", "Tenue de dot", "Kaba Ngondo", "Sanja", "Toghu",
    "Boubou africain", "Ensemble pagne wax", "Tenue traditionnelle sur mesure",
    "Robe de soirée longue", "Robe de cocktail", "Costume de gala", "Ensemble jupe + bustier",
    "Tailleur femme", "Robe de bureau", "Costume homme", "Chemise sur mesure",
    "Robe d'été", "Ensemble pantalon + top", "Jupe portefeuille", "Accessoire de luxe (foulard, pochette)"
]

TISSUS = [
    "Soie sauvage", "Dentelle de Calais", "Velours", "Bazin riche", "Wax haut de gamme",
    "Satin", "Crêpe", "Lin", "Coton égyptien", "Tissu traditionnel (Ndop, Obom)",
    "Mousseline", "Organza", "Broderie anglaise"
]

# -------------------- FONCTION POUR CHARGER LES DONNÉES --------------------
def charger_donnees():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return df
        except:
            return pd.DataFrame(columns=["date","atelier","prenom","age","type_tenue","tissu","budget","delai","satisfaction","recommandation"])
    else:
        return pd.DataFrame(columns=["date","atelier","prenom","age","type_tenue","tissu","budget","delai","satisfaction","recommandation"])

# -------------------- FONCTION POUR SAUVEGARDER --------------------
def sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation):
    nouvelle_ligne = pd.DataFrame([{
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "atelier": atelier, "prenom": prenom, "age": age,
        "type_tenue": type_tenue, "tissu": tissu, "budget": budget,
        "delai": delai, "satisfaction": satisfaction, "recommandation": recommandation
    }])
    df_existant = charger_donnees()
    df_final = pd.concat([df_existant, nouvelle_ligne], ignore_index=True)
    os.makedirs("data", exist_ok=True)
    df_final.to_csv(DATA_FILE, index=False)
    return True

# -------------------- CRÉATION DES DEUX COLONNES --------------------
colonne_gauche, colonne_droite = st.columns([1, 2])

# ==============================================
# PARTIE GAUCHE : FORMULAIRE DE SAISIE
# ==============================================
with colonne_gauche:
    st.subheader("📝 Nouvelle commande")
    st.markdown("*À remplir par le responsable d'atelier*")
    
    with st.form("formulaire_commande", clear_on_submit=True):
        atelier = st.selectbox("🏢 Atelier", ATELIERS)
        prenom = st.text_input("👤 Prénom du client / de la cliente", placeholder="Ex: Marie")
        age = st.number_input("🎂 Âge", min_value=15, max_value=90, value=30, step=1)
        type_tenue = st.selectbox("👗 Type de tenue commandée", TYPES_TENUES)
        tissu = st.selectbox("🧶 Tissu principal utilisé", TISSUS)
        budget = st.number_input("💰 Budget total (FCFA)", min_value=10000, max_value=2000000, value=150000, step=10000)
        delai = st.number_input("⏱️ Délai de confection (jours)", min_value=1, max_value=90, value=14, step=1)
        satisfaction = st.slider("⭐ Satisfaction client (1 à 5)", 1, 5, 4)
        recommandation = st.radio("👍 Recommanderait-il Becca Style & Design ?", ["Oui", "Non"], horizontal=True)
        
        envoyer = st.form_submit_button("📤 Enregistrer la commande", use_container_width=True)
        
        if envoyer:
            if prenom == "":
                st.error("❌ Veuillez entrer le prénom du client.")
            else:
                sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation)
                st.success(f"✅ Commande de {prenom} enregistrée avec succès !")
                st.balloons()
    
    # --- BOUTON D'ANNULATION DE LA DERNIÈRE COMMANDE ---
    if os.path.exists(DATA_FILE):
        df_data = pd.read_csv(DATA_FILE)
        if not df_data.empty:
            with st.expander("⚠️ Annuler la dernière commande", expanded=False):
                st.warning("Supprime la dernière commande enregistrée en cas d'erreur.")
                derniere_commande = df_data.iloc[-1]
                st.markdown(f"**Dernière commande :** {derniere_commande['prenom']} - {derniere_commande['type_tenue']} ({derniere_commande['atelier']})")
                if st.button("🗑️ Supprimer cette commande", key="supprimer_derniere"):
                    df_data = df_data.iloc[:-1]
                    df_data.to_csv(DATA_FILE, index=False)
                    st.success("✅ Dernière commande supprimée avec succès !")
                    st.rerun()

# ==============================================
# PARTIE DROITE : ANALYSE DES DONNÉES
# ==============================================
with colonne_droite:
    st.subheader("📊 Tableau de bord - Analyse des données collectées")
    
    df = charger_donnees()
    
    if df.empty:
        st.success("👋 Bienvenue chez **Becca Style & Design** ! Voici les données de démonstration. Utilisez le formulaire de gauche pour ajouter de nouvelles commandes.")
        # --- DONNÉES DE DÉMONSTRATION (15 commandes) ---
        df = pd.DataFrame([
            {"date":"2026-04-21 10:00","atelier":"Douala - Bonapriso","prenom":"Marie","age":28,"type_tenue":"Robe de mariée","tissu":"Dentelle de Calais","budget":450000,"delai":30,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 10:30","atelier":"Douala - Bonapriso","prenom":"Jeanne","age":35,"type_tenue":"Tailleur femme","tissu":"Lin","budget":85000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 11:00","atelier":"Douala - Bonapriso","prenom":"Carine","age":22,"type_tenue":"Robe de cocktail","tissu":"Satin","budget":120000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 11:30","atelier":"Yaoundé - Bastos","prenom":"Paul","age":40,"type_tenue":"Costume homme","tissu":"Coton égyptien","budget":150000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 12:00","atelier":"Yaoundé - Bastos","prenom":"Chantal","age":31,"type_tenue":"Kaba Ngondo","tissu":"Wax haut de gamme","budget":95000,"delai":7,"satisfaction":3,"recommandation":"Non"},
            {"date":"2026-04-21 12:30","atelier":"Yaoundé - Bastos","prenom":"Sylvie","age":45,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":200000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 13:00","atelier":"Yaoundé - Bastos","prenom":"Thomas","age":33,"type_tenue":"Costume de marié","tissu":"Soie sauvage","budget":350000,"delai":28,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 13:30","atelier":"Bafoussam - Centre","prenom":"Pauline","age":50,"type_tenue":"Sanja","tissu":"Tissu traditionnel (Ndop, Obom)","budget":110000,"delai":10,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 14:00","atelier":"Bafoussam - Centre","prenom":"Alice","age":27,"type_tenue":"Robe de soirée longue","tissu":"Velours","budget":175000,"delai":21,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 14:30","atelier":"Bafoussam - Centre","prenom":"Roger","age":55,"type_tenue":"Costume homme","tissu":"Lin","budget":130000,"delai":14,"satisfaction":3,"recommandation":"Oui"},
            {"date":"2026-04-21 15:00","atelier":"Limbé - Bord de mer","prenom":"Estelle","age":29,"type_tenue":"Robe d'été","tissu":"Coton égyptien","budget":65000,"delai":7,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 15:30","atelier":"Limbé - Bord de mer","prenom":"Flora","age":38,"type_tenue":"Ensemble pagne wax","tissu":"Wax haut de gamme","budget":90000,"delai":10,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 16:00","atelier":"Garoua - Centre ville","prenom":"Aïcha","age":26,"type_tenue":"Boubou africain","tissu":"Bazin riche","budget":220000,"delai":14,"satisfaction":5,"recommandation":"Oui"},
            {"date":"2026-04-21 16:30","atelier":"Garoua - Centre ville","prenom":"Mariam","age":34,"type_tenue":"Tenue de mariage traditionnel","tissu":"Tissu traditionnel (Ndop, Obom)","budget":300000,"delai":30,"satisfaction":4,"recommandation":"Oui"},
            {"date":"2026-04-21 17:00","atelier":"Garoua - Centre ville","prenom":"Fati","age":42,"type_tenue":"Accessoire de luxe (foulard, pochette)","tissu":"Soie sauvage","budget":45000,"delai":5,"satisfaction":5,"recommandation":"Oui"}
        ])
    
    # ----- MÉTRIQUES GLOBALES -----
    st.markdown("#### 📈 Vue d'ensemble")
    met1, met2, met3, met4 = st.columns(4)
    with met1:
        st.metric("📋 Total commandes", len(df))
    with met2:
        st.metric("💰 Budget moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
    with met3:
        st.metric("⭐ Satisfaction moyenne", f"{df['satisfaction'].mean():.1f}/5")
    with met4:
        taux_reco = (df['recommandation'] == "Oui").mean() * 100
        st.metric("👍 Recommandation", f"{taux_reco:.0f}%")
    
    st.markdown("---")
    
    # ----- FILTRE PAR ATELIER -----
    st.markdown("#### 🔍 Analyse par atelier")
    ateliers_disponibles = ["Tous les ateliers"] + list(df['atelier'].unique())
    atelier_selectionne = st.selectbox("Filtrer par atelier :", ateliers_disponibles)
    
    if atelier_selectionne != "Tous les ateliers":
        df_filtre = df[df['atelier'] == atelier_selectionne]
    else:
        df_filtre = df
    
    # ----- GRAPHIQUES -----
    onglet1, onglet2, onglet3 = st.tabs(["📊 Comparaison ateliers", "📈 Tendances", "📋 Gestion des données"])
    
    with onglet1:
        colA, colB = st.columns(2)
        with colA:
            st.subheader("Satisfaction moyenne par atelier")
            satisf_par_atelier = df.groupby('atelier')['satisfaction'].mean().sort_values(ascending=False)
            fig1, ax1 = plt.subplots(figsize=(8, 4))
            couleurs = ['#800020', '#CD5C5C', '#D4A574', '#8B6F47', '#6B8E23']
            bars = ax1.bar(satisf_par_atelier.index, satisf_par_atelier.values, color=couleurs[:len(satisf_par_atelier)])
            ax1.set_ylabel('Satisfaction (/5)')
            ax1.set_ylim(0, 5)
            plt.xticks(rotation=45, ha='right')
            for bar, val in zip(bars, satisf_par_atelier.values):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{val:.1f}', ha='center', fontweight='bold')
            st.pyplot(fig1)
        with colB:
            st.subheader("Nombre de commandes par atelier")
            commandes_par_atelier = df['atelier'].value_counts()
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            bars = ax2.bar(commandes_par_atelier.index, commandes_par_atelier.values, color=couleurs[:len(commandes_par_atelier)])
            ax2.set_ylabel('Nombre de commandes')
            plt.xticks(rotation=45, ha='right')
            for bar, val in zip(bars, commandes_par_atelier.values):
                ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(val), ha='center', fontweight='bold')
            st.pyplot(fig2)
    
    with onglet2:
        colC, colD = st.columns(2)
        with colC:
            st.subheader("Top 5 des tissus")
            top_tissus = df['tissu'].value_counts().head(5)
            if len(top_tissus) > 0:
                fig3, ax3 = plt.subplots(figsize=(6, 4))
                ax3.pie(top_tissus.values, labels=top_tissus.index, autopct='%1.1f%%', colors=couleurs)
                ax3.set_title('Tissus les plus demandés')
                st.pyplot(fig3)
        with colD:
            st.subheader("Top 5 des tenues")
            top_tenues = df['type_tenue'].value_counts().head(5)
            if len(top_tenues) > 0:
                fig4, ax4 = plt.subplots(figsize=(6, 4))
                ax4.pie(top_tenues.values, labels=top_tenues.index, autopct='%1.1f%%', colors=couleurs)
                ax4.set_title('Tenues les plus commandées')
                st.pyplot(fig4)
    
    with onglet3:
        st.subheader("Données brutes")
        st.dataframe(df.sort_values('date', ascending=False), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger (CSV)", data=csv, file_name='export_becca_style_design.csv', mime='text/csv', use_container_width=True)

# -------------------- CITATION INSPIRANTE --------------------
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
        <p>© 2026 <b>Becca Style & Design</b> - TOUBIWO ANGE BECCA</p>
        <p>Application développée dans le cadre du TP INF232 EC2</p>
    </div>
""", unsafe_allow_html=True)
