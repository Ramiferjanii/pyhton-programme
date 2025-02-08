def is_leap(year):
    leap = False
    if (year % 4 == 0 ) and (year % 100 != 0 ) or (year % 400 == 0 ) :
        return True 
    
    return leap

year = int(input())
if is_leap() : 
    print(f"the year {year} is leap ")
else : 
    print(f"year is not leap ")
