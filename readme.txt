This smart medical diagnosis system is implement using two different approach. 
1) Prolog integration with pyswip and streamlit which is complex and hard to understand.
2) Rule based using Experta.: While Prolog is philosophically the perfect language for pure logical inference, experta provides a highly functional, declarative rule system entirely within the modern Python application stack.

1)for Prolog pyswip and streamlit approach:
Critical Prerequisite 

The system requires the SWI-Prolog Interpreter to be installed on your operating system.

Download Link (Windows x64): https://www.swi-prolog.org/download/stable/bin/swipl-9.2.9-1.x64.exe

IMPORTANT: During the SWI-Prolog installation, ensure you select the option to add the SWI-Prolog executable directory to the system PATH. If you skip this, the Python integration will fail.

copy and paste these command on terminal of vs code to run this:

python -m venv krr_env 
.\krr_env\Scripts\activate
pip install --upgrade pip 
pip install -r requirements.txt
streamlit run app.py

----------------------------------------------------------------------------------------------------------------
2)Experta Rule based system:

Copy and paste them on vs code terminal

python -m venv krr_env 
.\krr_env\Scripts\activate
pip install --upgrade pip 
pip install experta
streamlit run ./mini_project.py