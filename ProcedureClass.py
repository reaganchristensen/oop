class Procedure:

    def __init__(self, proname, prodate, docname, charge, pid):
        self.__procedure = proname
        self.__proceduredate = prodate
        self.__doctorname = docname
        self.__charge = charge
        self.__patientID = pid

    def get_proname(self):
        return self.__procedure

    def get_prodate(self):
        return self.__proceduredate

    def get_docname(self):
        return self.__doctorname
    
    def get_charge(self):
        return self.__charge

    def get_pid(self):
        return self.__patientID
 