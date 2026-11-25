import os
import streamlit as st

st.set_page_config(page_title="Per te, Amorino mio", page_icon="💌", layout="centered")

# --- STILE GRAFICO RAFFINATO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');

.stApp {
    background: linear-gradient(180deg, #fffaf8 0%, #f9e8ee 100%);
    color: #5c3a47;
    font-family: 'Lora', serif;
}

/* Forza il colore scuro leggibile su TUTTI i testi (anche con Dark Mode attiva) */
.stApp p, .stApp label, .stApp span, .stApp div[data-testid="stMarkdownContainer"] p,
div[role="radiogroup"] label, div[role="radiogroup"] p,
div[data-testid="stWidgetLabel"] p, div[data-testid="stCaptionContainer"] p,
.streamlit-expanderHeader p {
    color: #5c3a47 !important;
    font-family: 'Lora', serif !important;
}

/* Mantiene bianco il testo dentro i bottoni rosa */
div.stButton > button, div.stButton > button p, div.stButton > button span {
    color: #fffaf8 !important;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #9e4768 !important;
    text-align: center;
}

.busta-container {
    background: linear-gradient(135deg, #fffdfb 0%, #f7dce5 100%);
    border: 2px solid #e3b5c4;
    border-radius: 18px;
    padding: 45px 25px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(158, 71, 104, 0.12);
    margin: 30px auto;
    max-width: 450px;
}

.sigillo {
    display: inline-block;
    background-color: #b85678;
    color: #fffaf8 !important;
    width: 65px;
    height: 65px;
    line-height: 65px;
    border-radius: 50%;
    font-size: 28px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(184, 86, 120, 0.35);
}

.card-elegante {
    background-color: rgba(255, 253, 251, 0.85);
    border: 1px solid #ebd0d9;
    border-radius: 16px;
    padding: 25px;
    box-shadow: 0 6px 20px rgba(158, 71, 104, 0.06);
    margin: 15px 0;
    line-height: 1.75;
    font-size: 16.5px;
    color: #5c3a47 !important;
}

div.stButton > button {
    background-color: #c97391;
    color: #fffaf8;
    border-radius: 30px;
    width: 100%;
    font-family: 'Lora', serif;
    font-weight: 600;
    font-size: 16px;
    border: none;
    padding: 12px 24px;
    box-shadow: 0 4px 12px rgba(201, 115, 145, 0.25);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background-color: #b05b7b;
    color: #ffffff;
    transform: translateY(-1px);
}

.stProgress > div > div > div > div {
    background-color: #c97391;
}

@keyframes floatUp {
    0% { transform: translateY(0) scale(0.8); opacity: 0; }
    50% { opacity: 0.7; }
    100% { transform: translateY(-80px) scale(1.1); opacity: 0; }
}
.cuore-animato {
    text-align: center;
    font-size: 20px;
    color: #c97391 !important;
    animation: floatUp 3s infinite ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# --- MEMORIA DEGLI STATI ---
if "busta_aperta" not in st.session_state:
    st.session_state.busta_aperta = False
if "numero" not in st.session_state:
    st.session_state.numero = 0
if "quiz_completato" not in st.session_state:
    st.session_state.quiz_completato = False

# ==========================================
# 1. SCHERMATA INIZIALE: LA BUSTA VIRTUALE
# ==========================================
if not st.session_state.busta_aperta:
    st.markdown("<div class='cuore-animato'>♡ &nbsp; ♡ &nbsp; ♡</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="busta-container">
        <div class="sigillo">💌</div>
        <p style="letter-spacing: 2px; font-size: 12px; text-transform: uppercase; color: #9e4768 !important; margin-bottom: 5px;">
            Casella n° 19 • Calendario dell'Avvento
        </p>
        <h1 style="font-style: italic; margin-top: 5px; margin-bottom: 15px;">Per te, Amorino mio</h1>
        <p style="font-size: 16px; color: #6e4756 !important;">
            C'è un piccolo nido custodito qui dentro,<br>creato solo per noi due.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Apri la busta ✨"):
            st.session_state.busta_aperta = True
            st.balloons()
            st.rerun()

# ==========================================
# 2. CONTENUTO DEL SITO (DOPO L'APERTURA)
# ==========================================
else:
    st.title("Il nostro piccolo nido")

    st.markdown("""
    <p style='text-align:center; font-size:18px; font-style: italic;'>
    Ho creato questo piccolo angolo tutto per noi.<br>
    Perché ci sono cose che non voglio dimenticare di dirti.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --- LA TUA LETTERA SEGRETA ---
    st.header("La tua lettera")
    with st.expander("Leggi il messaggio custodito per te", expanded=True):
        st.markdown("""
        <div class="card-elegante">
        Amorino mio,<br><br>

        volevo regalarti qualcosa di diverso dal solito per questo 19 dicembre. Qualcosa che non si compra in un negozio, ma che ho costruito io riga dopo riga (ammetto, con un piccolo aiutino), mettendo in pratica quello che ho imparato in Python con quelle due lezioni che ho seguito online, solo per creare un piccolo spazio tutto nostro.<br><br>

        Da quando ci sei tu, tante cose sono cambiate in meglio, spesso senza nemmeno che me ne accorgessi. Mi ritrovo a sorridere da sola ripensando a quando eravamo a Riva del Garda e, mentre facevamo le cose zozze in doccia, sei scivolato giù; oppure quando ripenso al 18 novembre: era un periodo brutto per me, ma quel giorno sei venuto all'ora di pranzo in ospedale e mi hai tagliato la mela per farmela mangiare. E mi sono persino affezionata a quel tuo lato così perfettino che a volte mi fa impazzire, ma ti amo anche per questo.<br><br>

        Grazie per come mi guardi, per come mi prendi in giro quando faccio finta di essere seria, e soprattutto per farmi sentire sempre al sicuro e libera di essere me stessa al cento per cento. Con te anche le giornate più normali diventano un ricordo che voglio tenermi stretto; con te anche una domenica a casa sotto le coperte a non fare nulla può diventare la più bella domenica di sempre.<br><br>

        Non so esattamente cosa ci riserverà il futuro, quali strade prenderemo o quali nuove sfide dovremo affrontare, ma c'è una cosa di cui sono sicura: voglio riempirlo di risate, di piccoli gesti, di nuovi viaggi e di infiniti momenti insieme a te.<br><br>

        Ti amo tantissimo, più di quanto riesca a scrivere qui dentro.<br><br>

        Sempre tua,<br>
        <b>Lauretta</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- ALBUM DEI NOSTRI RICORDI ---
    st.header("I nostri ricordi")
    st.markdown("<p style='text-align:center; font-size:15px;'>Qualche istante di noi che porto sempre nel cuore.</p>", unsafe_allow_html=True)

    cartella_corrente = os.path.dirname(os.path.abspath(__file__))

    album = [
        ("garda.jpeg", "Riva del Garda (e le famose avventure in doccia...)"),
        ("noi1.jpeg", "Il tuo sguardo seducente (che amo)."),
        ("noi2.jpeg", "Quel giorno migliorato da te e da quel gesto.")
    ]

    for nome_file, didascalia in album:
        percorso_foto = os.path.join(cartella_corrente, nome_file)
        if os.path.exists(percorso_foto):
            st.image(percorso_foto, caption=didascalia, width="stretch")
        else:
            st.markdown(f"""
            <div class="card-elegante" style="text-align:center; padding: 15px; font-size: 14px; color: #8c5c6e !important;">
                <i>Non trovo il file: <b>{nome_file}</b> sul Desktop.</i>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # --- 10 COSE CHE AMO DI TE ---
    st.header("10 cose che amo di te")

    motivi = [
        "1. Il tuo sorriso (che vince a mani basse su tutto, anche quando cerco di fare la seria).",
        "2. La tua capacità soprannaturale di farmi ridere anche quando ho la luna storta.",
        "3. Il tuo essere così tremendamente 'perfettino'... dai, ammetto che nel profondo (ma mooolto nel profondo) lo amo!",
        "4. Il modo in cui mi guardi, che mi fa sciogliere ogni singola volta.",
        "5. Il fatto che con te posso essere me stessa al 100%, senza filtri e in totale libertà.",
        "6. Le tue battute stupide — soprattutto quei 5 secondi di silenzio imbarazzante in cui il mio cervello prova a capirle.",
        "7. La tua voce profonda e rauca appena sveglio la mattina (illegale, davvero).",
        "8. Tutti i tuoi gesti, da quelli enormi a quelli piccolissimi che pensi io non noti (e invece noto eccome).",
        "9. Il tuo prendermi in giro continuamente, anche se faccio finta di offendermi.",
        "10. Semplicemente perché sei tu. E non ti cambierei con nessun altro al mondo"
    ]

    if st.button("Scopri una cosa che amo di te"):
        if st.session_state.numero < 10:
            st.session_state.numero += 1

    if st.session_state.numero > 0:
        st.markdown(f"""
        <div class="card-elegante" style="text-align:center;">
            <h3 style="margin:0;">{motivi[st.session_state.numero - 1]}</h3>
        </div>
        """, unsafe_allow_html=True)
        st.progress(st.session_state.numero / 10)

    if st.session_state.numero == 10:
        st.balloons()
        st.markdown("<p style='text-align:center; font-style:italic;'><b>E potrei continuare all'infinito!</b></p>", unsafe_allow_html=True)

    st.markdown("---")

    # --- IL TUO BUONO SPECIALE ---
    st.header("Il tuo buono speciale")

    with st.expander("Apri il tuo regalo segreto"):
        st.markdown("""
        <div class="card-elegante" style="text-align:center;">
            <h3>BUONO "HAI RAGIONE TU" (VALIDO UNA SOLA VOLTA)</h3>
            <p>Scherzo... ma quasi!</p>
            <p>Questo buono vale per una serata interamente dedicata a te:<br>
            scegli tu cosa mangiamo, cosa guardiamo e cosa facciamo.<br>
            Io penso a tutto il resto (e prometto di non lamentarmi!).</p>
            <p><b>Validità: quando vuoi tu (basta uno screenshot).</b></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- SORPRESA NASCOSTA: MINI-QUIZ SU DI NOI ---
    st.header("Ultima sorpresa nascosta")
    st.markdown("<p style='text-align:center;'>Rispondi correttamente a queste 3 domande su di noi per sbloccare l'ultimo messaggio segreto:</p>", unsafe_allow_html=True)

    q1 = st.radio(
        "1. Qual è stata la prima frase che mi hai detto quel giorno al centro commerciale?",
        ["Seleziona una risposta...", "Dammi da bere", "Ciao bella bambolina", "Non sono un alcolizzato"],
        index=0
    )

    q2 = st.radio(
        "2. Cosa mi hai portato da bere in uno dei nostri primi appuntamenti?",
        ["Seleziona una risposta...", "Un succo ACE", "Tè alla pesca", "Una Corona"],
        index=0
    )

    q3 = st.radio(
        "3. Qual è la mia idea di domenica perfetta con te?",
        ["Seleziona una risposta...", "Fare shopping tutto il giorno", "Stare a casa sotto le coperte a non fare nulla", "Andare a correre alle 7 del mattino"],
        index=0
    )

    if st.button("Sblocca il messaggio finale"):
        if q1 == "Non sono un alcolizzato" and q2 == "Una Corona" and q3 == "Stare a casa sotto le coperte a non fare nulla":
            st.session_state.quiz_completato = True
            st.snow()
        else:
            st.warning("Mmh... riprova! Uno dei ricordi non è esatto (concentrati!).")

    if st.session_state.quiz_completato:
        st.markdown("""
        <div class="card-elegante" style="text-align:center; border: 2px solid #c97391;">
            <h3>Hai sbloccato il finale segreto!</h3>
            <p>
            Complimenti: hai superato l'esame da fidanzato modello con 110 e lode (il tuo lato perfettino sarà fierissimo di te).<br>
            Non importa quanti anni passeranno, quante volte scivolerai in doccia o quante caselle apriremo:<br>
            resti comunque la mia scelta preferita.<br><br>
            <b>Buon 19 dicembre, amore mio. Ora posa il telefono e vieni a riscuotere un bacio (e il tuo buono)!</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <p style='text-align:center; font-size:22px; font-family: "Playfair Display", serif; font-style: italic;'>
    Sei il mio posto preferito.
    </p>
    """, unsafe_allow_html=True)

    st.caption("Creato con amore, solo per te.")