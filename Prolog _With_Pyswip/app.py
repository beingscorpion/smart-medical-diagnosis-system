import streamlit as st
import prolog_integration as prolog


DIAGNOSIS_PATTERNS = {
    "Chronic Sinusitis": {
        "duration": "chronic",
        "combinations": [
            ["nasal_congestion", "facial_pressure"],
            ["nasal_congestion", "loss_of_smell"],
            ["facial_pressure", "loss_of_smell"]
        ]
    },
    "Chronic Sinusitis with Discharge": {
        "duration": "chronic",
        "combinations": [
            ["nasal_discharge", "facial_pain"],
            ["nasal_discharge", "postnasal_drip"]
        ]
    },
    "Acute Sinusitis": {
        "duration": "acute",
        "combinations": [
            ["nasal_congestion", "facial_pain"],
            ["nasal_congestion", "fever"],
            ["facial_pain", "fever"]
        ]
    },
    "Acute Sinusitis with Dental Pain": {
        "duration": "acute",
        "combinations": [
            ["tooth_pain", "nasal_discharge"],
            ["tooth_pain", "facial_pressure"],
            ["tooth_pain", "headache"]
        ]
    },
    "Allergic Rhinitis": {
        "duration": None,
        "combinations": [
            ["sneezing", "itchy_nose", "nasal_discharge"],
            ["sneezing", "itchy_nose", "itchy_eyes"],
            ["sneezing", "itchy_nose", "watery_eyes"],
            ["sneezing", "itchy_eyes", "watery_eyes"],
            ["itchy_nose", "itchy_eyes", "watery_eyes"]
        ]
    },
    "Non-Allergic Rhinitis": {
        "duration": "chronic",
        "combinations": [
            ["nasal_congestion", "nasal_discharge"]
        ],
        "exclude": ["itchy_nose", "sneezing"]
    },
    "Deviated Nasal Septum": {
        "duration": "chronic",
        "combinations": [
            ["unilateral_congestion", "difficulty_breathing"],
            ["unilateral_congestion", "mouth_breathing"]
        ]
    },
    "Deviated Septum with Nosebleeds": {
        "duration": "chronic",
        "combinations": [
            ["unilateral_congestion", "nosebleeds"]
        ]
    },
    "Deviated Septum with Sleep Issues": {
        "duration": "chronic",
        "combinations": [
            ["unilateral_congestion", "snoring", "mouth_breathing"],
            ["unilateral_congestion", "snoring", "difficulty_breathing"]
        ]
    },
    "Deviated Septum with Noisy Breathing": {
        "duration": "chronic",
        "combinations": [
            ["unilateral_congestion", "noisy_breathing"]
        ]
    }
}

SYMPTOM_NAMES = {
    "nasal_congestion": "Nasal Congestion",
    "nasal_discharge": "Nasal Discharge",
    "facial_pain": "Facial Pain",
    "facial_pressure": "Facial Pressure",
    "loss_of_smell": "Loss of Smell",
    "fever": "Fever",
    "headache": "Headache",
    "tooth_pain": "Tooth Pain",
    "postnasal_drip": "Postnasal Drip",
    "sneezing": "Sneezing",
    "itchy_nose": "Itchy Nose",
    "itchy_eyes": "Itchy Eyes",
    "watery_eyes": "Watery Eyes",
    "unilateral_congestion": "Unilateral Congestion",
    "difficulty_breathing": "Difficulty Breathing",
    "nosebleeds": "Nosebleeds",
    "snoring": "Snoring",
    "mouth_breathing": "Mouth Breathing",
    "noisy_breathing": "Noisy Breathing"
}

def get_valid_symptoms_for_duration(duration, selected_symptoms):
    """Get symptoms that can lead to a diagnosis"""
    valid_symptoms = []
    
    for diagnosis_name in DIAGNOSIS_PATTERNS:
        pattern = DIAGNOSIS_PATTERNS[diagnosis_name]
        
        if pattern["duration"] == None:
            duration_matches = True
        elif pattern["duration"] == duration:
            duration_matches = True
        else:
            duration_matches = False
        
        if not duration_matches:
            continue
        
        for combo in pattern["combinations"]:
        
            if len(selected_symptoms) == 0:
                for symptom in combo:
                    if symptom not in valid_symptoms:
                        valid_symptoms.append(symptom)
            else:
                
                all_match = True
                for selected in selected_symptoms:
                    if selected not in combo:
                        all_match = False
                        break
                
                if all_match:
                    for symptom in combo:
                        if symptom not in valid_symptoms:
                            valid_symptoms.append(symptom)
    
    return valid_symptoms

