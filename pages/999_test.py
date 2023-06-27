import streamlit as st
from datetime import date
import sidebar

sidebar.run()

clicked = st.button("Click me!", key="clicked1", help="Help me!", disabled=True)

st.write(f"Button status: {clicked}")

if st.button("Run!", key="button1"):
	st.header("Running...")

checked = st.checkbox("my checkbox", key="checkbox1")
checked2 = st.checkbox("my checkbox", key="checkbox2")
checked3 = st.checkbox("my checkbox", key="checkbox3")
checked4 = st.checkbox("my checkbox", key="checkbox4")
st.write(f"Check status: {checked}")

st.number_input(
	"How many apples?",
	min_value=0,
	max_value=100,
	value=10,
	step=10,
)

date_reservation = st.date_input(
	"Reservation date",
	value=date.today(),
	min_value=date(2018,1,1),
	max_value=date.today(),
)




st.title("AirDAO.info", anchor="title")
st.write("Welcome to AirDAO.info, a transparency initiative of the newly elected council.")
st.write("")
st.write("")
st.header("header", anchor="chap-1")
st.write(
	"Helllooo world!!!\n"
	"this is a test..."
)

st.subheader("subheader")

st.markdown(
	"""
	# My Streamlit App :tada:

	**hello** _there_ `how are you`?

	> quickly build web apps

	- this
	- is
	- markdown :smile:

	---

	```python
	name='fanilo'
	print("hello world")
	"""
)


st.markdown(
	"""
	<span style='color:blue;'>
		Streamlit
	</span> is **easy**
	""",
	unsafe_allow_html=True
)

st.caption("caption")

text="this is a \n new line of this \n new text."
st.text(text)