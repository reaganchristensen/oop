import PatientClass as PatC
import ProcedureClass as ProC

def main():
    
   currentpid = 1
   currentname = 'Matt Jones'
   currentaddress = '123 Main St, Waco TX 76706'
   currentphone = "254-555-7415"
   currentstatus = input('Is the patient a veteran? TRUE or FALSE ')

   # Create a patient object
   currentpatient = PatC.Patient(currentpid, currentname, currentaddress, currentphone, currentstatus)
   
   pro1name = 'Physical Exam'
   pro1date = '2/15/2022'
   doc1name = 'Dr. Irvine'
   charge1 = 250
   currentpid = 1
   
   pro2name = 'MRI'
   pro2date = '2/15/2022'
   doc2name = 'Dr. Hamilton'
   charge2 = 1500
   currentpid = 1

   pro3name = 'CT Scan'
   pro3date = '2/17/2022'
   doc3name = 'Dr. Drey'
   charge3 = 1200
   pid2 = 2

   # Create the procedure objects
   procedure1 = ProC.Procedure(pro1name, pro1date, doc1name, charge1, currentpid)
   
   procedure2 = ProC.Procedure(pro2name, pro2date, doc2name, charge2, currentpid)

   procedure3 = ProC.Procedure(pro3name, pro3date, doc3name, charge3, pid2)

   
   print('*** Patient Bill ***')
   print(f'Name: {currentpatient.get_pname()}')
   print(f'Address: {currentpatient.get_paddress()}')
   print(f'Phone: {currentpatient.get_pphone()}')

   print(f'Procedure: {procedure1.get_proname()}')
   print(f'Date: {procedure1.get_prodate()}')
   print(f'Practitioner: {procedure1.get_docname()}')
   print('Charge: $', format(procedure2.get_charge(), ',.2f'), sep = '')
   
   print(f'Procedure: {procedure2.get_proname()}')
   print(f'Date: {procedure2.get_prodate()}')
   print(f'Practitioner: {procedure2.get_docname()}')
   print('Charge: $', format(procedure2.get_charge(), ',.2f'), sep = '')

   if currentstatus == "TRUE":
     print('Total Charges: $', format((procedure1.get_charge() + procedure2.get_charge())* .6, ',.2f'), sep = '')
   else:
     print('Total Charges: $', format(procedure1.get_charge() + procedure2.get_charge(), ',.2f'), sep = '')
   
# Call the main function.
main()