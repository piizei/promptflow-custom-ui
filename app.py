import streamlit as st

from promptflow import adapt_openai_to_prompt_flow

st.title("PrompFlow ChatGPT")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = adapt_openai_to_prompt_flow(
            [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        full_response += response
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    
    
    