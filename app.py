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

# عرض الجدول
st.subheader("📋 جدول الأداء")
st.dataframe(df.style.highlight_max(axis=0, color='lightgreen'))

# رسم دائري لنسبة تحقيق المبيعات
fig_sales_pie = px.pie(
    df, names="Area", values="Sales Per",
    title="نسبة تحقيق المبيعات",
    color_discrete_sequence=px.colors.sequential.Teal
)
st.plotly_chart(fig_sales_pie, use_container_width=True)

# رسم دائري لنسبة تحقيق العملاء
fig_customer_pie = px.pie(
    df, names="Area", values="Customer Per",
    title="نسبة تحقيق العملاء",
    color_discrete_sequence=px.colors.sequential.Blues
)
st.plotly_chart(fig_customer_pie, use_container_width=True)

# رسم خطي لنسبة المبيعات (شكل نبض)
fig_sales_line = px.line(
    df, x="Area", y="Sales Per",
    title="تطور نسبة المبيعات",
    markers=True, line_shape="spline",
    color_discrete_sequence=["green"]
)
st.plotly_chart(fig_sales_line, use_container_width=True)

# رسم خطي لنسبة العملاء
fig_customer_line = px.line(
    df, x="Area", y="Customer Per",
    title="تطور نسبة العملاء",
    markers=True, line_shape="spline",
    color_discrete_sequence=["blue"]
)
st.plotly_chart(fig_customer_line, use_container_width=True)

# ملخص ختامي
st.markdown("""
### 📌 ملاحظات تحليلية:
- أعلى نسبة مبيعات: `04-QA` بنسبة 50%
- أعلى نسبة عملاء: `02-kh` بنسبة 72%
- أقل أداء مبيعات: `09-ST` بنسبة 22%
- مناطق تحتاج تدخل: `07-MAH`, `09-ST`

""")