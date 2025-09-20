import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# تحميل البيانات من ملف CSV
df = pd.read_csv("sales_data.csv")

# تنظيف القيم غير الرقمية
months = [col for col in df.columns if col.startswith("Sales")]
for col in months:
    df[col] = df[col].astype(str).str.replace(",", "").str.replace("%", "")
    df[col] = pd.to_numeric(df[col], errors="coerce")

# إعداد الصفحة
st.set_page_config(page_title="تحليل المبيعات حسب المنطقة والشهر", layout="wide")
st.title("تحليل المبيعات حسب المنطقة والشهر")

# عرض البيانات الأصلية بعد التنظيف
st.subheader("البيانات بعد التنظيف")
st.dataframe(df)

# تحويل البيانات من Wide إلى Long لتحليلها
df_long = df.melt(id_vars=["المنطقة"], var_name="الشهر", value_name="المبيعات")

# رسم بياني خطي لتطور المبيعات لكل منطقة
fig_line = px.line(df_long, x="الشهر", y="المبيعات", color="المنطقة", markers=True, title="تطور المبيعات لكل منطقة")
st.plotly_chart(fig_line, use_container_width=True)

# رسم بياني عمودي لمقارنة المبيعات في كل شهر
fig_bar = px.bar(df_long, x="الشهر", y="المبيعات", color="المنطقة", barmode="group", title="مقارنة المبيعات بين المناطق في كل شهر")
st.plotly_chart(fig_bar, use_container_width=True)

# رسم بياني حراري Heatmap لتوضيح الأداء
pivot = df_long.pivot_table(index="المنطقة", columns="الشهر", values="المبيعات")
fig_heatmap = px.imshow(pivot, text_auto=True, aspect="auto", title="خريطة حرارية لأداء المبيعات")
st.plotly_chart(fig_heatmap, use_container_width=True)

# تحليل أعلى وأقل منطقة في كل شهر
st.subheader("تحليل شهري لأعلى وأقل منطقة")
months_unique = df_long["الشهر"].unique()
for month in months_unique:
    month_data = df_long[df_long["الشهر"] == month].dropna()
    if not month_data.empty:
        top = month_data.loc[month_data["المبيعات"].idxmax()]
        low = month_data.loc[month_data["المبيعات"].idxmin()]
        st.markdown(f"""
        **{month}:**
        - الأعلى مبيعًا: {top['المنطقة']} بمبيعات {int(top['المبيعات']):,}
        - الأقل مبيعًا: {low['المنطقة']} بمبيعات {int(low['المبيعات']):,}
        """)

# تحليل الاتجاه العام لكل منطقة
st.subheader("الاتجاه العام لكل منطقة")
trend = df_long.groupby("المنطقة")["المبيعات"].mean().sort_values(ascending=False)
st.bar_chart(trend)

# تحليل التذبذب لكل منطقة
st.subheader("تحليل التذبذب في الأداء")
volatility = df_long.groupby("المنطقة")["المبيعات"].std().sort_values()
st.markdown("المناطق ذات التذبذب الأقل تعكس استقرارًا في الأداء، بينما الأعلى قد تشير إلى فرص أو تحديات.")
st.bar_chart(volatility)

# جمل تحفيزية بناءً على الأداء
st.subheader("ملاحظات تحفيزية")
for area in df["المنطقة"]:
    area_data = df_long[df_long["المنطقة"] == area]["المبيعات"].dropna()
    avg = area_data.mean()
    std = area_data.std()
    if avg > df_long["المبيعات"].mean():
        st.markdown(f"- {area}: أداء قوي ومتسق، حافظ على الزخم.")
    elif std < df_long["المبيعات"].std():
        st.markdown(f"- {area}: أداء مستقر، فرصة ممتازة للتوسع بثقة.")
    else:
        st.markdown(f"- {area}: التذبذب واضح، راجع الاستراتيجية وركز على نقاط القوة.")
