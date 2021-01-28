import csv
def write_into_csv(info_list):
    with open ('student_info.csv' , 'a' , newline = '') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()== 0:
                 
            writer.writerow(["Name" , "Age" , "Contact Number" , "E-Mail ID"])
        
        writer.writerow(info_list)
        
if __name__ == '__main__':
    condition = True 
    student_num = 1
    

    while (condition):
        a = input("Enterinformation for student #{} in the following format (Name Age Phone_Number Email_Id)".format(student_num))
                       
        student_list= a.split(" ")
        print("\n The entered information is - \n Name: {} \n Age: {} \n Contact Number: {} \n E-Mail_ID: {}".format(student_list[0], student_list[1], student_list[2] , student_list[3]))
        
        choice_check = input("Is the information entered above correct? (yes/no)")
        
        if choice_check == "yes":
            write_into_csv(student_list)
    
            b = input("Do you want to add another student's info(yes/no)?")
    
            if b == "yes":
                condition= True
                student_num= student_num + 1 
                
            elif b == "no":
                condition = False
        elif choice_check == "no":
            print("\n Please re-enter the values!")