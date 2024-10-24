from dotenv import load_dotenv
import os
# Load the .env file
load_dotenv()
# Use the API key
api_key = os.getenv('OPENAI_API_KEY')
# Do NOT print the API key to avoid exposing it
# print(f"API Key: {api_key}")

import json
from swarm import Agent

# Example Tools / Functions
#def process_refund(item_id, reason="NOT SPECIFIED"):
#    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before #processing the refund."""
#    print(f"[mock] Refunding item {item_id} because {reason}...")
#    return "Success!"
#def apply_discount():
#    """Apply a discount to the user's cart."""
#    print("[mock] Applying discount...")
#    return "Applied discount of 11%"

## Agents
triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a diagnostic interviewer agent. You will conduct a diagnostic interview with a patient to gather sufficient information to suggest a strong, potential diagnosis. Begin by asking general questions about the patient's symptoms, health history, and lifestyle. As the patient responds, adapt your questions dynamically, probing deeper into specific symptoms and possible conditions. Ensure that you follow up on any red flags, refine your questions to rule out or confirm diagnoses, and stop asking questions once you have enough information to confidently suggest a diagnosis. Use clear, patient-friendly language, and make sure to address any patient confusion or need for clarification. Always provide a rationale for your follow-up questions and gather enough data to justify your diagnostic conclusions.",
    functions=[],
)

diagnostic_agent = Agent(
    name="Diagnostic Agent",
    instructions="You are an agent that provides medical diagnoses. Assist in diagnosing cancer by analyzing various patient data from user input. Based on current patterns, list the possible cancer types or subtypes and assess the likelihood of each diagnosis. If possible, highlight specific features or abnormalities that support your conclusions, referencing any similar historical cases or known biomarkers", 
    functions=[],
)

prognostic_agent = Agent(
    name="Prognostic Agent",
    instructions="You are a patient prognosis agent. Predict patient outcomes based on their specific diagnosis, treatment history, and other relevant factors. Given the diagnosis of [specific cancer type], assess the prognosis for the patient by analyzing available [historical patient data, treatment outcomes, and progression markers]. Provide estimated survival rates, risk of recurrence, and likely disease progression over an appropriate time period. Include relevant factors such as [patients age, biomarkers, genetic profile, and comorbidities] that influence the prognosis. Also, suggest any warning signs that should be monitored closely.",
    functions=[],
)

treatment_plan_agent = Agent(
    name="Treatment Plan Agent",
    instructions="You are an agent that provides treatment plans. Generate personalized treatment recommendations based on a patients diagnosis, genetic profile, and medical history. Given the patients diagnosis of [specific cancer type], analyze their [genetic profile, treatment history, and current health status] to recommend a personalized treatment plan. Consider the latest approved treatments, potential participation in clinical trials, and the effectiveness of targeted therapies. Provide a rationale for each recommended treatment, noting any potential side effects, contraindications, and expected outcomes.",
    functions=[],
)

clinical_guidelines_agent = Agent(
    name="Clinical Guidelines Agent",
    instructions="You are an agent that cross-checks suggested treatment plans with Clinical Guidelines and highlights deviations.Ensure treatment recommendations adhere to the latest clinical guidelines and protocols in oncology. Cross-reference the suggested treatment plan for [specific cancer type] with the most recent clinical guidelines from [NCCN, ASCO, or relevant governing body]. Ensure the recommendations align with approved standards for treatment, including [surgery, chemotherapy, radiation, immunotherapy]. Highlight any deviations from the standard of care and provide justifications based on the patient’s unique characteristics or emerging research.",
    functions=[],
)

final_agent = Agent(
    name="Final Agent",
    instructions="You are a doctor writing a comprehensive report on a patient. You will compile a comprehensive report for a patient based on information gathered from the Diagnostic, Prognostic, Treatment Plan, Clinical Guidelines, and Diagnostic Tests Suggesting agents. Use the diagnostic agent’s findings to provide a detailed summary of the likely diagnosis, the prognostic agent’s data to give a prediction of the disease course and potential outcomes, and the treatment plan agent’s recommendations to propose a personalized treatment plan. Cross-reference this plan with the clinical guidelines agent to highlight where the suggestions deviate from latest medical standards, and include any suggested diagnostic tests from the diagnostic tests agent for further clarity. Provide a clear, patient-friendly summary of each section, and include rationale for all conclusions and recommendations, noting any potential risks, benefits, and alternative treatment paths. Ensure the report is thorough yet easy to understand, offering both clinicians and the patient a comprehensive view of the condition and next steps.”",
    functions=[],
)


def transfer_to_triage():
#    """Call this function if a user or patient is providing more information about the patient."""    
    return triage_agent
def transfer_to_diagnostic():
    return diagnostic_agent
def transfer_to_prognostic():
    return prognostic_agent
def transfer_to_treatment_plan():
    return treatment_plan_agent
def transfer_to_clinical_guidelines():
    return clinical_guidelines_agent
def transfer_to_final_agent():
    return final_agents


triage_agent.functions.append(transfer_to_diagnostic)
diagnostic_agent.functions.append(transfer_to_prognostic)
prognostic_agent.functions.append(transfer_to_treatment_plan)
treatment_plan_agent.functions.append(transfer_to_clinical_guidelines)
clinical_guidelines_agent.functions.append(transfer_to_final_agent)