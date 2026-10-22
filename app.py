import streamlit as st

st.set_page_config(
    page_title="Amity School Help Desk",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="expanded",
)

# School details supplied for this student project. Verify all details with the school
# before using this demo as an official information channel.
SCHOOL_NAME = "Amity International School, Mayur Vihar"
RECEPTION_PHONE = "011-22717261"
SCHOOL_WEBSITE = "https://amityschools.in/mayurvihar/"
AMITRANET_URL = "https://amitranet.amizone.net"
AMITRANET_APP_URL = "https://play.google.com/store/apps/details?id=com.amizone.amitranet"

st.markdown(
    """
    <style>
      :root { --amity-navy: #12315a; --amity-blue: #1d5fa7; --amity-teal: #21a6a1; }
      .block-container {max-width: 980px; padding-top: 1.4rem; padding-bottom: 2.5rem;}
      [data-testid="stSidebar"] {border-right: 1px solid rgba(100,116,139,.18);}
      .hero {
        position: relative; overflow: hidden; padding: 1.8rem 1.8rem 1.65rem;
        border-radius: 24px; margin: .35rem 0 1.2rem;
        color: white; background: linear-gradient(120deg, #102c50 0%, #185a91 62%, #178f98 100%);
        box-shadow: 0 14px 35px rgba(18,49,90,.16);
      }
      .hero:after {content:""; position:absolute; width:220px; height:220px; right:-55px; top:-95px;
        border: 28px solid rgba(255,255,255,.10); border-radius:50%; pointer-events:none;}
      .hero:before {content:""; position:absolute; width:100px; height:100px; right:110px; bottom:-65px;
        background:rgba(255,255,255,.08); border-radius:28px; transform:rotate(35deg); pointer-events:none;}
      .hero .eyebrow {font-size:.75rem; letter-spacing:.13em; text-transform:uppercase; font-weight:700; opacity:.8; margin-bottom:.5rem;}
      .hero h1 {margin:0 0 .4rem; font-size:2rem; line-height:1.15; color:white;}
      .hero p {margin:0; max-width:620px; color:rgba(255,255,255,.86); font-size:1rem;}
      .hero .hero-mark {font-size:2.2rem; margin-bottom:.35rem;}
      .section-heading {font-size:1.05rem; font-weight:700; margin:.25rem 0 .25rem;}
      .section-sub {font-size:.88rem; opacity:.72; margin:0 0 .75rem;}
      .info-card {border:1px solid rgba(100,116,139,.20); border-radius:16px; padding:1rem 1.05rem;
        background:linear-gradient(145deg, rgba(255,255,255,.92), rgba(239,246,255,.75)); min-height:108px;}
      @media (prefers-color-scheme: dark) {
        .info-card {background:linear-gradient(145deg, rgba(30,41,59,.8), rgba(15,45,70,.65));}
      }
      .info-icon {font-size:1.35rem; margin-bottom:.35rem;}
      .info-label {font-size:.76rem; text-transform:uppercase; letter-spacing:.06em; opacity:.68; font-weight:700;}
      .info-value {font-size:1rem; font-weight:700; margin-top:.2rem;}
      .small-note {font-size:.82rem; opacity:.72; line-height:1.55;}
      div[data-testid="stChatMessage"] {border-radius:16px; padding:.25rem .45rem;}
      div[data-testid="stExpander"] {border-radius:16px; border-color:rgba(100,116,139,.22);}
      div.stButton > button, div.stLinkButton > a {border-radius:11px; font-weight:600;}
      div[data-testid="stChatInput"] {border-radius:16px;}
      .footer-line {text-align:center; opacity:.58; font-size:.78rem; padding:.5rem 0 .2rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

language = st.radio("Language", ["English", "हिन्दी"], horizontal=True, key="ui_language")
lang = "en" if language == "English" else "hi"

st.markdown(
    f'<div class="hero"><div class="hero-mark">🏫</div>'
    f'<div class="eyebrow">{"AMITY INTERNATIONAL SCHOOL · MAYUR VIHAR" if lang == "en" else "एमिटी इंटरनेशनल स्कूल · मयूर विहार"}</div>'
    f'<h1>{"School Help Desk" if lang == "en" else "स्कूल सहायता केंद्र"}</h1>'
    f'<p>{"A simple place to find school information, useful links and contact details." if lang == "en" else "स्कूल की जानकारी, उपयोगी लिंक और संपर्क विवरण पाने का आसान माध्यम।"}</p></div>',
    unsafe_allow_html=True,
)

# At-a-glance cards add a little visual structure without distracting from the chat.
card_cols = st.columns(3)
card_data = (
    [("🕘", "SCHOOL HOURS", "7:50 AM – 1:50 PM"), ("☎️", "RECEPTION", RECEPTION_PHONE), ("🌐", "ONLINE ACCESS", "Amitranet portal")]
    if lang == "en" else
    [("🕘", "स्कूल का समय", "सुबह 7:50 – दोपहर 1:50"), ("☎️", "रिसेप्शन", RECEPTION_PHONE), ("🌐", "ऑनलाइन सुविधा", "Amitranet पोर्टल")]
)
for card_col, (card_icon, card_label, card_value) in zip(card_cols, card_data):
    with card_col:
        st.markdown(
            f'<div class="info-card"><div class="info-icon">{card_icon}</div>'
            f'<div class="info-label">{card_label}</div><div class="info-value">{card_value}</div></div>',
            unsafe_allow_html=True,
        )
st.write("")

with st.sidebar:
    st.subheader("School links" if lang == "en" else "स्कूल लिंक")
    st.link_button("Official school website" if lang == "en" else "स्कूल की आधिकारिक वेबसाइट", SCHOOL_WEBSITE, use_container_width=True)
    st.link_button("Amitranet portal" if lang == "en" else "Amitranet पोर्टल", AMITRANET_URL, use_container_width=True)
    st.link_button("Amitranet Android app" if lang == "en" else "Amitranet Android ऐप", AMITRANET_APP_URL, use_container_width=True)
    st.markdown("### Reception" if lang == "en" else "### रिसेप्शन")
    st.write(f"**{RECEPTION_PHONE}**")
    st.link_button("📞 Call reception" if lang == "en" else "📞 रिसेप्शन पर कॉल करें", f"tel:{RECEPTION_PHONE}", use_container_width=True)
    st.caption("For urgent or account-specific questions, contact the school directly." if lang == "en" else "ज़रूरी या व्यक्तिगत जानकारी के लिए सीधे स्कूल से संपर्क करें।")
    st.divider()
    st.caption("Demo project · Verify information against current school circulars." if lang == "en" else "डेमो प्रोजेक्ट · जानकारी की पुष्टि नवीनतम स्कूल सर्कुलर से करें।")

FAQS = {
    "en": {
        "id": (
            "If your school ID card is lost, please contact reception to confirm the replacement procedure. Do not share your student ID or personal details in this chat.",
            ["id card", "lost id", "identity card", "school id", "lost card"],
        ),
        "fees": (
            "For fee-related questions, please contact the school's Accounts Section. For online payment, use the school-approved Amitranet/app process and confirm the current instructions with the school. Do not enter payment or bank details here.",
            ["fee", "fees", "payment", "accounts", "tuition", "dues", "फीस"],
        ),
        "bus": (
            f"For current bus routes and stops, sign in to Amitranet using your school-provided credentials: [{AMITRANET_URL}]({AMITRANET_URL}). If the details are unavailable, contact reception at **{RECEPTION_PHONE}**. This demo does not have access to live transport records.",
            ["bus", "route", "transport", "stop", "school bus", "bus number"],
        ),
        "teacher": (
            f"For teacher contact details or an appointment, please follow the school's approved communication process or contact reception at **{RECEPTION_PHONE}**. This chatbot does not have a verified directory of teachers' personal contact details.",
            ["teacher", "meet teacher", "email teacher", "contact teacher", "class teacher", "appointment"],
        ),
        "leave": (
            "For absence or leave, follow the procedure communicated by your class teacher or the school app. Confirm the required format and recipient with the school. Please do not share medical or other sensitive personal details in this chatbot.",
            ["leave", "absent", "absence", "sick leave", "holiday application", "छुट्टी आवेदन"],
        ),
        "datesheet": (
            "**Class XII Pre-Board dates shared for this demo**\n\n"
            "| Date | Subject |\n|---|---|\n"
            "| 26 October 2026 | Sixth Subject |\n"
            "| 2 November 2026 | Physics |\n"
            "| 13 November 2026 | English |\n"
            "| 18 November 2026 | Chemistry |\n"
            "| 30 November 2026 | Mathematics |",
            ["datesheet", "date sheet", "exam date", "examination", "planner", "exam", "unit test", "preboard", "pre-board", "pre board", "paper date", "test date"],
        ),
        "timing": (
            "The school timing previously provided for this project is **7:50 a.m. to 1:50 p.m.** Timings, holidays, and special schedules can change, so please check the latest circular or contact reception before travelling.",
            ["timing", "school time", "opening time", "closing time", "what time", "school hours", "holiday", "holidays"],
        ),
        "homework": (
            "Homework is assigned by teachers and may also be shared through the school-approved app or class communication channels. Please check your class instructions and contact your teacher if something is missing.",
            ["homework", "assignment", "classwork", "work to do", "home work"],
        ),
        "website": (
            f"School information and services: [official school website]({SCHOOL_WEBSITE}) · [Amitranet portal]({AMITRANET_URL}) · [Amitranet Android app]({AMITRANET_APP_URL}). Use only login details provided by the school. If a link has changed, confirm it with reception.",
            ["amitranet", "school app", "app", "online portal", "website", "website login", "browser", "school website", "login"],
        ),
        "contact": (
            f"You can contact the school reception at **{RECEPTION_PHONE}**. Tap the **Call reception** link in the sidebar on a compatible device, or use the [official school website]({SCHOOL_WEBSITE}) to confirm contact details.",
            ["contact", "phone", "call", "reception", "telephone", "number", "address"],
        ),
    },
    "hi": {
        "id": (
            f"यदि स्कूल का आई-कार्ड खो गया है, तो नया कार्ड बनवाने की प्रक्रिया जानने के लिए रिसेप्शन से संपर्क करें: **{RECEPTION_PHONE}**। इस चैट में अपना विद्यार्थी आईडी या निजी जानकारी साझा न करें।",
            ["आई कार्ड", "आई-कार्ड", "id card", "पहचान पत्र", "कार्ड खो"],
        ),
        "fees": (
            "फीस से संबंधित प्रश्नों के लिए स्कूल के Accounts Section से संपर्क करें। ऑनलाइन भुगतान के लिए स्कूल द्वारा स्वीकृत Amitranet/ऐप प्रक्रिया का उपयोग करें और वर्तमान निर्देशों की पुष्टि कर लें। यहाँ बैंक या भुगतान संबंधी विवरण न डालें।",
            ["फीस", "शुल्क", "पेमेंट", "अकाउंट्स", "भुगतान", "fees", "payment"],
        ),
        "bus": (
            f"बस रूट और स्टॉप की नवीनतम जानकारी के लिए स्कूल द्वारा दिए गए लॉगिन विवरण से [Amitranet]({AMITRANET_URL}) पर लॉगिन करें। जानकारी न मिले तो रिसेप्शन **{RECEPTION_PHONE}** पर संपर्क करें। इस डेमो को लाइव परिवहन रिकॉर्ड की पहुँच नहीं है।",
            ["बस", "रूट", "परिवहन", "bus", "route", "स्टॉप", "स्कूल बस"],
        ),
        "teacher": (
            f"शिक्षक से संपर्क या मुलाकात के लिए स्कूल की स्वीकृत प्रक्रिया अपनाएँ या रिसेप्शन **{RECEPTION_PHONE}** पर संपर्क करें। इस चैटबॉट में शिक्षकों के निजी संपर्क विवरण की सत्यापित सूची उपलब्ध नहीं है।",
            ["शिक्षक", "टीचर", "मिलना", "ईमेल", "teacher", "क्लास टीचर", "मुलाकात"],
        ),
        "leave": (
            "अनुपस्थिति या छुट्टी के लिए क्लास टीचर द्वारा बताई गई प्रक्रिया या स्कूल ऐप का उपयोग करें। आवश्यक प्रारूप और प्राप्तकर्ता की पुष्टि स्कूल से करें। इस चैट में संवेदनशील निजी जानकारी साझा न करें।",
            ["छुट्टी", "अनुपस्थित", "अवकाश", "leave", "absent", "छुट्टी आवेदन"],
        ),
        "datesheet": (
            "**कक्षा XII की प्री-बोर्ड डेटशीट — इस डेमो के लिए साझा जानकारी**\n\n"
            "| तारीख | विषय |\n|---|---|\n"
            "| 26 अक्टूबर 2026 | छठा विषय |\n"
            "| 2 नवंबर 2026 | भौतिक विज्ञान (Physics) |\n"
            "| 13 नवंबर 2026 | अंग्रेज़ी (English) |\n"
            "| 18 नवंबर 2026 | रसायन विज्ञान (Chemistry) |\n"
            "| 30 नवंबर 2026 | गणित (Mathematics) |",
            ["डेटशीट", "तारीख", "परीक्षा", "प्लानर", "datesheet", "exam", "unit test", "preboard", "pre-board", "प्री-बोर्ड", "प्री बोर्ड", "पेपर की तारीख"],
        ),
        "timing": (
            "इस प्रोजेक्ट के लिए पहले साझा किया गया स्कूल समय **सुबह 7:50 से दोपहर 1:50 बजे तक** है। समय, छुट्टियाँ और विशेष कार्यक्रम बदल सकते हैं, इसलिए आने से पहले नवीनतम सर्कुलर देखें या रिसेप्शन से पुष्टि करें।",
            ["समय", "टाइमिंग", "स्कूल का समय", "कितने बजे", "छुट्टी", "अवकाश", "स्कूल टाइम"],
        ),
        "homework": (
            "होमवर्क शिक्षक देते हैं और इसे स्कूल द्वारा स्वीकृत ऐप या कक्षा के सूचना चैनलों पर भी साझा किया जा सकता है। अपनी कक्षा के निर्देश देखें; कोई जानकारी न मिले तो शिक्षक से पूछें।",
            ["होमवर्क", "गृहकार्य", "असाइनमेंट", "काम", "homework", "assignment"],
        ),
        "website": (
            f"स्कूल की जानकारी और सेवाओं के लिए: [आधिकारिक स्कूल वेबसाइट]({SCHOOL_WEBSITE}) · [Amitranet पोर्टल]({AMITRANET_URL}) · [Amitranet Android ऐप]({AMITRANET_APP_URL})। केवल स्कूल द्वारा दिए गए लॉगिन विवरण का उपयोग करें। लिंक बदल गया हो तो रिसेप्शन से पुष्टि करें।",
            ["amitranet", "ऐप", "app", "ऑनलाइन पोर्टल", "वेबसाइट", "लॉगिन", "स्कूल वेबसाइट"],
        ),
        "contact": (
            f"स्कूल रिसेप्शन का नंबर **{RECEPTION_PHONE}** है। उपयुक्त डिवाइस पर साइडबार में **Call reception** लिंक दबाएँ या [आधिकारिक स्कूल वेबसाइट]({SCHOOL_WEBSITE}) पर संपर्क विवरण की पुष्टि करें।",
            ["संपर्क", "फोन", "कॉल", "रिसेप्शन", "नंबर", "फोन नंबर", "पता"],
        ),
    },
}

FALLBACK = {
    "en": f"I couldn't find a verified answer to that question. Please check the latest school circular or contact reception at **{RECEPTION_PHONE}**. This demo is not connected to live school records.",
    "hi": f"मुझे इस प्रश्न का सत्यापित उत्तर नहीं मिला। कृपया नवीनतम स्कूल सर्कुलर देखें या रिसेप्शन **{RECEPTION_PHONE}** पर संपर्क करें। यह डेमो स्कूल के लाइव रिकॉर्ड से जुड़ा नहीं है।",
}

QUICK_PROMPTS = {
    "en": ["Lost ID card", "Fee payment", "Bus route", "Contact a teacher", "Exam datesheet", "School timings", "Homework", "Call reception"],
    "hi": ["आई-कार्ड खो गया", "फीस भुगतान", "बस रूट", "शिक्षक से संपर्क", "परीक्षा डेटशीट", "स्कूल का समय", "होमवर्क", "रिसेप्शन नंबर"],
}


def answer_question(question: str, selected_lang: str) -> str:
    """Return a predefined FAQ answer using simple keyword matching."""
    q = question.casefold().strip()
    # More specific topics are checked before general contact and website topics.
    priority = ("datesheet", "bus", "fees", "id", "leave", "homework", "teacher", "timing", "contact", "website")
    for key in priority:
        answer, keywords = FAQS[selected_lang][key]
        if any(keyword.casefold() in q for keyword in keywords):
            return answer
    return FALLBACK[selected_lang]


if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

st.markdown(
    f'<div class="section-heading">{"💬 Ask the Help Desk" if lang == "en" else "💬 सहायता केंद्र से पूछें"}</div>'
    f'<div class="section-sub">{"Choose a common topic or type your question below." if lang == "en" else "कोई सामान्य विषय चुनें या नीचे अपना सवाल लिखें।"}</div>',
    unsafe_allow_html=True,
)
with st.expander("Quick questions" if lang == "en" else "जल्दी पूछें", expanded=True):
    cols = st.columns(2)
    for i, prompt in enumerate(QUICK_PROMPTS[lang]):
        if cols[i % 2].button(prompt, use_container_width=True, key=f"quick_{lang}_{i}"):
            st.session_state.pending_question = prompt

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=False)

pending = st.session_state.pending_question
question = st.chat_input("Ask a school question..." if lang == "en" else "स्कूल से जुड़ा सवाल पूछें...")
if pending:
    question = pending
    st.session_state.pending_question = None

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    response = answer_question(question, lang)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear chat" if lang == "en" else "चैट साफ़ करें", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
with col2:
    st.link_button("Open school website" if lang == "en" else "स्कूल की वेबसाइट खोलें", SCHOOL_WEBSITE, use_container_width=True)

st.divider()
footer_note = (
    "Student project demo. FAQ answers are predefined, not generated by an AI model. "
    "Exam dates and school procedures may not be current. Confirm important information with the school. "
    "Do not enter passwords, student IDs, payment details, or other sensitive information."
    if lang == "en" else
    "विद्यार्थी प्रोजेक्ट डेमो। जवाब पहले से तय हैं, AI द्वारा तैयार नहीं किए जाते। "
    "परीक्षा की तारीखों और स्कूल की प्रक्रियाओं की पुष्टि स्कूल से करें। "
    "पासवर्ड, विद्यार्थी आईडी, भुगतान विवरण या अन्य निजी जानकारी न डालें।"
)
st.markdown(f'<p class="small-note">{footer_note}</p><div class="footer-line">✦ {"Designed for easier school information access" if lang == "en" else "स्कूल की जानकारी आसानी से पाने के लिए बनाया गया"} ✦</div>', unsafe_allow_html=True)
