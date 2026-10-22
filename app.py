import streamlit as st

st.set_page_config(page_title="School Help Desk", page_icon="🏫", layout="centered")

AMITRANET_URL = "https://amitranet.amizone.net"

FAQS = {
    "en": {
        "id": (
            "If your school ID card has been lost, please contact the school reception for guidance on the replacement procedure.",
            ["id card", "lost id", "identity card"],
        ),
        "fees": (
            "For fee-related enquiries, please contact the school's Accounts Section. Please confirm the current payment procedure with the school.",
            ["fee", "fees", "payment", "accounts"],
        ),
        "bus": (
            f"For the latest bus route and stop information, please sign in to the official Amitranet website using your school-provided credentials: [{AMITRANET_URL}]({AMITRANET_URL}). If the required information is unavailable, please contact the school reception at **011-22717261** for assistance.",
            ["bus", "route", "transport", "stop", "school bus"],
        ),
        "teacher": (
            "For teacher-related enquiries, please contact the school to confirm the appropriate communication procedure or to arrange an appointment.",
            ["teacher", "meet teacher", "email teacher", "contact teacher"],
        ),
        "datesheet": (
            "**Class XII Pre-Board Examination Datesheet**\n\n"
            "The following schedule is based on the latest dates you provided. Please check the school's official notices for any revisions.\n\n"
            "| Date | Subject |\n|---|---|\n"
            "| 26 October 2026 | Sixth Subject |\n"
            "| 2 November 2026 | Physics |\n"
            "| 13 November 2026 | English |\n"
            "| 18 November 2026 | Chemistry |\n"
            "| 30 November 2026 | Mathematics |\n\n"
            "*Note: The sixth subject depends on the student's subject combination.*",
            ["datesheet", "date sheet", "exam date", "examination", "planner", "exam", "unit test", "preboard", "pre-board", "pre board", "paper date"],
        ),
        "timing": (
            "For confirmed school timings and holiday information, please refer to the latest school circular or contact the school reception.",
            ["timing", "school time", "holiday", "opening time"],
        ),
        "website": (
            f"The official Amitranet website for school-related services is available at [{AMITRANET_URL}]({AMITRANET_URL}). Please sign in using your school-provided credentials. For login assistance, contact the school.",
            ["amitranet", "school app", "app", "online portal", "website", "website login", "browser", "school website"],
        ),
    },
    "hi": {
        "id": (
            "यदि आपका स्कूल आई-कार्ड खो गया है, तो नया आई-कार्ड प्राप्त करने की प्रक्रिया जानने के लिए कृपया स्कूल रिसेप्शन से संपर्क करें।",
            ["आई कार्ड", "आई-कार्ड", "id card", "पहचान पत्र"],
        ),
        "fees": (
            "फीस से संबंधित जानकारी के लिए कृपया स्कूल के अकाउंट्स सेक्शन से संपर्क करें। भुगतान की वर्तमान प्रक्रिया की पुष्टि स्कूल से कर लें।",
            ["फीस", "शुल्क", "पेमेंट", "अकाउंट्स", "fees"],
        ),
        "bus": (
            f"बस रूट और स्टॉप की नवीनतम जानकारी के लिए कृपया स्कूल द्वारा दिए गए लॉगिन विवरण से आधिकारिक Amitranet वेबसाइट पर लॉगिन करें: [{AMITRANET_URL}]({AMITRANET_URL})। यदि आवश्यक जानकारी उपलब्ध न हो, तो सहायता के लिए स्कूल रिसेप्शन **011-22717261** पर संपर्क करें।",
            ["बस", "रूट", "परिवहन", "bus", "route", "स्टॉप", "स्कूल बस"],
        ),
        "teacher": (
            "शिक्षक से संबंधित जानकारी के लिए कृपया स्कूल से संपर्क करके उचित संपर्क प्रक्रिया की पुष्टि करें या मुलाकात का समय निर्धारित करें।",
            ["शिक्षक", "टीचर", "मिलना", "ईमेल", "teacher"],
        ),
        "datesheet": (
            "**कक्षा XII की प्री-बोर्ड परीक्षा की डेटशीट**\n\n"
            "नीचे दिया गया कार्यक्रम आपके द्वारा साझा की गई नवीनतम तिथियों पर आधारित है। किसी भी बदलाव के लिए कृपया स्कूल के आधिकारिक नोटिस देखें।\n\n"
            "| तारीख | विषय |\n|---|---|\n"
            "| 26 अक्टूबर 2026 | छठा विषय (Sixth Subject) |\n"
            "| 2 नवंबर 2026 | भौतिक विज्ञान (Physics) |\n"
            "| 13 नवंबर 2026 | अंग्रेज़ी (English) |\n"
            "| 18 नवंबर 2026 | रसायन विज्ञान (Chemistry) |\n"
            "| 30 नवंबर 2026 | गणित (Mathematics) |\n\n"
            "*नोट: छठा विषय विद्यार्थी के विषय संयोजन पर निर्भर करता है।*",
            ["डेटशीट", "तारीख", "परीक्षा", "प्लानर", "datesheet", "exam", "unit test", "preboard", "pre-board", "प्री-बोर्ड", "प्री बोर्ड"],
        ),
        "timing": (
            "स्कूल के समय और छुट्टियों की पुष्टि के लिए कृपया नवीनतम स्कूल सर्कुलर देखें या स्कूल रिसेप्शन से संपर्क करें।",
            ["समय", "टाइमिंग", "छुट्टी", "स्कूल का समय"],
        ),
        "website": (
            f"स्कूल से संबंधित सेवाओं के लिए आधिकारिक Amitranet वेबसाइट यहाँ उपलब्ध है: [{AMITRANET_URL}]({AMITRANET_URL})। कृपया स्कूल द्वारा दिए गए लॉगिन विवरण का उपयोग करें। लॉगिन में सहायता के लिए स्कूल से संपर्क करें।",
            ["amitranet", "ऐप", "app", "ऑनलाइन पोर्टल", "वेबसाइट", "लॉगिन", "स्कूल वेबसाइट"],
        ),
    },
}

