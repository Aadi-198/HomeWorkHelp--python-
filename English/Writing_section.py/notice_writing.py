import shutil # A module to get curren terminal_length anc do more
import inspect # This is to resolve the """triple code in ef indentation issue"""
import time
import datetime

size = shutil.get_terminal_size() # Get size
half_width = int(size.columns / 2)
seps = "-" * size.columns # Make separators according to the terminal size

def notice():
    time.sleep(0.1)
    organisation = input("Name of orgainsation : ")
    time.sleep(0.1)
    city = input("Name of city : ")
    time.sleep(0.1)
    header = f"{organisation}, {city}"
    t_date = datetime.datetime.now().date()
    time.sleep(0.1)
    title = input("Title : ")
    time.sleep(0.1)
    people = input("Who do you want to inform ? ")
    time.sleep(0.1)
    why = input("Why is the event being organised ? [In one word] ")
    time.sleep(0.1)
    event_date = input("On which date will the event take place ? ")
    time.sleep(0.1)
    formatted_date = f"Date : {event_date}"
    time.sleep(0.1)
    c_time = input("What is the time of event ? ")
    formatted_time = f"Time : {c_time}"
    time.sleep(0.1)
    venue = input("Where will the event take place ? ")
    formatted_venue = f"Venue : {venue}"
    time.sleep(0.1)
    register = input("Phone number / email id to register : ")
    time.sleep(0.1)
    r_date = input(f"By when should {people} register ? ")
    while True:
        time.sleep(0.1)
        optional = input("Is the event optional ? [Y]es or [N]o ").strip().lower()
        if optional == "y":
            fill = f"Interested {people} may register at {register} by {r_date}."
            break
        elif optional == "n":
            fill = f"All the {people} are required to participate and regiter at {register} by {r_date}."
            break
        else:
            print("Error! Try again")
    support = input(f"Where should {people} contact for additional support ? ")
    name = input(f"What is the name of the speciman wring the notice ? ")
    sign = f"{name}/{t_date}"
    designation = input("What is your designation ? ")

    print(seps)
    
    writing = f"""
    {header:^{size.columns}}
    {"NOTICE":^{size.columns}}
    {t_date:<{half_width}}
    {title:^{size.columns}}

    {f"This is to inform the {people} that a {title.lower()} is being organised on the occasion of {why} following the given schedule -"}

    {formatted_date:^{size.columns}}{formatted_time:^{size.columns}}{formatted_venue:^{size.columns}}

    {fill}
    For further information contact with {support} or the undersigned.
    
    {name}
    {sign}
    {designation}
    """
    writing = inspect.cleandoc(writing)

    time.sleep(0.8)
    print(writing)
 
if __name__ == "__main__":
    notice()