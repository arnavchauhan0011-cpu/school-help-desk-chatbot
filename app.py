import streamlit as st

st.set_page_config(page_title="School Help Desk", page_icon="🏫", layout="centered")

FAQS = {
    "en": {
        "id": ("Lost your ID card? Please visit the school reception for guidance on getting a replacement.",
               ["id card", "lost id", "identity card"]),
        "fees": ("For fee-related questions, contact the school's Accounts Section. Online fee payment may be available through the Amitranet app; please verify the current process with the school.",
                 ["fee", "fees", "payment", "accounts"]),
        "bus": ("For the latest bus route and stop information, please check the official Amitranet app/online portal using your school-provided login. If you cannot find your route there, contact the school reception at 011-22717261 for confirmation. Online portal: http://aismv.amizone.net/Parentmvg/ | Android app: https://play.google.com/store/apps/details?id=com.amizone.amitranet",
                ["bus", "route", "transport", "stop"]),
        "teacher": ("You can contact the teacher through a professional email, call the school to ask about the correct contact process, or visit the school to arrange a meeting.",
                    ["teacher", "meet teacher", "email teacher", "contact teacher"]),
        "datesheet": ("Latest Class XII Pre-Board datesheet (based on the dates you provided; please confirm any changes with school):\n\n• 26 October 2026: Sixth Subject\n• 2 November 2026: Physics\n• 13 November 2026: English\n• 18 November 2026: Chemistry\n• 30 November 2026: Mathematics\n\n“Sixth Subject” depends on your subject combination. This is the latest pre-board schedule you provided, not an independently verified official circular. Please check Amitranet or your school’s latest notice for updates.",
                      ["datesheet", "date sheet", "exam date", "examination", "planner", "exam", "unit test", "preboard", "pre-board", "pre board", "paper date"]),
        "timing": ("Please check the latest school circular or contact reception for confirmed school timings and holiday information.",
                   ["timing", "school time", "holiday", "opening time"]),
        "app": ("Amitranet access options:\n\n• Online parent portal for Amity International School, Mayur Vihar: http://aismv.amizone.net/Parentmvg/\n• Android app on Google Play: https://play.google.com/store/apps/details?id=com.amizone.amitranet\n\nUse only your own school-provided login details. If the portal link does not open, confirm the current link with the school.",
                ["amitranet", "school app", "app", "online portal", "website login", "browser"]),
    },
    "hi": {
        "id": ("आई-कार्ड खो गया है? नया आई-कार्ड बनवाने की प्रक्रिया जानने के लिए स्कूल के रिसेप्शन पर संपर्क करें।",
               ["आई कार्ड", "आई-कार्ड", "id card", "पहचान पत्र"]),
        "fees": ("फीस से संबंधित जानकारी के लिए स्कूल के अकाउंट्स सेक्शन से संपर्क करें। Amitranet ऐप से ऑनलाइन फीस भुगतान की सुविधा हो सकती है; वर्तमान प्रक्रिया स्कूल से पुष्टि कर लें।",
                 ["फीस", "शुल्क", "पेमेंट", "अकाउंट्स", "fees"]),
        "bus": ("बस रूट और स्टॉप की नवीनतम जानकारी के लिए अपने स्कूल द्वारा दिए गए लॉगिन से आधिकारिक Amitranet ऐप/ऑनलाइन पोर्टल देखें। यदि वहाँ रूट न मिले, तो पुष्टि के लिए स्कूल रिसेप्शन 011-22717261 पर संपर्क करें। ऑनलाइन पोर्टल: http://aismv.amizone.net/Parentmvg/ | Android ऐप: https://play.google.com/store/apps/details?id=com.amizone.amitranet",
                ["बस", "रूट", "परिवहन", "bus", "route", "स्टॉप"]),
        "teacher": ("आप शिक्षक को औपचारिक ईमेल भेज सकते हैं, सही संपर्क प्रक्रिया जानने के लिए स्कूल में फोन कर सकते हैं, या मुलाकात तय करने के लिए स्कूल जा सकते हैं।",
                    ["शिक्षक", "टीचर", "मिलना", "ईमेल", "teacher"]),
        "datesheet": ("कक्षा XII की नवीनतम Pre-Board डेटशीट (आपके दिए गए विवरण के आधार पर; किसी बदलाव की पुष्टि स्कूल से करें):\n\n• 26 अक्टूबर 2026: छठा विषय (Sixth Subject)\n• 2 नवंबर 2026: Physics\n• 13 नवंबर 2026: English\n• 18 नवंबर 2026: Chemistry\n• 30 नवंबर 2026: Mathematics\n\n“छठा विषय” आपके विषय संयोजन पर निर्भर करता है। यह आपके द्वारा दी गई नवीनतम प्री-बोर्ड डेटशीट है, आधिकारिक सर्कुलर से स्वतंत्र रूप से सत्यापित नहीं है। अपडेट के लिए Amitranet या स्कूल का नवीनतम नोटिस देखें।",
                      ["डेटशीट", "तारीख", "परीक्षा", "प्लानर", "datesheet", "exam", "unit test", "preboard", "pre-board", "प्री-बोर्ड", "प्री बोर्ड"]),
        "timing": ("स्कूल के समय और छुट्टियों की पुष्टि के लिए नवीनतम सर्कुलर देखें या रिसेप्शन से संपर्क करें।",
                   ["समय", "टाइमिंग", "छुट्टी", "स्कूल का समय"]),
        "app": ("Amitranet के विकल्प:\n\n• Amity International School, Mayur Vihar का ऑनलाइन parent portal: http://aismv.amizone.net/Parentmvg/\n• Android ऐप Google Play पर: https://play.google.com/store/apps/details?id=com.amizone.amitranet\n\nकेवल स्कूल द्वारा दिए गए अपने लॉगिन विवरण का उपयोग करें। लिंक न खुले तो स्कूल से वर्तमान लिंक की पुष्टि करें।",
                ["amitranet", "ऐप", "app", "ऑनलाइन पोर्टल", "वेबसाइट", "लॉगिन"]),
    }
}

FALLBACK = {
    "en": "I couldn't find a verified answer to that question. Please contact the school reception or the relevant school office for accurate information.",
    "hi": "मुझे इस प्रश्न का सत्यापित उत्तर नहीं मिला। सही जानकारी के लिए स्कूल रिसेप्शन या संबंधित कार्यालय से संपर्क करें।"
}

st.title("🏫 School Help Desk Chatbot")
st.caption("Amity International School, Mayur Vihar • Student/parent information demo")

language = st.radio("Language / भाषा", ["English", "हिन्दी"], horizontal=True)
lang = "en" if language == "English" else "hi"

with st.expander("Quick questions / जल्दी पूछें", expanded=True):
    prompts = {
        "en": ["Lost ID card", "Fee payment", "Bus route", "Contact a teacher", "Exam datesheet", "School app"],
        "hi": ["आई-कार्ड खो गया", "फीस भुगतान", "बस रूट", "शिक्षक से संपर्क", "परीक्षा डेटशीट", "स्कूल ऐप"]
    }
    cols = st.columns(2)
    for i, prompt in enumerate(prompts[lang]):
        if cols[i % 2].button(prompt, use_container_width=True):
            st.session_state["pending_question"] = prompt

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def answer_question(question, lang):
    q = question.lower()
    for _, (answer, keywords) in FAQS[lang].items():
        if any(k.lower() in q for k in keywords):
            return answer
    return FALLBACK[lang]

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
st.caption("Demo only. Confirm dates, fees, transport, timings and official procedures with the school. Do not enter private student information.")
