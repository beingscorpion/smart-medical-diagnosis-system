symptom(nasal_congestion).
symptom(nasal_discharge).
symptom(facial_pain).
symptom(facial_pressure).
symptom(loss_of_smell).
symptom(fever).
symptom(sneezing).
symptom(itchy_nose).
symptom(itchy_eyes).
symptom(watery_eyes).
symptom(unilateral_congestion).
symptom(difficulty_breathing).
symptom(nosebleeds).
symptom(snoring).
symptom(mouth_breathing).
symptom(noisy_breathing).
symptom(headache).
symptom(tooth_pain).
symptom(postnasal_drip).

duration(acute).
duration(chronic).

% Dynamic predicates
:- dynamic patient_symptom/2.
:- dynamic patient_symptom_duration/2.

% DIAGNOSTIC RULES

% Rule 1: Chronic Sinusitis (needs duration + 2 of 3 main symptoms)
chronic_sinusitis(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, nasal_congestion),
    (patient_symptom(Patient, facial_pressure) ; patient_symptom(Patient, loss_of_smell)).

chronic_sinusitis(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, facial_pressure),
    patient_symptom(Patient, loss_of_smell).

% Rule 2: Chronic Sinusitis with Discharge (needs duration + 2 of 3 symptoms)
chronic_sinusitis_with_discharge(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, nasal_discharge),
    (patient_symptom(Patient, facial_pain) ; patient_symptom(Patient, postnasal_drip)).

% Rule 3: Acute Sinusitis (needs acute duration + 2 of 3 main symptoms)
acute_sinusitis(Patient) :-
    patient_symptom_duration(Patient, acute),
    patient_symptom(Patient, nasal_congestion),
    (patient_symptom(Patient, facial_pain) ; patient_symptom(Patient, fever)).

acute_sinusitis(Patient) :-
    patient_symptom_duration(Patient, acute),
    patient_symptom(Patient, facial_pain),
    patient_symptom(Patient, fever).

% Rule 4: Acute Sinusitis with Tooth Pain (needs acute + 2 of 4 symptoms)
acute_sinusitis_dental(Patient) :-
    patient_symptom_duration(Patient, acute),
    patient_symptom(Patient, tooth_pain),
    (patient_symptom(Patient, nasal_discharge) ; patient_symptom(Patient, facial_pressure) ; patient_symptom(Patient, headache)).

% Rule 5: Allergic Rhinitis (needs 3 of 5 symptoms)
allergic_rhinitis(Patient) :-
    patient_symptom(Patient, sneezing),
    patient_symptom(Patient, itchy_nose),
    (patient_symptom(Patient, nasal_discharge) ; patient_symptom(Patient, itchy_eyes) ; patient_symptom(Patient, watery_eyes)).

allergic_rhinitis(Patient) :-
    patient_symptom(Patient, sneezing),
    patient_symptom(Patient, itchy_eyes),
    patient_symptom(Patient, watery_eyes).

allergic_rhinitis(Patient) :-
    patient_symptom(Patient, itchy_nose),
    patient_symptom(Patient, itchy_eyes),
    patient_symptom(Patient, watery_eyes).

% Rule 6: Non-Allergic Rhinitis (needs chronic + congestion + discharge, but NO itchy symptoms)
non_allergic_rhinitis(Patient) :-
    patient_symptom(Patient, nasal_congestion),
    patient_symptom(Patient, nasal_discharge),
    \+ patient_symptom(Patient, itchy_nose),
    \+ patient_symptom(Patient, sneezing),
    patient_symptom_duration(Patient, chronic).

% Rule 7: Deviated Nasal Septum (needs chronic + unilateral + 1 breathing issue)
deviated_nasal_septum(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, unilateral_congestion),
    (patient_symptom(Patient, difficulty_breathing) ; patient_symptom(Patient, mouth_breathing)).

% Rule 8: Deviated Septum with Nosebleeds
deviated_septum_bleeding(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, unilateral_congestion),
    patient_symptom(Patient, nosebleeds).

% Rule 9: Deviated Septum with Sleep Issues
deviated_septum_sleep(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, unilateral_congestion),
    patient_symptom(Patient, snoring),
    (patient_symptom(Patient, mouth_breathing) ; patient_symptom(Patient, difficulty_breathing)).

% Rule 10: Deviated Septum with Noisy Breathing
deviated_septum_noisy(Patient) :-
    patient_symptom_duration(Patient, chronic),
    patient_symptom(Patient, unilateral_congestion),
    patient_symptom(Patient, noisy_breathing).