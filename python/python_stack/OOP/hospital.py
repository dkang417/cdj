class Patient(object):
	Patient_Count = 0

	def __init__(self,  name, allergies):
		self.name = name
		self.allergies = allergies
		self.id = Patient.Patient_Count
		self.bed_num = None
		Patient.Patient_Count += 1
	def display_info(self):
		print "Name is {}, allergic to {}, patient id is {}, bed number is {}".format(self.name,self.allergies,self.id,self.bed_num)

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
				print "Patient #{} succesfully discharged. Bed #{} now available".format(patient.id, patient.bed_num)
		return "Patient not found"


mike = Patient("Mike","cheese")
leo = Patient("Leo", "milk")
stan = Patient("Stan", "fruit")
barkley = Patient("Barkley", "wheat")
david = Patient("David","dairy")
mat = Patient("Lmat", "alchohol")
jacob = Patient("Jacob", "flour")
noah = Patient("Noah", "sugar")
yoenis = Patient("Yoenis","grain")
daniel = Patient("Daniel", "glutten")

elmhurtsHospital = Hospital("Elmhurt Hospital", 10)
elmhurtsHospital.admit(mike).admit(leo).admit(stan).admit(barkley).admit(daniel).admit(yoenis).admit(noah).admit(jacob).admit(mat).admit(david)

elmhurtsHospital.discharge(8)

daniel.display_info()


