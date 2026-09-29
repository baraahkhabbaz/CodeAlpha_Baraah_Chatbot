import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(page_title="Baraah Chatbot", page_icon="🤖")

st.title("🤖 Baraah Chatbot")
st.write("مرحباً بك! أنا روبوت إجابة الأسئلة الشائعة الخاصة بالتدريب. اسألني أي سؤال!")

# قاعدة بيانات الأسئلة والأجوبة الشائعة
faqs = {
    "ما هو هذا التدريب؟": "هذا تدريب عملي مقدم من CodeAlpha لبناء مشاريع ذكاء اصطناعي وتطبيقات ويب.",
    "ما هي اللغات المستخدمة؟": "نستخدم لغة Python بشكل أساسي مع مكتبات مثل Streamlit لبناء الواجهات.",
    "كيف أقوم بتسليم المهام؟": "يتم تسليم المهام عن طريق رفع الكود على GitHub ونشر فيديو شرح على LinkedIn ثم ملء النموذج.",
    "مرحبا بك! اسألني أي سؤال!": "أهلاً بك! كيف يمكنني مساعدتك اليوم؟",
    "هل أستطيع الحصول على شهادة؟": "نعم، عند إتمام جميع المهام المطلوبة وتسليمها في الوقت المحدد.",
    "ما هي مدة التدريب؟": "مدة التدريب عادة ما تكون شهر واحد مقسمة على عدة مهام عملية."
}

# حفظ سجل المحادثة في جلسة العمل
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if user_input := st.chat_input(" اكتب سؤالك هنا..."):
    # عرض سؤال المستخدم في الشات
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # البحث عن أفضل إجابة مطابقة
    bot_response = "عذراً، لا أملك إجابة على هذا السؤال حالياً. يمكنك تجربة سؤال آخر!"

    for question, answer in faqs.items():
        # فحص وجود كلمات مفتاحية من السؤال
        if any(word in user_input.lower() for word in question.lower().split() if len(word) > 2):
            bot_response = answer
            break

    # عرض إجابة البوت
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})