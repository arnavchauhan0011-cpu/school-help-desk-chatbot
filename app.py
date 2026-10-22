import streamlit as st

st.set_page_config(page_title="School Help Desk", page_icon="🏫", layout="centered")

FAQS = {
    "en": {
        "id": ("Lost your ID card? Please visit the school reception for guidance on getting a replacement.",
               ["id card", "lost id", "identity card"]),
        "fees": ("For fee-related questions, contact the school's Accounts Section. Online fee payment may be available through the Amitranet app; please verify the current process with the school.",
                 ["fee", "fees", "payment", "accounts"]),
        "bus": ("I don't have verified bus-route information. Please contact the school reception or transport office for the correct route details.",
                ["bus", "route", "transport"]),
        "teacher": ("You can contact the teacher through a professional email, call the school to ask about the correct contact process, or visit the school to arrange a meeting.",
                    ["teacher", "meet teacher", "email teacher", "contact teacher"]),
        "datesheet": ("I don't have a verified, complete current-year datesheet loaded in this demo. Please check the latest school circular/planner or confirm with the school before relying on exam dates.",
                      ["datesheet", "date sheet", "exam date", "examination", "planner", "exam"]),
        "timing": ("Please check the latest school circular or contact reception for confirmed school timings and holiday information.",
                   ["timing", "school time", "holiday", "opening time"]),
        "app": ("The Amitranet app is available on Google Play: https://play.google.com/store/apps/details?id=com.amizone.amitranet",
                ["amitranet", "school app", "app"]),
    },
    "hi": {
        "id": ("आई-कार्ड खो गया है? नया आई-कार्ड बनवाने की प्रक्रिया जानने के लिए स्कूल के रिसेप्शन पर संपर्क करें।",
               ["आई कार्ड", "आई-कार्ड", "id card", "पहचान पत्र"]),
        "fees": ("फीस से संबंधित जानकारी के लिए स्कूल के अकाउंट्स सेक्शन से संपर्क करें। Amitranet ऐप से ऑनलाइन फीस भुगतान की सुविधा हो सकती है; वर्तमान प्रक्रिया स्कूल से पुष्टि कर लें।",
                 ["फीस", "शुल्क", "पेमेंट", "अकाउंट्स", "fees"]),
        "bus": ("मेरे पास बस रूट की सत्यापित जानकारी उपलब्ध नहीं है। सही जानकारी के लिए स्कूल रिसेप्शन या ट्रांसपोर्ट कार्यालय से संपर्क करें।",
                ["बस", "रूट", "परिवहन", "bus", "route"]),
        "teacher": ("आप शिक्षक को औपचारिक ईमेल भेज सकते हैं, सही संपर्क प्रक्रिया जानने के लिए स्कूल में फोन कर सकते हैं, या मुलाकात तय करने के लिए स्कूल जा सकते हैं।",
                    ["शिक्षक", "टीचर", "मिलना", "ईमेल", "teacher"]),
        "datesheet": ("इस डेमो में वर्तमान वर्ष की पूरी और सत्यापित डेटशीट उपलब्ध नहीं है। परीक्षा की तारीखों पर भरोसा करने से पहले स्कूल का नवीनतम सर्कुलर/प्लानर देखें या स्कूल से पुष्टि करें।",
                      ["डेटशीट", "तारीख", "परीक्षा", "प्लानर", "datesheet", "exam"]),
        "timing": ("स्कूल के समय और छुट्टियों की पुष्टि के लिए नवीनतम सर्कुलर देखें या रिसेप्शन से संपर्क करें।",
                   ["समय", "टाइमिंग", "छुट्टी", "स्कूल का समय"]),
        "app": ("Amitranet ऐप Google Play पर उपलब्ध है: https://play.google.com/store/apps/details?id=com.amizone.amitranet",
                ["amitranet", "ऐप", "app"]),
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
