# ==============================================
# MAISON DE COUTURE ÉLÉGANCE
# Application de collecte et analyse de données
# TP INF232 EC2
# ==============================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------- CONFIGURATION DE LA PAGE --------------------
st.set_page_config(
    page_title="Maison de Couture Élégance",
    page_icon="👗",
    layout="wide"
)

# -------------------- TITRE ET INTRODUCTION --------------------
st.title("👗 MAISON DE COUTURE ÉLÉGANCE")
st.markdown("### Application de collecte et d'analyse des données clients")
st.markdown("---")

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
    "Robe de mariée",
    "Costume de marié",
    "Tenue de témoin / demoiselle d'honneur",
    "Tenue de mariage traditionnel",
    "Tenue de dot",
    "Kaba Ngondo",
    "Sanja",
    "Toghu",
    "Boubou africain",
    "Ensemble pagne wax",
    "Tenue traditionnelle sur mesure",
    "Robe de soirée longue",
    "Robe de cocktail",
    "Costume de gala",
    "Ensemble jupe + bustier",
    "Tailleur femme",
    "Robe de bureau",
    "Costume homme",
    "Chemise sur mesure",
    "Robe d'été",
    "Ensemble pantalon + top",
    "Jupe portefeuille",
    "Accessoire de luxe (foulard, pochette)"
]

TISSUS = [
    "Soie sauvage",
    "Dentelle de Calais",
    "Velours",
    "Bazin riche",
    "Wax haut de gamme",
    "Satin",
    "Crêpe",
    "Lin",
    "Coton égyptien",
    "Tissu traditionnel (Ndop, Obom)",
    "Mousseline",
    "Organza",
    "Broderie anglaise"
]

# -------------------- FONCTION POUR CHARGER LES DONNÉES --------------------
def charger_donnees():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return df
        except:
            return pd.DataFrame(columns=[
                "date", "atelier", "prenom", "age", "type_tenue", 
                "tissu", "budget", "delai", "satisfaction", "recommandation"
            ])
    else:
        return pd.DataFrame(columns=[
            "date", "atelier", "prenom", "age", "type_tenue", 
            "tissu", "budget", "delai", "satisfaction", "recommandation"
        ])

# -------------------- FONCTION POUR SAUVEGARDER UNE NOUVELLE COMMANDE --------------------
def sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation):
    nouvelle_ligne = pd.DataFrame([{
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "atelier": atelier,
        "prenom": prenom,
        "age": age,
        "type_tenue": type_tenue,
        "tissu": tissu,
        "budget": budget,
        "delai": delai,
        "satisfaction": satisfaction,
        "recommandation": recommandation
    }])
    
    df_existant = charger_donnees()
    df_final = pd.concat([df_existant, nouvelle_ligne], ignore_index=True)
    
    os.makedirs("data", exist_ok=True)
    df_final.to_csv(DATA_FILE, index=False)
    return True

# -------------------- CRÉATION DES DEUX COLONNES PRINCIPALES --------------------
colonne_gauche, colonne_droite = st.columns([1, 2])

# ==============================================
# PARTIE GAUCHE : FORMULAIRE DE SAISIE
# ==============================================
with colonne_gauche:
    st.subheader("📝 Saisie d'une nouvelle commande")
    st.markdown("À remplir par le responsable d'atelier")
    
    with st.form("formulaire_commande", clear_on_submit=True):
        # Choix de l'atelier
        atelier = st.selectbox("🏢 Atelier", ATELIERS)
        
        # Informations client
        prenom = st.text_input("👤 Prénom du client / de la cliente", placeholder="Ex: Marie")
        age = st.number_input("🎂 Âge", min_value=15, max_value=90, value=30, step=1)
        
        # Détails de la commande
        type_tenue = st.selectbox("👗 Type de tenue commandée", TYPES_TENUES)
        tissu = st.selectbox("🧶 Tissu principal utilisé", TISSUS)
        
        budget = st.number_input(
            "💰 Budget total de la commande (FCFA)",
            min_value=10000, max_value=2000000, value=150000, step=10000
        )
        
        delai = st.number_input(
            "⏱️ Délai de confection (jours)",
            min_value=1, max_value=90, value=14, step=1
        )
        
        # Retour client
        satisfaction = st.slider(
            "⭐ Satisfaction client (1 = très mauvais, 5 = excellent)",
            min_value=1, max_value=5, value=4
        )
        
        recommandation = st.radio(
            "👍 Le client recommanderait-il notre maison ?",
            ["Oui", "Non"], horizontal=True
        )
        
        # Bouton de soumission
        envoyer = st.form_submit_button("📤 Enregistrer la commande", use_container_width=True)
        
        if envoyer:
            if prenom == "":
                st.error("❌ Veuillez entrer le prénom du client.")
            else:
                sauvegarder_commande(atelier, prenom, age, type_tenue, tissu, budget, delai, satisfaction, recommandation)
                st.success(f"✅ Commande de {prenom} enregistrée avec succès !")
                st.balloons()

