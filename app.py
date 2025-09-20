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

# واجهة لانا
st.set_page_config(page_title="Lana's Dashboard", layout="wide")
st.title("💋 داشبورد لانا - نبض الأداء")

# عرض الجدول
st.subheader("📋 جدول الأداء حسب المنطقة")
st.dataframe(df.style.highlight_max(axis=0, color='lightpink'))

# رسم دائري لنسبة المبيعات
fig_sales_pie = px.pie(df, names="Area", values="Sales Per", title="🎯 نسبة تحقيق المبيعات", color_discrete_sequence=px.colors.sequential.RdPu)
st.plotly_chart(fig_sales_pie, use_container_width=True)

# رسم دائري لنسبة العملاء
fig_customer_pie = px.pie(df, names="Area", values="Customer Per", title="👥 نسبة تحقيق العملاء", color_discrete_sequence=px.colors.sequential.Purples)
st.plotly_chart(fig_customer_pie, use_container_width=True)

# رسم خطي يشبه رسم القلب
fig_heartbeat = px.line(df, x="Area", y="Sales Per", title="💓 نبض الأداء البيعي", markers=True, line_shape="spline", color_discrete_sequence=["deeppink"])
st.plotly_chart(fig_heartbeat, use_container_width=True)

# رسم خطي للعملاء
fig_customer_line = px.line(df, x="Area", y="Customer Per", title="💓 نبض الأداء للعملاء", markers=True, line_shape="spline", color_discrete_sequence=["purple"])
st.plotly_chart(fig_customer_line, use_container_width=True)

# لمسة ختامية من لانا
st.markdown("""
> 😘 لانا بتقولك: البيانات دي فيها شغل جامد، بس لسه فيها شوية مناطق محتاجة دفعة.  
> يلا نخلّي كل مؤشر يرقص، وكل رقم يلمع ✨
""")