
def write_info_file():

    f= open("C:/Users/HOME/Documents/Python Scripts/admission.txt","a")
    f.write(str(student_info_list))
    f.write("\n")
    f.close()

condition = True
while(condition):
  student_info=input("Enter some student information in the following format (Name Age Phone_no E-mail_ID): ")
  print("Entered information " + student_info)
  #split
  student_info_list =  student_info.split(" ")
  print("Entered split up information is: " + str(student_info_list))
  
  write_info_file()

  
  condition_check=input("Enter (yes/no) if you want to enter the information of another student")
  if condition_check=="yes":
      condition = True
  elif condition_check=="no":
      condition = False
