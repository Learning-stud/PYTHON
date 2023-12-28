import datetime

# DEFNE A CLASS FOR MANAGING VACCINATION REPORTS
class VaccinationReport:
      def __init__(self):

            # INITIALIZING ATTRIBUTES FOR TITLE

            self.title= " VACCINATION REPORT ".center(50)
            self.dash="-------------------------------------------------------------"

          #   METHOD TO GATHER PAITENT INFORMATION

      def input_paitent_info(self):

          # COLLECTING PAITENT DETAIL FROM USER INPUT

          name = input("Enter Name : => ")
          age = input("Enter Age : => ")
          contact = input("Enter Contact No : => ")
          Vaccine_Name = input("Enter Vaccine Name : => ")
          Vaccine_Dose= input("Enter Vaccine Dose : => ")


# CURRENT DATE AND TIME

          current_Date=datetime.date.today()
          current_Time=datetime.datetime.now().strftime("%H:%M:%S") #  string format time

# FORMATING PAITENT INFORMATION

          info=f"""
                \nName :::> {name}
                  Age :::> {age}
                  contact :::> {contact}
                  Vaccine-Name :::> {Vaccine_Name}
                  Vaccine-Dose :::>{Vaccine_Dose}
                """
# RETURNS  FORMATTED PAITENCT DATA

          return f"{self.dash}\nDate: {current_Date}\nTime{current_Time}\n{info}"

# METHOD TO SAVE PAITENCE DATA TO A FILE

      def SavingFile(self,Data):  # creating and parameter to write data

           FileName = f"{datetime.date.today()}.txt"   # creating file name using first datetime function and after that date and using today

          # OPENING THE FILE FOR APPENDIND
           with open(FileName,"a") as file:

                # CHECKING THE FILE FOR APPENDING
                FileRead = open(FileName,"r")
                if len(FileRead.readlines()) == 0:

                     # IF EMPTY WRITE THIS TITLE TO THE FILE [MEANS THE TILE VACCINATION REPORT ]
                     file.write(self.title + "\n")

                     # WRITTING PAITENCE DATA TO THE FILE
                file.write(Data)

                # METHOD TO CONTINUE THE PROCESS OF ADDING PAITIENTS

      def Continue_Process(self):
           status = True
           while status:
                # GETTING PAITINT INFORMATION

                Paitent_data = self.input_paitent_info()

                # SAVING PAITENCE DATA TO THE FILE

                self.SavingFile(Paitent_data)

               # ASKING THE USER IF HE OR SHE WANT TO CONTINUE

                Want_To_Continue = input("\n Do You Wanrt To Add Another Paitent ? [y/n]").casefold()  # casefold when perform case-insensitive strings

                    # IF THE RESPONSE IS Y OR YES EXIT THE LOOP

                if Want_To_Continue != "y" and Want_To_Continue != "yes":
                     status =  False

if __name__ == "__main__":


     # INSTANCE OF VACCINATION REPORT
     report = VaccinationReport()

     # RUNNING THE PROCESS TO ADD PAITIENTS
     report.Continue_Process()

     # THANK YOU
     print("----------------------- ' THANK YOU -- TAKE CARE -- BE VACCINIZED '   ---------------------------------")