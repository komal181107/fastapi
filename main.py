from fastapi import FastAPI, Path,HTTPException
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        return data

@app.get("/")
def hello():
    return{'message':'Patient Management system api'}


@app.get("/about")
def about():
    return{'message':'A fully functional api to manage your patient record'}


@app.get('/view')
def view():
    data=load_data()

    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str=Path(..., description="id of the patient in the db",example='P001')):
    #load att the patient
    data=load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="patient not found")
