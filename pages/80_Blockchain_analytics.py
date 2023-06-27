import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import sidebar

sidebar.run()

st.title("Under construction...")

address_to_analyze = st.text_input("AMB address:", key="address_to_analyze")

if st.button("reset address"):
	address_to_analyze = ""

import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('0x37d6...1247', '0xC62E7...CABB8')
graph.edge('0xC62E...ABB8', '0x37d6...1247')
graph.edge('0xC62E...ABB8', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

tab_overview, tab_graphiz = st.tabs(["Summary", "Visualization"])

if address_to_analyze != "":
	with tab_overview:
		st.header("Summary for: "+address_to_analyze)
		st.text(
			"""
			Source address: 0x3D0F148FE58d592B9CCF5ab492C971D4954B5e7a 

			Total input addresses: 2
			Total input transacions: 2
			Total input value: 1k 

			Total output addresses: 21
			Total output transacions: 588
			Total output value: 418M
			"""
		)


		col1, col2 = st.columns(2)

		with col1:
			st.header("input addresses:")
			st.text(
				"""
				0x37d6bF7e8875137EefA8286e6AEA2cc4bFAF1247 : count: 3 total AMB: 0
				0x55d46039e187b37a0201068dE189ecB63eaE87d2 : count: 34 total AMB: 0
				0x6fA040aD7e94f905a29536Ba786D433638FeD19b : count: 6 total AMB: 0
				0xa5E32D3fB342D9Ed3135fD5cb59a102AC8ED7B85 : count: 11 total AMB: 0
				0xe8592B3a9ee54472A0115262871eF43B5F3e8E53 : count: 10 total AMB: 0
				0x787afc1E7a61af49D7B94F8E774aC566D1B60e99 : count: 18 total AMB: 0
				0xb16398c0698149Ae6EC342614830bC0511b83CAf : count: 25 total AMB: 0
				0x5700F8e0ae3d80964f7718EA625E3a2CB4D2096d : count: 14 total AMB: 0
				0x55feDD7843efc88A9ddd066B2ec2C8618C38fB62 : count: 11 total AMB: 0
				0x40B7d71E70fA6311cB0b300c1Ba6926A2A9000b8 : count: 5 total AMB: 0
				0xc3A192b4A637fcD20c87e91eEB561121C28d4028 : count: 11 total AMB: 0
				"""
			)


		with col2:
			st.header("output addresses:")
			st.text(
				"""
				0xC62E72710F2008487AfB872b999a5cd7AE8CABB8 : count: 169 total AMB: 195M
				0x50dD86C4cfb3Cf68167F18B86458c3af16FceB7C : count: 2 total AMB: 1M
				0xD69f41d00210C1A6259fed82Cb2BcAD58cD5e503 : count: 4 total AMB: 3M
				0xe505872Aa3aeD53e7BE1C629Cc2b9c2D6d49E40C : count: 129 total AMB: 76M
				0x4ca8d89157C287cCc85b3AD9A40732Bb6559F5a9 : count: 37 total AMB: 19M
				0x101D2c4Cff1cd42189cf353E45F451316a402DF0 : count: 10 total AMB: 5M
				0x0E303B82EA04370CE15F6E61438D6AEf1dD9da13 : count: 200 total AMB: 99M
				0xf21e7E46D8dD1b412952a2c5d11AA25a1B538FB4 : count: 1 total AMB: 380k
				0xBcf23582388c34b6507D14c883dEA8e3cFdbD16B : count: 6 total AMB: 2M
				0x53B3e51DB19623235700AcA2FaD974414E744Fe7 : count: 12 total AMB: 5M
				0xA8cF841Caa20531E5f6374A0B7b636cbbE3a2aA6 : count: 2 total AMB: 10k
				0xbB5ABF57eC0beb1A54f0a3289198c5B61C0A2A39 : count: 1 total AMB: 10k
				0xE63528Ab1b16A3DdD0Bd38Ff80d83A0C98e09546 : count: 1 total AMB: 123
				0x291A06673D113f69cF7FCB6C3533f472720751F1 : count: 1 total AMB: 10
				0xAdE2E48Ff326bE97F56205Efbe1f75D9BDbbf06d : count: 1 total AMB: 250k
				0x73e7023fEEF532De9018Eb10635B7e1d6E79ec46 : count: 4 total AMB: 1M
				0x3F64Cb9C9218c3dD3c541c30438799256acf5a19 : count: 1 total AMB: 300k
				0x5a7924772903c5fdcCc06098ca6E3304AB7da990 : count: 1 total AMB: 249k
				0xF286D03BB71196CB3Ff234B1eA48bB08DF8de161 : count: 2 total AMB: 1M
				0xc45560E41A7260d5FEA04D34BAA8E37b08fA1D49 : count: 2 total AMB: 999k
				0xB783f9Ce284570232BEeC491b6426Cca7E9f5227 : count: 2 total AMB: 1M
				"""
			)

	with tab_graphiz:
		st.header("Visualization:")
		st.graphviz_chart(graph)



csv_upload = st.file_uploader(
	"Upload previously saved analytics results", 
	type=["csv"],
	accept_multiple_files=True
)

if csv_upload is not None:
	st.write("file(s) uploaded...")

	#csv_upload.getvalue()

	#df = pd.read_csv(csv_upload)
	#process_data(df)
