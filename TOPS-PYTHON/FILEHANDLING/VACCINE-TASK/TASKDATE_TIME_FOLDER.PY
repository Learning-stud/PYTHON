import datetime


class VaccinationReport:
      def __init__(self):
            self.title= " VACCINATION REPORT ".center(50)
            self.dash="-------------------------------------------------------------"
      def input_paitent_info(self):
          name = input("Enter Name : => ")
          age = input("Enter Age : => ")
          contact = input("Enter Contact No : => ")
          Vaccine_Name = input("Enter Vaccine Name : => ")
          Vaccine_Dose= input("Enter Vaccine Dose : => ")


          current_Date=datetime.date.today()
          current_Time=datetime.datetime.now().strftime("%H:%M:%S") #  string format time

          info=f"""
                \nName :::> {name}
                  Age :::> {age}
                  contact :::> {contact}
                  Vaccine-Name :::> {Vaccine_Name}
                  Vaccine-Dose :::>{Vaccine_Dose}
                """
          return f"{self.dash}\nDate: {current_Date}\nTime{current_Time}\n{info}"

      def SavingFile(self,Data):  # creating and parameter to write data
           FileName = f"{datetime.date.today()}.txt"   # creating file name using first datetime function and after that date and using today creating todays date and time
           with open(FileName,"a") as file:   # data will be added to the file at end
                FileRead = open(FileName,"r")
                if len(FileRead.readlines()) == 0:
                     file.write(self.title + "\n")
                file.write(Data)
      def Continue_Process(self):
           status = True
           while status:
                Paitent_data = self.input_paitent_info()
                self.SavingFile(Paitent_data)
                Want_To_Continue = input("\n Do You Wanrt To Add Another Paitent ? [y/n]").casefold()  # casefold when perform case-insensitive strrings comperision diffrent language character or special characcter
                if Want_To_Continue != "y" and Want_To_Continue != "yes":
                     status =  False

if __name__ == "__main__":
     report = VaccinationReport()
     report.Continue_Process()
     print("-----------------------THANK YOU---------------------------------")