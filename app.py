from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
# Define symptoms and FAQs
symptoms_dict = {
    "Breast Cancer": {"lump or mass", "change in breast size", "change in nipple size", "skin changes", "redness", "swelling", "discharge from nipple", "pain"},
    "PCOD": {"irregular periods", "excessive hair growth", "acne", "weight gain", "ovarian cysts", "thinning hair", "dark skin patches"},
    "Uterine Fibroids": {"heavy bleeding", "pelvic pain", "frequent urination", "difficulty emptying the bladder", "lower back pain", "enlarged abdomen"},
    "Urinary Infection": {"frequent urination", "burning sensation", "bloody or cloudy urine", "strong smelling urine", "lower abdominal pain", "urgency", "fever", "chills"},
    "Mastitis": {"breast pain", "tenderness", "heat", "painful lump", "hard spot", "clogged milk ducts", "fever", "swollen lymph"}
}

faqs_dict = {
    "Breast Cancer": {
        "What are early stages of breast cancer?": "A lump, changes in breast size, nipple discharge, or skin changes.",
        "How often should I perform self-breast exams?": "Monthly, ideally a week after your period ends.",
        "What age should I start getting mammograms?": "Typically at age 40, but earlier if you have risk factors.",
        "Can men get breast cancer?": "Yes, although it is rare.",
        "What are the treatment options for breast cancer?": "Surgery, radiation, chemotherapy, hormone therapy, or targeted therapy."
    },
    "PCOD": {
        "What are the common symptoms of PCOD?": "Irregular periods, excessive hair growth, acne, and weight gain.",
        "How does PCOD affect fertility?": "It can cause irregular ovulation, leading to difficulty conceiving.",
        "Can PCOD be managed with lifestyle changes?": "Yes, diet and exercise can help manage symptoms.",
        "Is weight gain associated with PCOD?": "Yes, many women with PCOD experience weight gain.",
        "What treatments are available for PCOD?": "Birth control pills, lifestyle changes, and medications like metformin."
    },
    "Uterine Fibroids": {
        "What are uterine fibroids, and how common are they?": "Non-cancerous growths in the uterus; very common in women of reproductive age.",
        "What symptoms indicate the presence of fibroids?": "Heavy bleeding, pelvic pain, frequent urination.",
        "Can uterine fibroids affect pregnancy?": "Yes, they can cause complications like miscarriage or preterm birth.",
        "How are fibroids diagnosed?": "Through ultrasound, MRI, or pelvic exams.",
        "What are the treatment options for fibroids?": "Medication, non-invasive procedures, or surgery."
    },
    "Urinary Infection": {
        "What are the common symptoms of a urinary tract infection (UTI)?": "Burning sensation, frequent urination, and cloudy or bloody urine.",
        "How can I prevent urinary infections?": "Stay hydrated, urinate after intercourse, and maintain good hygiene.",
        "Are urinary infections more common in women than men?": "Yes, due to the shorter urethra in women.",
        "What should I do if I have frequent urinary infections?": "Consult a doctor for a potential underlying issue.",
        "What are the common treatments for UTIs?": "Antibiotics are the primary treatment."
    },
    "Mastitis": {
        "What is mastitis, and what causes it?": "An infection of the breast tissue, often caused by blocked milk ducts.",
        "What are the symptoms of mastitis?": "Breast pain, swelling, redness, and flu-like symptoms.",
        "How is mastitis treated?": "Antibiotics, pain relievers, and frequent breastfeeding or pumping.",
        "Can I continue breastfeeding if I have mastitis?": "Yes, it's usually safe and helps clear the infection.",
        "How can I prevent mastitis while breastfeeding?": "Ensure proper latching, avoid skipping feedings, and fully empty the breast."
    }
}
global name, gender, age

@app.route('/')
def index():
    return render_template('index.html')

'''
LETS MAKE THIS GLOBAL 
'''


@app.route('/diagnose/<execution_type>', methods=['POST'])
def diagnose(execution_type:int):
    faq_answer = ''
    if(execution_type == 0):
        name = request.form.get('name')
        gender = request.form.get('gender')
        age= request.form.get('age')
        print(request.form.getlist('symptoms'))
        print(f"Gender: {gender}, Age: {age}")
        execution_type = int(execution_type)
        diagnoses = []
        symptoms = request.form.getlist('symptoms')[0].split(',')
        
        for disease, disease_symptoms in symptoms_dict.items():
            matching_symptoms = sum(1 for symptom in symptoms if symptom.lower().strip() in disease_symptoms)
            if matching_symptoms >= 4:
                diagnoses.append(f"May be {disease}.")
        
        if not diagnoses:
            diagnoses.append("The patient is not affected by any of the above 5 diseases.")
    else:
        faq_question = request.form.get('faq')
        faq_answer = "Sorry to say this but I am not enough programmed to answer these questions."
        if faq_question:
            for disease, faqs in faqs_dict.items():
                if faq_question in faqs:
                    faq_answer = faqs[faq_question]
                    break

    return render_template('diagnosis.html', name=name, diagnosis=diagnoses,faq_answer=faq_answer)

if __name__ == '__main__':
    app.run(debug=True)