def can_lead_to_diagnosis(selected_symptoms, duration):

    for diagnosis_name in DIAGNOSIS_PATTERNS:
        pattern = DIAGNOSIS_PATTERNS[diagnosis_name]
        
        if pattern["duration"] == None:
            duration_matches = True
        elif pattern["duration"] == duration:
            duration_matches = True
        else:
            duration_matches = False
        
        if not duration_matches:
            continue
        
        for combo in pattern["combinations"]:
            
            all_in_combo = True
            for selected in selected_symptoms:
                if selected not in combo:
                    all_in_combo = False
                    break
            
            if all_in_combo:
                return True
    
    return False

st.set_page_config(page_title="Medical Diagnosis System", page_icon="🏥")
st.title("🏥 Smart Medical Diagnosis System")
st.write("Select symptoms step-by-step. Only symptoms that can lead to a diagnosis are shown.")

st.subheader("⏱️ Step 1: Duration")
duration_choice = st.radio(
    "How long have you had these symptoms?",
    ["Acute (< 4 weeks)", "Chronic (> 12 weeks)"],
    key="duration",
    horizontal=True
)
duration_map = {"Acute (< 4 weeks)": "acute", "Chronic (> 12 weeks)": "chronic"}
selected_duration = duration_map[duration_choice]

if 'selected_symptoms' not in st.session_state:
    st.session_state.selected_symptoms = []

valid_symptoms = get_valid_symptoms_for_duration(selected_duration, st.session_state.selected_symptoms)


valid_symptom_names = []
for symptom in valid_symptoms:
    symptom_name = SYMPTOM_NAMES[symptom]
    valid_symptom_names.append(symptom_name)
valid_symptom_names.sort()


st.subheader("🔍 Step 2: Select Your Symptoms")
st.info(f"📌 Showing {len(valid_symptom_names)} relevant symptoms that can lead to a diagnosis")


default_values = []
for symptom in st.session_state.selected_symptoms:
    if symptom in valid_symptoms:
        default_values.append(SYMPTOM_NAMES[symptom])

selected_symptom_names = st.multiselect(
    "Choose symptoms:",
    options=valid_symptom_names,
    default=default_values,
    key="symptom_selector"
)


st.session_state.selected_symptoms = []
for symptom_key in SYMPTOM_NAMES:
    symptom_value = SYMPTOM_NAMES[symptom_key]
    if symptom_value in selected_symptom_names:
        st.session_state.selected_symptoms.append(symptom_key)


if len(st.session_state.selected_symptoms) > 0:
    st.write("**Currently selected:**")
    cols = st.columns(3)
    for i in range(len(st.session_state.selected_symptoms)):
        symptom = st.session_state.selected_symptoms[i]
        col_index = i % 3
        with cols[col_index]:
            st.success(f"✓ {SYMPTOM_NAMES[symptom]}")


st.subheader("🔬 Step 3: Get Diagnosis")
col1, col2 = st.columns([1, 3])

with col1:
    diagnose_btn = st.button("🔬 Diagnose", type="primary", use_container_width=True)

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.selected_symptoms = []
        st.rerun()

if diagnose_btn:
    if len(st.session_state.selected_symptoms) > 0:
        with st.spinner("Analyzing symptoms..."):
            diagnoses = prolog.diagnose("patient1", st.session_state.selected_symptoms, selected_duration, None)
        
        st.subheader("📋 Diagnosis Results:")
        
        if len(diagnoses) > 0 and diagnoses[0] != "No diagnosis found":
            st.success(f"✅ Found {len(diagnoses)} possible diagnosis(es):")
            for i in range(len(diagnoses)):
                d = diagnoses[i]
                st.markdown(f"**{i + 1}. {d}**")
        else:
            st.warning("⚠️ No diagnosis found. You may need to select more symptoms.")
            if can_lead_to_diagnosis(st.session_state.selected_symptoms, selected_duration):
                st.info("💡 Your current selection is on the right track. Try adding more symptoms.")
    else:
        st.warning("⚠️ Please select at least one symptom.")