# MAKING A AGE CALCULATOR USING "DEF FUNCTION", "IF AND ELSE" AND "DATE-TIME MODULE"

# IMPORT DATE AND DATETIME FROM THE MODULE "DATETIME"
from datetime import date , datetime

# MAKING THE FUNCTION TO CALCULATE THE YEAR OF THE USER AGE
def year():
    year = date_today.year - date_dob.year
    return year

# FUNCTION TO CALCULATE THE MONTH OF THE USER AGE
# IF THE CURRENT MONTH IS GREATER THAN THE USER DOB
def month_today():
    month_today = date_today.month - date_dob.month
    return month_today

# FUNCTION TO CALCULATE THE MONTH OF THE USER AGE
# IF THE DOB IS GREATER THE THE CURRENT MONTH
def month_dob():
    month_dob = date_dob.month - date_today.month
    return month_dob

# FUNCTION TO CALCULATE THE DAY OF THE USER AGE
# IF THE CURRENT DAY IS GREATER THEN THE USER DOB
def day_today():
    day_today = date_today.day - date_dob.day
    return day_today

# FUNCTION TO CALCULATE THE DAY OF THE USER AGE
# IF THE DOB OF THE USER IS GREATER THAN THE CURRENT AGE
def day_dob():
    day_dob = date_dob.day - date_today.day
    return day_dob
    

# TAKING USER DATE OF BIRTH FORM THE USER
date_input = input("Enter your date of birth in (dd/mm/yyyy): ")

# CONVERTING INPUT DOB TAKEN FROM THE USER INTO DATE-TIME FORMAT
date_dob = date.strptime(date_input, "%d/%m/%Y")

# FINDING THE TODAY'S DATE TO CALCULATE THE AGE (USING TODAY() FUNCTION)
date_today = date.today()

# print(date.today().year)
# print(date_dob)


# ASSIGNING MULTIPLE CONDITION TO CALCULATE THE AGE OF THE USER
# ALL THE CONDITION IS ASSIGNED IS FOR DAY AND MONTH
if date_dob.year < date_today.year:
    if date_today.year > date_dob.year:
        print(f"{year()} year"," ", end="")
    else:
        print("Given date is invalid. Please enter a valid date")
        
    if date_today.month > date_dob.month:
        print(f"{month_today()} month"," " ,  end=" ")
    else:
        print(f"{month_dob()} month"," " , end=" ")
        
    if date_today.day > date_dob.day:
        print(f"{day_today()} day"," ", end=" ")
    else:
        print(f"{day_dob()} day"," ", end=" ")

else:
    print("Incorrect Date")

# print(date.today())
# print(datetime.now().time())