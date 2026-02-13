import streamlit as st

st.title("Password Validation and Encryption")

password = st.text_input("Enter the password", type="password")

if st.button("Validate and Encrypt"):

    if password == "":
        st.warning("Please enter password")

    elif len(password) < 8:
        st.error("Password must be at least 8 characters")

    elif password[4] not in "12345":
        st.error("5th character must be between 1 and 5")

    elif not any(c.isupper() for c in password):
        st.error("Password must contain at least 1 uppercase letter")

    elif not any(c.islower() for c in password):
        st.error("Password must contain at least 1 lowercase letter")

    else:
        encrypted = ""

        for ch in password:
            if ch == "b":
                encrypted += "1"
            elif ch == "A":
                encrypted += "@"
            elif ch == "a":
                encrypted += "B"
            else:
                encrypted += ch

        st.success("Thank you for entering valid password!")
        st.write("Encrypted password:", encrypted)

