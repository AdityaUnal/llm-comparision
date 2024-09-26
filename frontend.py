import streamlit as st
import url_check as uc
import generic_prompt_engine as gpe
import json


def show():
    st.title("LLM comparison")
    st.sidebar.header("Enter your LLMs here")
    # stores all the LLMs
    if "LLMs_list" not in st.session_state:
        st.session_state.LLMs_list = []

    # stores all the LLMs selected for comparison
    if "selected_LLM" not in st.session_state:
        st.session_state.selected_LLM = []

    # stores all the outputs selected for comparison
    if "output" not in st.session_state:
        st.session_state.output = []

    prompt = st.chat_input("Enter the prompt here")

    def LLMs():
        st.sidebar.text("sample input:")
        code = '''
         {
         "model_endpoint": "abc.com",
         "token": "1234",
         "Content-Type": "application/json" 
                }'''

        st.sidebar.code(code, language="python")
        x = st.sidebar.text_area("Enter here")
        submit_LLM = st.sidebar.button("Submit", key="submit_LLM")

        # if submit_LLM is True:
        #     if uc.url_check(x):
        if x not in st.session_state.LLMs_list:
            st.session_state.LLMs_list.append(x)
        else:
            st.sidebar.error("This LLM is already here")
        if "LLMs_list" in st.session_state:
            for llm in st.session_state.LLMs_list:
                is_checked = st.sidebar.checkbox(label=llm, key=llm)
                if is_checked:
                    if llm not in st.session_state.selected_LLM:
                        st.session_state.selected_LLM.append(llm)
                else:
                    if llm in st.session_state.selected_LLM:
                        st.session_state.selected_LLM.remove(llm)

    def responses():
        LLMs_response = []
        # print(prompt)
        st.session_state.output.append(prompt)
        for llm in st.session_state.selected_LLM:
            # LLMs_response.append(gpe.prompting(json.loads(llm), prompt))

            LLMs_response.append("sample input of" + prompt)
        st.session_state.output.append(LLMs_response)

    def display_output():
        for item in st.session_state.output:
            if isinstance(item, list):
                ncol = len(item)
                cols = st.columns(ncol)
                for i in range(ncol):
                    with cols[i]:
                        st.subheader(f"response {i+1} ")
                        st.write(item[i])
            else:
                st.write("prompt : " + item)
    LLMs()

    if prompt:
        if len(st.session_state.selected_LLM) > 0:
            responses()
            display_output()
        else:
            st.error("Please select at least one llm")


if __name__ == "__main__":
    show()
