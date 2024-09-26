import generic_prompt_engine as gpe
import json
import streamlit as st


def url_check(x):
    """
a function that checks whether a url is valid or not

:parameters
- a key value dictionary with the model_inout, token, and tags(optional)

:return type
- a boolean indicating whether the url is valid or not

"""
    try:
        if isinstance(eval(x), dict):
            content = gpe.prompting(json.loads(x), "return hi")
            if "error" not in content:
                st.sidebar.success("The LLMs url and token are correct")
                return True
            else:
                st.sidebar.error("The provided sample is not correct\nError : " + content["error"])
                return False
    except Exception as e:
        st.sidebar.error(f"Error : {e}.\nEnter correct input")
        return False
