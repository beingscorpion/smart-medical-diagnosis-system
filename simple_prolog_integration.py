from pyswip import Prolog

prolog = Prolog()
prolog.consult("medical_diagnosis.pl")

def clear_patient(patient_id):
    """Clear patient data"""
    list(prolog.query(f"retractall(patient_symptom({patient_id}, _))"))
    list(prolog.query(f"retractall(patient_symptom_duration({patient_id}, _))"))

def add_symptoms(patient_id, symptoms, duration=None):
    """Add symptoms for a patient"""
    clear_patient(patient_id)
    
    # Add symptoms
    for symptom in symptoms:
        query = f"assertz(patient_symptom({patient_id}, {symptom}))"
        list(prolog.query(query))
    
    # Add duration
    if duration:
        query = f"assertz(patient_symptom_duration({patient_id}, {duration}))"
        list(prolog.query(query))

def diagnose(patient_id, symptoms, duration=None, discharge_types=None):
    """Get diagnosis for patient"""
    # Add symptoms to knowledge base
    add_symptoms(patient_id, symptoms, duration)
    
    # Query for diagnoses
    diagnoses = []
    
    try:
        # Try each diagnosis rule
        if list(prolog.query(f"chronic_sinusitis({patient_id})")):
            diagnoses.append("Chronic Sinusitis")
        
        if list(prolog.query(f"chronic_sinusitis_with_discharge({patient_id})")):
            diagnoses.append("Chronic Sinusitis with Discharge")
        
        if list(prolog.query(f"acute_sinusitis({patient_id})")):
            diagnoses.append("Acute Sinusitis")
        
        if list(prolog.query(f"acute_sinusitis_dental({patient_id})")):
            diagnoses.append("Acute Sinusitis with Dental Pain")
        
        if list(prolog.query(f"allergic_rhinitis({patient_id})")):
            diagnoses.append("Allergic Rhinitis")
        
        if list(prolog.query(f"non_allergic_rhinitis({patient_id})")):
            diagnoses.append("Non-Allergic Rhinitis")
        
        if list(prolog.query(f"deviated_nasal_septum({patient_id})")):
            diagnoses.append("Deviated Nasal Septum")
        
        if list(prolog.query(f"deviated_septum_bleeding({patient_id})")):
            diagnoses.append("Deviated Septum with Nosebleeds")
        
        if list(prolog.query(f"deviated_septum_sleep({patient_id})")):
            diagnoses.append("Deviated Septum with Sleep Issues")
        
        if list(prolog.query(f"deviated_septum_noisy({patient_id})")):
            diagnoses.append("Deviated Septum with Noisy Breathing")
    
    except Exception as e:
        print(f"Error during diagnosis: {e}")
        diagnoses.append(f"Error: {e}")
    
    return diagnoses if diagnoses else ["No diagnosis found"]