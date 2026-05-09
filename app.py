import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PrimeFlow",
    layout="wide"
)

st.title("PrimeFlow")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Dossiers actifs", "148")
col2.metric("Taux conformité", "94%")
col3.metric("Factures émises", "82")
col4.metric("Prime moyenne", "4 260 €")

st.subheader("Workflow CEE")

workflow = pd.DataFrame({
    "Étape": [
        "Créé",
        "Contrôle",
        "Documents OK",
        "Déposé",
        "Validé",
        "Facturé"
    ],
    "Total": [12, 8, 31, 54, 28, 15]
})

st.dataframe(workflow, use_container_width=True)

st.subheader("Documents manquants")

docs = pd.DataFrame({
    "Dossier": ["CEE-2041", "CEE-2042", "CEE-2043"],
    "Client": ["Dupont", "Martin", "Bernard"],
    "Alerte": [
        "AH manquante",
        "Photo chantier",
        "Facture artisan"
    ]
})

st.dataframe(docs, use_container_width=True)