FALLBACK = {
    "en": "I could not find a verified answer to that question. Please contact the school reception or the relevant school office for accurate information.",
    "hi": "मुझे इस प्रश्न का सत्यापित उत्तर नहीं मिला। सही जानकारी के लिए कृपया स्कूल रिसेप्शन या संबंधित कार्यालय से संपर्क करें।",
}

st.title("🏫 School Help Desk Chatbot")
st.caption("Amity International School, Mayur Vihar • Student/parent information demo")

language = st.radio("Language / भाषा", ["English", "हिन्दी"], horizontal=True)
lang = "en" if language == "English" else "hi"

with st.expander("Quick questions / जल्दी पूछें", expanded=True):
    prompts = {
        "en": ["Lost ID card", "Fee payment", "Bus route", "Contact a teacher", "Exam datesheet", "School website"],
        "hi": ["आई-कार्ड खो गया", "फीस भुगतान", "बस रूट", "शिक्षक से संपर्क", "परीक्षा डेटशीट", "स्कूल की वेबसाइट"],
    }
    cols = st.columns(2)
    for i, prompt in enumerate(prompts[lang]):
        if cols[i % 2].button(prompt, use_container_width=True):
            st.session_state["pending_question"] = prompt

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=False)


def answer_question(question, selected_lang):
    q = question.lower()
    # Prefer more specific categories before broader website/app terms.
    for key in ("bus", "datesheet", "id", "fees", "teacher", "timing", "website"):
        answer, keywords = FAQS[selected_lang][key]
        if any(keyword.lower() in q for keyword in keywords):
            return answer
    return FALLBACK[selected_lang]


pending = st.session_state.pop("pending_question", None)
question = st.chat_input("Ask a school question..." if lang == "en" else "स्कूल से जुड़ा सवाल पूछें...")
if pending:
    question = pending

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    answer = answer_question(question, lang)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

st.divider()
st.caption("Demo only. Confirm examination dates, fees, transport, timings and official procedures with the school. Do not enter private student information.")
