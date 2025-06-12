# LLM Comparision tool
- Designed a Web Application for comparing responses of different LLMs to a given prompt.
- Created the frontend using Streamlit to allow users to input API details of LLM and prompts. The page then displays the
received response in a column-wise format.
- Developed the Backend that returns the response for the selected LLM.

## Getting Started
```shell
git clone https://github.com/AdityaUnal/llm-comparision.git
pip install -r requirements.txt
streamlit run frontend.py
```

## Working

![Screenshot from 2025-05-13 13-39-09](https://github.com/user-attachments/assets/397ec91c-20ca-45b8-88cc-1fd59f7c82f6)

## Screenshots 

![Screenshot from 2025-05-13 13-45-44](https://github.com/user-attachments/assets/8da40783-ab7c-4be4-90e4-51d115f4909a)</br>
![responses](https://github.com/user-attachments/assets/809bd7cb-e25f-486d-8f82-66a93d872176)
1. **Enter LLM Details**  
   The user inputs LLM details (e.g., model name, API endpoint, or other configurations) in the text box on the left panel.

2. **Validate LLM Details**  
   The **Generic Prompt Engine** checks the entered details to ensure they are valid and can be queried.

3. **Checklist Display**  
   Once validated, the LLMs are added to a **checklist** UI component, allowing users to see which models are ready for comparison.

4. **Enter Prompt and Select LLMs**  
   The user enters a prompt/question and selects one or more LLMs from the checklist to **compare responses**.
