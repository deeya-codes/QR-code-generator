import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="UPI QR Generator", page_icon="💳")

st.title("💳 UPI QR Code Generator")

upi_id = st.text_input("Enter UPI ID", placeholder="example@upi")

if st.button("Generate QR Code"):

    if upi_id:

        upi_url = f"upi://pay?pa={upi_id}&cu=INR"

        qr = qrcode.make(upi_url)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        st.image(buffer, caption="UPI QR Code", width=300)

        st.download_button(
            "📥 Download QR",
            data=buffer.getvalue(),
            file_name="UPI_QR.png",
            mime="image/png"
        )

    else:
        st.error("Please enter a UPI ID.")