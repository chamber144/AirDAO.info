import streamlit as st
import pandas as pd
import numpy as np
import sidebar

sidebar.run()

# TODO: two new objects needed: proposal, all_proposals

# get a list of all snapshot proposals
proposal_list = ('AirDAO Tokenomics Proposal', 'Ecosystem Fund: Community Multisig', 'Transition to Community Governance: AirDAO Council Proposal', 'Community Vote', 'Operations Vote')

# drop down menu with a list of all proposals
selected_proposal = st.selectbox('Select proposal', proposal_list, help="Hit enter to send the address...")

# Proposal text
st.header(selected_proposal)

# graphic with bars: vote winners
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["In favour", "Against the Proposal"])

st.bar_chart(chart_data)

# pie chart with vote distribution by address
  # option to condensate addresses that are connected through unique addresses (i.E. cex deposit address)

