import streamlit as st
st.set_page_config(layout='wide')

st.title("Amazon Prime dashboard")
power_bi_link = "https://app.powerbi.com/groups/me/reports/74406191-1f14-4829-b05e-e6a151a3b60f?ctid=685000c7-e97a-46ae-804d-8dae8633009e&pbi_source=linkShare"
html_code = '''<iframe title="amazon_prime" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=74406191-1f14-4829-b05e-e6a151a3b60f&autoAuth=true&ctid=685000c7-e97a-46ae-804d-8dae8633009e" frameborder="0" allowFullScreen="true"></iframe>
'''
# Displaying the HTML in Streamlit
st.components.v1.html(html_code, height = 900, width=1500)