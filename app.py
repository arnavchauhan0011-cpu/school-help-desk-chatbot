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
      .block-container {max-width: 850px; padding-top: 1.8rem; padding-bottom: 2.5rem;}
      .hero {padding: 1.25rem 1.35rem; border-radius: 18px; border: 1px solid rgba(128,128,128,.25); margin-bottom: 1rem;}
      .hero h1 {margin: 0 0 .3rem 0; font-size: 1.8rem;}
      .hero p {margin: 0; opacity: .82;}
      .small-note {font-size: .85rem; opacity: .8;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="hero"><h1>🏫 School Help Desk</h1>'
    f'<p>{SCHOOL_NAME} · Student and parent information demo</p></div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("School links / स्कूल लिंक")
    st.link_button("Official school website", SCHOOL_WEBSITE, use_container_width=True)
    st.link_button("Amitranet portal", AMITRANET_URL, use_container_width=True)
    st.link_button("Amitranet Android app", AMITRANET_APP_URL, use_container_width=True)
    st.markdown("### Reception / रिसेप्शन")
    st.write(f"**{RECEPTION_PHONE}**")
    st.link_button("📞 Call reception", f"tel:{RECEPTION_PHONE}", use_container_width=True)
    st.caption("For urgent or account-specific questions, contact the school directly.")
    st.divider()
    st.caption("Demo project · Please verify information against current school circulars.")

language = st.radio("Language / भाषा", ["English", "हिन्दी"], horizontal=True)
lang = "en" if language == "English" else "hi"

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
            "| 26 October 2026 | Sixth Subject* |\n"
            "| 2 November 2026 | Physics |\n"
            "| 13 November 2026 | English |\n"
            "| 18 November 2026 | Chemistry |\n"
            "| 30 November 2026 | Mathematics |\n\n"
            "*This schedule was transcribed from information previously shared for the project; it is **not live-verified**. Check the latest official school circular or teacher message before relying on any date. The sixth subject depends on your subject combination.*",
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
            "| 26 अक्टूबर 2026 | छठा विषय* |\n"
            "| 2 नवंबर 2026 | भौतिक विज्ञान (Physics) |\n"
            "| 13 नवंबर 2026 | अंग्रेज़ी (English) |\n"
            "| 18 नवंबर 2026 | रसायन विज्ञान (Chemistry) |\n"
            "| 30 नवंबर 2026 | गणित (Mathematics) |\n\n"
            "*यह सूची पहले साझा की गई जानकारी से टाइप की गई है; इसे लाइव सत्यापित नहीं किया गया है। किसी तारीख पर भरोसा करने से पहले नवीनतम आधिकारिक सर्कुलर या शिक्षक के संदेश से पुष्टि करें। छठा विषय विद्यार्थी के विषय संयोजन पर निर्भर है।",
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

st.markdown("**Ask a question / अपना सवाल पूछें**")
with st.expander("Quick questions / जल्दी पूछें", expanded=True):
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
    if st.button("Clear chat / चैट साफ़ करें", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
with col2:
    st.link_button("Open school website", SCHOOL_WEBSITE, use_container_width=True)

st.divider()
st.markdown(
    '<p class="small-note">Student project demo. FAQ answers are predefined, not generated by an AI model. '
    'Exam dates and school procedures are not live-verified. Confirm important information with the school. '
    'Do not enter passwords, student IDs, payment details, or other sensitive information.</p>',
    unsafe_allow_html=True,
)
