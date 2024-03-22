# Hospital Management System Using Django
This hospital management system is designed with the goal of not only being a tool to track and manage patient and medical staff information, but also a smart solution to help optimize work processes, ensuring patient care is delivered in the best and most effective way.

# UML
```mermaid
classDiagram
    class Patient{
        - ID: number
        - PersonalInfo: PersonalInfo
        - MedicalHistory: Date[]
        - TestResult: TestResult
        - TreatmentSchedule: Diary
        - Progress: Progress
        + addPersonalInfo(PersonalInfo: PersonalInfo)
    }

    class PersonalInfo{
        - ...
    }

    class TestResult{
        - Blood:
        - ...
    }

    class HealthcareStaff{
        - Staff: Staff[]
        + addPatientInfo(Patient: Patient)
        + addMedicalHistory(Date: Date)
        + addTestResult(TestResult: TestResult)
        + addTreatmentSchedule(Diary: Diary)
        + evaluateProgress()
    }

    class Staff{
        - ID: number
        - Name: string
        - Age: number
        - Phone: number
        - Address: string
        - Avatar: picture
        - Role: [Doctor, Nurse, Assistant]
        - Certificate: string
        - Specialize: string
        - Availablle: []
    }


    class Facility{
        - Medicine: Medicine[]
        - MedicalEquipment: MedicalEquipment[]
        + addMedicine(Medicine: Medicine)
        + removeMedicine()
        + MedicineInfo()
        + addMedicalEquipment()
        + MedicalEquipmentInfo()
    }

    class Medicine{
        - Name: string
        - Numbers: number
        - Expiry: date
        - InputDay: date
        - OutputDay: date
    }

    class MedicalEquipment{
        - Name: string
        - Numbers: number
        - MaintenaceHistory: date[]
        - Available: []
    }

    class Hospital{
        - Patient: Patient[]
        + PatientAccess(Patient)
        + StaffAccess(HealthcareStaff)
        + WorkDivision(Patient, HealthcareStaff, Facility)
    }

    PersonalInfo <-- Patient
    TestResult <-- Patient
    Staff <-- HealthcareStaff
    Medicine <-- Facility
    MedicalEquipment <-- Facility
    Patient <-- Hospital
    HealthcareStaff *-- Hospital
    Facility *-- Hospital

```

