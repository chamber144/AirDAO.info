import streamlit as st
from datetime import date
import sidebar

sidebar.run()

st.title("CSV Export")

address_csv_export = st.text_input("AMB address:", key="address_csv_export")

if address_csv_export != "":
	st.header(address_csv_export)

date_reservation = st.date_input(
	"Date range:",
	value=(date.today(),date.today()),
	min_value=date(2018,1,1),
	max_value=date.today(),
)

with st.expander("specify start and end time", expanded=False):
#if st.checkbox("specify start and end time"):
	starting_time = st.time_input("start")
	ending_time = st.time_input("end")

with st.expander("Timezone settings", expanded=False):
	st.write("under construction")

csv_formats = ('Cointracking', 'Manual selection')
csv_export_type = st.selectbox('Select CSV format', csv_formats, help="Chose between pre-formatted CSV files or manually choose the details you want to export.")

if csv_export_type is csv_formats[0]:
	st.header("Cointracking:")
	st.checkbox("Sum up daily transactions")
	export_assets = st.multiselect("Assets", ["AMB", "wAMB", "wETH", "BUSD", "USDC", "BOND", "others"], ["AMB"])

if csv_export_type is csv_formats[1]:
	st.header("Manual selection:")
	export_assets = st.multiselect("Assets", ["AMB", "wAMB", "wETH", "BUSD", "USDC", "BOND", "others"], ["AMB"])
	export_methods = st.multiselect("Methods:", ["Transactions", "Contract calls", "undefined events"], ["Transactions"])

st.download_button("Export CSV file now", "CSV download currently under construction...", key="export_csv_button")