import streamlit as st
from datetime import datetime, date
import numpy as np

st.title("Insurance Pro Rata Calculator")

col1, col2, col3 = st.columns(3)
premium_startdate = col1.date_input("Premium start date", datetime.today().date())


sd = datetime.today().date()
ed = date(sd.year + 1, sd.month, sd.day)

premium_enddate = col2.date_input("Premium end date", ed)

premium_rate = col3.number_input("Premium rate (dollars)", 0.0)

col1b, col2b = st.columns(2)
pr_sd = date(sd.year, sd.month + 1, sd.day)
prorata_startdate = col1b.date_input("Pro Rata start date", pr_sd)


remaining_installments = col2b.number_input("Remaining installments:", 1)

st.markdown("------")
st.markdown("## Summary:")

st.write("The premium starts on:", premium_startdate)
st.write("The premium ends on:", premium_enddate)
st.write("The Pro Rata starts on:", prorata_startdate)


daily_rate = premium_rate / (premium_enddate - premium_startdate).days
st.write("The premium daily rate is:", np.round(daily_rate, 2))
prorata_dt = premium_enddate - prorata_startdate

prorata_rate = daily_rate * prorata_dt.days
st.write("The Pro Rata term rate is:", np.round(prorata_rate, 2))

st.write("Remaining policy installments:", remaining_installments)

installment_increase = np.round(prorata_rate / remaining_installments, 2)
ii_str = "##### Estimated Pro Rata increase: " + str(installment_increase)
st.markdown(ii_str)
