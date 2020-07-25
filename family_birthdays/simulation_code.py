from datetime import date
from operator import itemgetter

def execute_simulation(inputs, n=3):
    """Function that returns the n closest birthdays.
    
    :param inputs: The dictionary with names and birthdates.
    :type x_max: dict
    :return: Dictionary with the results of the simulation
    :rtype: dict
    """
    today = date.today()
    computed_days_and_ages = []        
    for who, borndate_str in inputs["birthdates"].items():
        isoformat_str = "-".join(borndate_str.split("-")[::-1])
        borndate = date.fromisoformat(isoformat_str)
        d2b = calculate_days_to_birthday(today, borndate)
        age = calculate_age(today, borndate)
        computed_days_and_ages.append([who, d2b, age])
    # Sort
    sorted_list = sorted(computed_days_and_ages, key = itemgetter(1))
    # Print
    for who, days, age in sorted_list[:n]:
        print(f"{who} tiene cumpleaños en {days} días más y cumple {age} años.")
    # Pack the outputs, in case we want to check them later
    outputs = {"computed_days_and_ages":computed_days_and_ages}
    return outputs

def calculate_days_to_birthday(today, born):
    """Function that computes the days to the birthday

    :param born: [description]
    :type born: [type]
    :return: [description]
    :rtype: [type]
    """
    # Use current year for the birthday
    birthday = date(today.year, born.month, born.day)
    days_to_birthday = (birthday - today).days
    if days_to_birthday>=0:
        return days_to_birthday
    else:
        birthday = date(today.year + 1, born.month, born.day)
        days_to_birthday = (birthday - today).days
        return days_to_birthday

def calculate_age(today, born):
    """Function that computes the age given  
    todays date and born (birth) date.
    Based on: https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python

    :param born: [description]
    :type born: [type]
    :return: [description]
    :rtype: [type]
    """
    years =  today.year - born.year 
    adjustment = ((today.month, today.day) < (born.month, born.day))
    return years - adjustment

if __name__=="__main__":
    birthdates = {"Captain America":"04-07-1918",
                  "Ironman":"29-05-1970",
                  "Spiderman":"10-08-2001",
                  "Batman":"17-04-1915",
                  "Hulk":"18-12-1969",
    }
    execute_simulation({"birthdates":birthdates})
    """
    today = date.today()
    birthdate = date.fromisoformat('1982-07-25')
    years = calculate_age(today, birthdate)
    print(years)
    d2b = calculate_days_to_birthday(today, birthdate)
    print(d2b)
    """