import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PrimeFlow",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- STYLE ----------
st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
}

[data-testid="metric-container"]{
    border:1px solid rgba(255,255,255,.08);
    border-radius:16px;
    padding:18px;
}

[data-testid="stSidebar"]{
    border-right:1px solid rgba(255,255,255,.08);
}

h1,h2,h3{
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)


# ---------- SIDEBAR ----------
with st.sidebar:

    st.title("⚡ PrimeFlow")

    st.markdown("---")

    st.markdown("### Navigation")

    st.markdown("🏠 Dashboard")
    st.markdown("📂 Dossiers")
    st.markdown("📄 Documents")
    st.markdown("💶 Facturation")
    st.markdown("👥 CRM")
    st.markdown("📊 Analytics")

    st.markdown("---")

    st.caption("Prototype by Florian")


# ---------- HEADER ----------
st.title("CEE Workflow Intelligence")
st.caption("Digitalisation métier pour acteurs CEE")


# ---------- KPI ----------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Dossiers actifs", "148", "+12")
c2.metric("Conformité", "94%", "+3%")
c3.metric("Factures", "82", "+7")
c4.metric("Cash Flow", "348k€", "+22k€")


st.divider()


# ---------- PIPELINE ----------
st.subheader("Pipeline opérationnel")

pipeline = pd.DataFrame({
    "Étape":[
        "Créé",
        "Contrôle",
        "Documents OK",
        "Déposé",
        "Validé",
        "Facturé"
    ],
    "Volume":[12,8,31,54,28,15]
})

st.dataframe(
    pipeline,
    hide_index=True,
    use_container_width=True
)


# ---------- BOTTOM ----------
left, right = st.columns(2)

with left:

    st.subheader("⚠ Alertes")

    alerts = pd.DataFrame({
        "Dossier":[
            "CEE-2041",
            "CEE-2042",
            "CEE-2043"
        ],
        "Client":[
            "Dupont",
            "Martin",
            "Bernard"
        ],
        "Action":[
            "AH manquante",
            "Photo chantier",
            "Facture artisan"
        ]
    })

    st.dataframe(
        alerts,
        hide_index=True,
        use_container_width=True
    )


with right:

    st.subheader("💶 Facturation")

    billing = pd.DataFrame({
        "Facture":[
            "FAC-031",
            "FAC-032",
            "FAC-033"
        ],
        "Montant":[
            "12 800€",
            "9 400€",
            "18 200€"
        ],
        "Statut":[
            "Payée",
            "En attente",
            "Validation"
        ]
    })

    st.dataframe(
        billing,
        hide_index=True,
        use_container_width=True
    )