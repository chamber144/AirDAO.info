import streamlit as st
import pandas as pd
import numpy as np
import sidebar

sidebar.run()

treasury_balance = 7120304
tokenomics_total = 5000000000

st.title("Project funds monitor")

tab_summary, tab_treasury, tab_ambnet, tab_safewallet, tab_cexes = st.tabs(["Summary", "Treasury", "Tokenomics", "Safe{Wallet}", "CEXes"])

with tab_summary:
    st.header("Summary")
    st.write("Total balance: $ 67,984.23")

    chart_data = pd.DataFrame(
        #np.random.randn(12, 3),
        #columns=['a', 'b', 'c'])
        np.random.randn(12),
        columns=['Total balance'])

    st.line_chart(chart_data)

    st.header("Treasury wallets")
    st.subheader("Balance:")
    st.write("8,045,470.54 AMB / $ 67,984.23")

    st.header("Amb-net multisig")
    st.subheader("Balance:")
    st.write("4.4B AMB / $ x")

    st.header("Safe{Wallet}")
    st.subheader("Balance:")
    st.write("0.1 ETH / $ x")
    st.write("100 USDC / $ 100")

with tab_treasury:
    #st.title("Tokenomics")
    st.header("Summary")
    st.write("Current treasury balance: $ 67,984.23")

    chart_data = pd.DataFrame(
        #np.random.randn(12, 3),
        #columns=['a', 'b', 'c'])
        np.random.randn(12),
        columns=['Total balance'])

    st.line_chart(chart_data)

    st.write()



    tab_summary2, tab_transactions, tab_multisig_signers = st.tabs(["Summary", "Transactions", "Multisig signers"])
    #with st.expander("Multisig signers"):
    with tab_summary2:
        st.empty()

    with tab_safewallet:
        st.header("Safe{Wallet}")

        st.subheader("Balance:")
        st.write("ETH: 0.1")
        st.write("USDC: 100")

    with tab_multisig_signers:
        st.subheader("Active signers")
        col_name, col_amb_net_signer, col_safewallet_signer, col_address = st.columns(4)
        with col_name:
            st.text("""
                Oleksiy Pyltsov
                Michael Grimwood
                Jorma Spitz
                Matthieu Bourlon
                Seth Duodu
                Sophie Bein Mack
                Oleksandr Yaniuk
                Alina Tustanovska
                Igor Stadnyk
                """)
        with col_address:
            st.text("""
                0xa5E32D3fB342D9Ed3135fD5cb59a102AC8ED7B85
                0xB72aDaffEb3419487C49690Dc68e963F7d7D81AC
                0x4Cf8F9058E9Bd31afb6f7c235880a9C65c3ee537
                0x37d6bF7e8875137EefA8286e6AEA2cc4bFAF1247
                0x6fA040aD7e94f905a29536Ba786D433638FeD19b
                0xBc2e61822443b18070E387F045CcFAD33E6958d0
                0xe8592B3a9ee54472A0115262871eF43B5F3e8E53
                0x787afc1E7a61af49D7B94F8E774aC566D1B60e99
                0x55d46039e187b37a0201068dE189ecB63eaE87d2
                """)

        st.subheader("Inactive signers")



with tab_ambnet:
    st.header("New Tokenomics Funds")

    st.subheader("Tokenomic funds total")
    st.write("Total: 4.4B")

    st.subheader("Tokenomics funds distribution")
    st.write("Master wallet: n/a")
    st.write("Rewards wallet: n/a")
    st.write("Investors wallet: n/a")
    st.write("Team wallet: n/a")
    st.write("Ecosystem wallet: n/a")
    #Total
    #per section in numbers
    #per section in graphical statistic

