import collections
import collections.abc
collections.Mapping = collections.abc.Mapping

from experta import KnowledgeEngine, Fact, Rule
import streamlit as st

class Symptom(Fact):
    pass

class ENTEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnoses = []

    @Rule(Symptom(duration='chronic', nasal_congestion=True, facial_pressure=True))
    def chronic_sinusitis1(self):
        self.diagnoses.append('Chronic Sinusitis')

    @Rule(Symptom(duration='chronic', nasal_congestion=True, loss_of_smell=True))
    def chronic_sinusitis2(self):
        self.diagnoses.append('Chronic Sinusitis')

    @Rule(Symptom(duration='chronic', facial_pressure=True, loss_of_smell=True))
    def chronic_sinusitis3(self):
        self.diagnoses.append('Chronic Sinusitis')

    @Rule(Symptom(duration='chronic', nasal_discharge=True, facial_pain=True))
    def chronic_sinusitis_discharge1(self):
        self.diagnoses.append('Chronic Sinusitis (with discharge)')

    @Rule(Symptom(duration='chronic', nasal_discharge=True, postnasal_drip=True))
    def chronic_sinusitis_discharge2(self):
        self.diagnoses.append('Chronic Sinusitis (with discharge)')

    @Rule(Symptom(duration='acute', nasal_congestion=True, facial_pain=True))
    def acute_sinusitis1(self):
        self.diagnoses.append('Acute Sinusitis')

    @Rule(Symptom(duration='acute', nasal_congestion=True, fever=True))
    def acute_sinusitis2(self):
        self.diagnoses.append('Acute Sinusitis')

    @Rule(Symptom(duration='acute', facial_pain=True, fever=True))
    def acute_sinusitis3(self):
        self.diagnoses.append('Acute Sinusitis')

    @Rule(Symptom(duration='acute', tooth_pain=True, nasal_discharge=True))
    def acute_sinusitis_dental1(self):
        self.diagnoses.append('Acute Sinusitis with Dental Pain')

    @Rule(Symptom(duration='acute', tooth_pain=True, facial_pressure=True))
    def acute_sinusitis_dental2(self):
        self.diagnoses.append('Acute Sinusitis with Dental Pain')

    @Rule(Symptom(duration='acute', tooth_pain=True, headache=True))
    def acute_sinusitis_dental3(self):
        self.diagnoses.append('Acute Sinusitis with Dental Pain')

    @Rule(Symptom(sneezing=True, itchy_nose=True, nasal_discharge=True))
    @Rule(Symptom(sneezing=True, itchy_nose=True, itchy_eyes=True))
    @Rule(Symptom(sneezing=True, itchy_nose=True, watery_eyes=True))
    @Rule(Symptom(sneezing=True, itchy_eyes=True, watery_eyes=True))
    @Rule(Symptom(itchy_nose=True, itchy_eyes=True, watery_eyes=True))
    def allergic_rhinitis(self):
        self.diagnoses.append('Allergic Rhinitis')

    @Rule(Symptom(duration='chronic', nasal_congestion=True, nasal_discharge=True,
                  itchy_nose=False, sneezing=False))
    def non_allergic_rhinitis(self):
        self.diagnoses.append('Non-Allergic Rhinitis')

    @Rule(Symptom(duration='chronic', unilateral_congestion=True, difficulty_breathing=True))
    @Rule(Symptom(duration='chronic', unilateral_congestion=True, mouth_breathing=True))
    def deviated_septum(self):
        self.diagnoses.append('Deviated Nasal Septum')

    @Rule(Symptom(duration='chronic', unilateral_congestion=True, nosebleeds=True))
    def deviated_septum_bleeding(self):
        self.diagnoses.append('Deviated Septum with Nosebleeds')

    @Rule(Symptom(duration='chronic', unilateral_congestion=True, snoring=True,
                  mouth_breathing=True))
    @Rule(Symptom(duration='chronic', unilateral_congestion=True, snoring=True,
                  difficulty_breathing=True))
    def deviated_septum_sleep(self):
        self.diagnoses.append('Deviated Septum with Sleep Issues')

    @Rule(Symptom(duration='chronic', unilateral_congestion=True, noisy_breathing=True))
    def deviated_septum_noisy(self):
        self.diagnoses.append('Deviated Septum with Noisy Breathing')

    @Rule(Symptom())
    def fallback(self):
        if not self.diagnoses:
            self.diagnoses.append('No clear diagnosis')


st.title('Rule Based System Using Experta')

with st.form(key='symptom_form_final'):
    st.header('Patient data')
    duration_choice = st.radio('Symptom duration', options=['acute','chronic'])
    fever = st.checkbox('Fever')
    nasal_congestion = st.checkbox('Nasal congestion')
    nasal_discharge = st.checkbox('Nasal discharge')
    facial_pain = st.checkbox('Facial pain')
    facial_pressure = st.checkbox('Facial pressure')
    loss_of_smell = st.checkbox('Loss of smell')
    sneezing = st.checkbox('Sneezing')
    itchy_nose = st.checkbox('Itchy nose')
    itchy_eyes = st.checkbox('Itchy eyes')
    watery_eyes = st.checkbox('Watery eyes')
    unilateral_congestion = st.checkbox('Unilateral congestion')
    difficulty_breathing = st.checkbox('Difficulty breathing')
    mouth_breathing = st.checkbox('Mouth breathing')
    snoring = st.checkbox('Snoring')
    noisy_breathing = st.checkbox('Noisy breathing')
    nosebleeds = st.checkbox('Nosebleeds')
    headache = st.checkbox('Headache')
    tooth_pain = st.checkbox('Tooth pain')
    postnasal_drip = st.checkbox('Postnasal drip')

    submitted = st.form_submit_button('Assess')

if submitted:
    engine = ENTEngine()
    engine.reset()
    engine.declare(Symptom(duration=duration_choice, fever=fever,
                           nasal_congestion=nasal_congestion, nasal_discharge=nasal_discharge,
                           facial_pain=facial_pain, facial_pressure=facial_pressure,
                           loss_of_smell=loss_of_smell, sneezing=sneezing, itchy_nose=itchy_nose,
                           itchy_eyes=itchy_eyes, watery_eyes=watery_eyes,
                           unilateral_congestion=unilateral_congestion, difficulty_breathing=difficulty_breathing,
                           mouth_breathing=mouth_breathing, snoring=snoring, noisy_breathing=noisy_breathing,
                           nosebleeds=nosebleeds, headache=headache, tooth_pain=tooth_pain,
                           postnasal_drip=postnasal_drip))
    engine.run()

    st.subheader('Likely Diagnoses')
    if engine.diagnoses:
        for d in set(engine.diagnoses):
            st.write('- ', d)
    else:
        st.write('No likely diagnosis determined from the inputs.')