# ==============================================
# PARTIE DROITE : ANALYSE DES DONNÉES
# ==============================================
with colonne_droite:
    st.subheader("📊 Tableau de bord - Analyse des données collectées")
    
    df = charger_donnees()
    
    if df.empty:
        st.info("👆 Aucune commande enregistrée pour le moment. Utilisez le formulaire de gauche pour commencer la collecte.")
    else:
        # ----- MÉTRIQUES GLOBALES -----
        st.markdown("#### 📈 Vue d'ensemble du groupe")
        
        met1, met2, met3, met4 = st.columns(4)
        with met1:
            st.metric("📋 Total commandes", len(df))
        with met2:
            st.metric("💰 Budget moyen", f"{df['budget'].mean():,.0f} FCFA".replace(",", " "))
        with met3:
            st.metric("⭐ Satisfaction moyenne", f"{df['satisfaction'].mean():.1f}/5")
        with met4:
            taux_reco = (df['recommandation'] == "Oui").mean() * 100
            st.metric("👍 Taux de recommandation", f"{taux_reco:.0f}%")
        
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
        onglet1, onglet2, onglet3 = st.tabs(["📊 Comparaison ateliers", "📈 Tendances", "📋 Données brutes"])
        
        with onglet1:
            colA, colB = st.columns(2)
            
            with colA:
                st.subheader("Satisfaction moyenne par atelier")
                if len(df['atelier'].unique()) > 0:
                    satisf_par_atelier = df.groupby('atelier')['satisfaction'].mean().sort_values(ascending=False)
                    
                    fig1, ax1 = plt.subplots(figsize=(8, 4))
                    couleurs = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
                    bars = ax1.bar(satisf_par_atelier.index, satisf_par_atelier.values, color=couleurs[:len(satisf_par_atelier)])
                    ax1.set_ylabel('Satisfaction moyenne (/5)')
                    ax1.set_xlabel('Atelier')
                    ax1.set_ylim(0, 5)
                    plt.xticks(rotation=45, ha='right')
                    
                    for bar, val in zip(bars, satisf_par_atelier.values):
                        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
                                f'{val:.1f}', ha='center', va='bottom', fontweight='bold')
                    
                    st.pyplot(fig1)
                else:
                    st.info("Données insuffisantes")
            
            with colB:
                st.subheader("Nombre de commandes par atelier")
                commandes_par_atelier = df['atelier'].value_counts()
                
                fig2, ax2 = plt.subplots(figsize=(8, 4))
                couleurs = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
                bars = ax2.bar(commandes_par_atelier.index, commandes_par_atelier.values, color=couleurs[:len(commandes_par_atelier)])
                ax2.set_ylabel('Nombre de commandes')
                ax2.set_xlabel('Atelier')
                plt.xticks(rotation=45, ha='right')
                
                for bar, val in zip(bars, commandes_par_atelier.values):
                    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                            str(val), ha='center', va='bottom', fontweight='bold')
                
                st.pyplot(fig2)
        
        with onglet2:
            colC, colD = st.columns(2)
            
            with colC:
                st.subheader("Top 5 des tissus les plus demandés")
                top_tissus = df['tissu'].value_counts().head(5)
                
                if len(top_tissus) > 0:
                    fig3, ax3 = plt.subplots(figsize=(6, 4))
                    ax3.pie(top_tissus.values, labels=top_tissus.index, autopct='%1.1f%%', 
                           colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
                    ax3.set_title('Répartition des tissus')
                    st.pyplot(fig3)
                else:
                    st.info("Données insuffisantes")
            
            with colD:
                st.subheader("Top 5 des tenues les plus commandées")
                top_tenues = df['type_tenue'].value_counts().head(5)
                
                if len(top_tenues) > 0:
                    fig4, ax4 = plt.subplots(figsize=(6, 4))
                    ax4.pie(top_tenues.values, labels=top_tenues.index, autopct='%1.1f%%',
                           colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
                    ax4.set_title('Types de tenues commandées')
                    st.pyplot(fig4)
                else:
                    st.info("Données insuffisantes")
            
            st.markdown("---")
            st.subheader("📊 Statistiques détaillées par atelier")
            
            # Tableau récapitulatif par atelier
            recap = df.groupby('atelier').agg({
                'budget': ['count', 'mean'],
                'satisfaction': 'mean',
                'delai': 'mean'
            }).round(1)
            
            recap.columns = ['Nombre commandes', 'Budget moyen', 'Satisfaction moyenne', 'Délai moyen']
            recap['Budget moyen'] = recap['Budget moyen'].apply(lambda x: f"{x:,.0f} FCFA".replace(",", " "))
            recap['Délai moyen'] = recap['Délai moyen'].apply(lambda x: f"{x:.0f} jours")
            recap['Satisfaction moyenne'] = recap['Satisfaction moyenne'].apply(lambda x: f"{x:.1f}/5")
            
            st.dataframe(recap, use_container_width=True)
        
        with onglet3:
            st.subheader("Données brutes")
            st.dataframe(df.sort_values('date', ascending=False), use_container_width=True)
            
            # Bouton de téléchargement
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Télécharger toutes les données (CSV)",
                data=csv,
                file_name='export_commandes_couture.csv',
                mime='text/csv',
                use_container_width=True
            )