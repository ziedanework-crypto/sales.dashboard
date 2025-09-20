import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد البيانات
data = {
    "Area": ["01-Sh", "02-kh", "03-QL", "04-QA", "05-BE", "06-TKH", "07-MAH", "08-A+", "09-ST"],
    "Sales Target": [2850000, 3200000, 2800000, 3650000, 2800000, 1900000, 300000, 1000000, 1500000],
    "Sales": [1239477, 1085150, 1033987, 1817742, 1192597, 847687, 68884, 356570, 333634],
    "Sales Per": [43, 34, 37, 50, 43, 45, 23, 36, 22],
    "Customer Target": [220, 220, 170, 180, 140, 190, 20, 5, 5],
    "Customer": [134, 158, 100, 125, 72, 98, 11, 3, 2],
    "Customer Per": [61, 72, 59, 69, 51, 52, 55, 60, 40]
}

df = pd.DataFrame(data)

# إعداد الصفحة
st.set_page_config(page_title="Dashboard الأداء", layout="wide")
st.title("📊 لوحة متابعة الأداء حسب المنطقة")

# جمل تحفيزية
st.markdown("""
<div style='background-color:#ffe6e6; padding:10px; border-radius:10px'>
<b>💡 تحفيز اليوم:</b><br>
- كل رقم هو خطوة نحو النجاح.<br>
- لو المؤشرات ضعيفة، إحنا هنا نرفعها.<br>
- البيانات مش بس أرقام... دي فرص بتتنفس.<br>
- خلّي التحليل يتكلم، وإنت خليك القائد.
</div>
""", unsafe_allow_html=True)

# عرض الجدول
st.subheader("📋 جدول الأداء")
st.dataframe(df.style.highlight_max(axis=0, color='#ffcccc'))

# رسم دائري لنسبة تحقيق المبيعات
fig_sales_pie = px.pie(
    df, names="Area", values="Sales Per",
    title="🎯 نسبة تحقيق المبيعات",
    color_discrete_sequence=px.colors.sequential.Reds
)
st.plotly_chart(fig_sales_pie, use_container_width=True)

# رسم دائري لنسبة تحقيق العملاء
fig_customer_pie = px.pie(
    df, names="Area", values="Customer Per",
    title="👥 نسبة تحقيق العملاء",
    color_discrete_sequence=px.colors.sequential.Purples
)
st.plotly_chart(fig_customer_pie, use_container_width=True)

# رسم خطي لنسبة المبيعات
fig_sales_line = px.line(
    df, x="Area", y="Sales Per",
    title="📈 تطور نسبة المبيعات",
    markers=True, line_shape="spline",
    color_discrete_sequence=["#ff4d4d"]
)
st.plotly_chart(fig_sales_line, use_container_width=True)

# رسم خطي لنسبة العملاء
fig_customer_line = px.line(
    df, x="Area", y="Customer Per",
    title="📈 تطور نسبة العملاء",
    markers=True, line_shape="spline",
    color_discrete_sequence=["#8000ff"]
)
st.plotly_chart(fig_customer_line, use_container_width=True)

# ملاحظات تحليلية موسعة
st.markdown("""
### 📌 ملاحظات تحليلية مفصلة:

- ✅ <b>04-QA</b> الأعلى في تحقيق المبيعات بنسبة 50%، أداء ثابت ويستحق الدعم.
- ✅ <b>02-kh</b> الأعلى في تحقيق العملاء بنسبة 72%، مؤشر قوي على التفاعل الممتاز.
- ⚠️ <b>09-ST</b> الأقل في المبيعات والعملاء، تحتاج تدخل عاجل وخطة تنشيط.
- ⚠️ <b>07-MAH</b> نسبة مبيعات 23% فقط، رغم عدد العملاء المقبول نسبيًا.
- 🔄 <b>06-TKH</b> أداء متوسط في المبيعات والعملاء، ممكن يتحسن بفلاتر موجهة.
- 🔼 <b>03-QL</b> نسبة العملاء 59% رغم ضعف المبيعات، فيه فرصة لتحسين العرض.
- 🔥 <b>08-A+</b> نسبة العملاء 60% رغم أن الهدف صغير، أداء ذكي في نطاق محدود.
- 📉 <b>05-BE</b> نسبة العملاء 51%، محتاجة متابعة وتحسين تجربة العميل.
- 📊 <b>01-Sh</b> أداء متوازن، بس محتاج دفعة في العملاء لتحقيق الهدف الكامل.

""", unsafe_allow_html=True)

# لمسة ختامية
st.markdown("""
<div style='background-color:#e6f7ff; padding:10px; border-radius:10px'>
<b>🎯 خلاصة لانا:</b><br>
- في مناطق بتتألق، ومناطق بتطلب تدخل.<br>
- التحليل مش بس أرقام، ده رؤية.<br>
- يلا نشتغل على اللي محتاج دفعة، ونحتفل باللي متفوق.<br>
</div>
""", unsafe_allow_html=True)