s1 = float(input("Enter subject1 total mark: "))
s2 = float(input("Enter subject2 total mark: "))
s3 = float(input("Enter subject3 total mark: "))

Total = float(s1)+float(s2)+float(s3)

sg1 = float(input("Enter subject1 mark of the student: "))
sg2 = float(input("Enter subject2 mark of the student: "))
sg3 = float(input("Enter subject3 mark of the student: "))

Total_get = float(sg1)+float(sg2)+float(sg3)

cal_m1 = float(s1*0.33)
cal_m2 = float(s2*0.33)
cal_m3 = float(s3*0.33)

Toatl_cal = float(Total*0.4)

if(sg1 > cal_m1 and sg2>cal_m2 and sg3>cal_m3 and Total_get>Toatl_cal):
    print("Student is passed")
else:
    print("Student is failed")