class Patient(object):
	Patient_Count = 0

	def __init__(self,  name, allergies):
		self.name = name
		self.allergies = allergies
		self.id = Patient.Patient_Count
		self.bed_num = None
		Patient.Patient_Count += 1


class Hospital(object):
	
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []
		self.beds = self.initialize_beds()

	def initialize_beds(self):
		beds = []
		for i in range(0,self.capacity):
			beds.append({
				"bed_id": i,
				"Available": True
				})
		return beds 



	def admit(self,patient):
		if len(self.patients) <= self.capacity:
			self.patients.append(patient)
			for i in range(0, len(self.beds)):
				if self.beds[i]["Available"]:
					patient.bed_num = self.beds[i]["bed_id"]
					self.beds[i]["Available"] = False 
					break 
			print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)

		else: 
			print "Sorry, The hospital is at full capacity"
		return self


	def discharge(self, patient_id):
		for patient in self.patients:
			if patient.id == patient_id:
				for bed in self.beds:
					if bed["bed_id"] == patient.bed_num:
						bed["Available"] = True 
						break 

				self.patients.remove(patient)
				return "Patient #{} succesfully discharged. Bed #{} now available".format(patient.id, patient.bed_num)
		return "Patient not found"


mike = Patient("Mike","cheese")
leo = Patient("Leo", "milk")
stan = Patient("Stan", "fruit")
barkley = Patient("Barkley", "wheat")
david = Patient("david","dairy")
mat = Patient("Lmat", "alchohol")
jacob = Patient("jacob", "flour")
noah = Patient("noah", "sugar")
yoenis = Patient("yoenis","grain")
daniel = Patient("daniel", "glutten")

elmhurtsHospital = Hospital("Elmhurt Hospital", 10)
elmhurtsHospital.admit(mike).admit(leo).admit(stan).admit(barkley).admit(daniel).admit(yoenis).admit(noah).admit(jacob).admit(mat).admit(david)

elmhurtsHospital.discharge(8)

#bed number 5 is free 




