import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# الاتصال بجوجل شيت
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("gcreds.json", scope)
client = gspread.authorize(creds)

# قراءة البيانات من الشيت
sheet = client.open("اسم الشيت").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# إعداد الصفحة
st.set_page_config(page_title="تحليل المبيعات حسب المنطقة والشهر", layout="wide")
st.title("تحليل المبيعات حسب المنطقة والشهر")

# عرض الجدول الأصلي
st.subheader("البيانات الأصلية")
st.dataframe(df)

# تحويل البيانات من Wide إلى Long لتحليلها
df_long = df.melt(id_vars=["منطقة"], var_name="الشهر", value_name="المبيعات")

# رسم بياني خطي لتطور المبيعات لكل منطقة
fig_line = px.line(df_long, x="الشهر", y="المبيعات", color="منطقة", markers=True, title="تطور المبيعات لكل منطقة")
st.plotly_chart(fig_line, use_container_width=True)

# رسم بياني عمودي لمقارنة المبيعات في كل شهر
fig_bar = px.bar(df_long, x="الشهر", y="المبيعات", color="منطقة", barmode="group", title="مقارنة المبيعات بين المناطق في كل شهر")
st.plotly_chart(fig_bar, use_container_width=True)

# رسم بياني حراري Heatmap لتوضيح الأداء
pivot = df_long.pivot_table(index="منطقة", columns="الشهر", values="المبيعات")
fig_heatmap = px.imshow(pivot, text_auto=True, aspect="auto", title="خريطة حرارية لأداء المبيعات")
st.plotly_chart(fig_heatmap, use_container_width=True)

# تحليل أعلى وأقل منطقة في كل شهر
st.subheader("تحليل شهري لأعلى وأقل منطقة")
months = df_long["الشهر"].unique()
for month in months:
    month_data = df_long[df_long["الشهر"] == month]
    top = month_data.loc[month_data["المبيعات"].idxmax()]
    low = month_data.loc[month_data["المبيعات"].idxmin()]
    st.markdown(f"""
    **{month}:**
    - الأعلى مبيعًا: {top['منطقة']} بمبيعات {top['المبيعات']:,}
    - الأقل مبيعًا: {low['منطقة']} بمبيعات {low['المبيعات']:,}
    """)

# تحليل الاتجاه العام لكل منطقة
st.subheader("تحليل الاتجاه العام لكل منطقة")
trend = df_long.groupby("منطقة")["المبيعات"].mean().sort_values(ascending=False)
st.bar_chart(trend)

st.markdown("""
### استنتاجات عامة:
- بعض المناطق بتحقق أداء ثابت وعالي عبر الشهور، وده مؤشر على استقرار السوق فيها.
- مناطق تانية فيها تذبذب أو ضعف في بعض الشهور، وده محتاج تدخل وتحسين.
- التحليل ده بيساعدك تحدد الأولويات وتوجّه الموارد بشكل ذكي.
""")