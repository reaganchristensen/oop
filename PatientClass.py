class Patient:

    def __init__(self, pid, pname, paddress, pphone, pvet):
        self.__patientID = pid
        self.__name = pname
        self.__address = paddress
        self.__phone = pphone
        self.__veteranstatus = pvet

    def get_pid(self):
        return self.__patientID
 
    def get_pname(self):
        return self.__name
    
    def get_paddress(self):
        return self.__address
    
    def get_pphone(self):
        return self.__phone
    
    def get_pvet(self):
        return self.__veteranstatus