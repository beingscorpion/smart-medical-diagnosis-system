You can copy and paste the content below directly into a file named **`README.md`** in the root of your repository. I've used **Markdown** for professional formatting and **corrected the terminal commands** for robustness.


# 🧠 Smart Medical Diagnosis System

This project showcases a rule-based expert system implemented using two distinct technologies to perform differential diagnosis for ENT (Ear, Nose, and Throat) conditions.

## 💡 Project Approaches

| Approach | Technology Stack | Key Feature | Complexity |
| :--- | :--- | :--- | :--- |
| **1. Hybrid System** | **Prolog, PySwip, Streamlit** | Uses Prolog for pure logical inference. | High (Requires external dependency). |
| **2. Pure Python Rule-Based** | **Experta, Streamlit** | Provides a highly functional, declarative rule system entirely within the Python stack. | Low (Recommended). |

---

## 1️⃣ Approach 1: Prolog & PySwip (The Hybrid System)

This approach integrates a Prolog knowledge base with a Python/Streamlit front-end.

### 🛑 Critical Prerequisite: SWI-Prolog

The system requires the **SWI-Prolog Interpreter** to be installed on your operating system.

****

**Download Link (Windows x64):**
`https://www.swi-prolog.org/download/stable/bin/swipl-9.2.9-1.x64.exe`

> **⚠️ IMPORTANT:** During installation, ensure you select the option to add the SWI-Prolog executable directory to the **System PATH**. If this step is skipped, the Python integration will fail with a `SwiPrologNotFoundError`.

### 💻 Execution Commands (Windows/VS Code Terminal)

Copy and paste these commands **one-by-one** into your VS Code terminal (or PowerShell) to set up and run the project:

# 1. Create the virtual environment
python -m venv krr_env 

# 2. Activate the environment
.\krr_env\Scripts\activate

# 3. Upgrade pip (optional but recommended)
pip install --upgrade pip 

# 4. Install dependencies (requires pyswip and streamlit in requirements.txt)
pip install -r requirements.txt

# 5. Launch the application
streamlit run app.py



## 2️⃣ Approach 2: Experta (Pure Python Rule-Based)

This approach uses the native Python rule engine `Experta`, simplifying setup and deployment by removing the external Prolog dependency.

### 💻 Execution Commands (Windows/VS Code Terminal)

Copy and paste these commands **one-by-one** into your VS Code terminal (or PowerShell) to set up and run the project:


# 1. Create the virtual environment
python -m venv krr_env 

# 2. Activate the environment
.\krr_env\Scripts\activate

# 3. Upgrade pip (optional but recommended)
pip install --upgrade pip 

# 4. Install dependencies (Experta and Streamlit)
pip install experta streamlit

# 5. Launch the application
streamlit run ./mini_project.py
