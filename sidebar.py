import streamlit as st


def run():
	st.set_page_config(layout='wide', initial_sidebar_state='expanded')
	#bottom_placeholder = st.sidebar.empty()


	with open('style.css') as f:
	    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

	#st.sidebar.header("Sidebar Content 1")
	#st.sidebar.subheader("Sidebar Content 2")

	#bottom_placeholder.text("Bottom Content")

	st.sidebar.markdown(
		"""
		<a href="">:us:</a> <a href="">🇹🇷</a> <a href="">:cn:</a> <a href="">:jp:</a>
		""",
		unsafe_allow_html=True
	)




def testrun():
	st.sidebar.header('AirDAO.info')

	st.sidebar.markdown(
		"""
		- Voting
		  - past votes
		  - running votes
		- CSV export
		- Address analysis
		- Products
		  - bridge
		    - fees (monthly)
		  - firepot
		"""
	)

	st.sidebar.subheader('Heat map parameter')
	time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

	st.sidebar.subheader('Donut chart parameter')
	donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

	st.sidebar.subheader('Line chart parameters')
	plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
	plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

	st.sidebar.markdown('''
	---
	Created with ❤️ by [Data Professor](https://youtube.com/dataprofessor/).
	''')