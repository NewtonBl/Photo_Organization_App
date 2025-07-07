import os
from pathlib import Path


# Function to convert numeric month to string value
def convert_month(month):
    match month:
        case "01":
            return "January"
        case "02":
            return "February"
        case "03":
            return "March"
        case "04":
            return "April"
        case "05":
            return "May"
        case "06":
            return "June"
        case "07":
            return "July"
        case "08":
            return "August"
        case "09":
            return "September"
        case "10":
            return "October"
        case "11":
            return "November"
        case "12":
            return "December"
        case _:
            return "Unknown Month"


# Function to create directory if it does not exist
def create_dir(p: str):
    os.makedirs(p, exist_ok=True)


# Main Function to sort photos
def sort(folder):

    # Set directory 
    directory = folder
    dir = Path(folder)

    # Begin iterating through files
    for file in dir.iterdir():

        # Verify that object is a file, not a directory
        if file.is_file():

            # Initial attempt if file name starts with a date
            try:
                year = int(file.name[:4])
                month = convert_month(file.name[4:6])
                new_dir = f"{directory}/{year}/{month}"
                create_dir(new_dir)
                file.rename(f"{new_dir}/{file.name}")

            # If file does not start with a date, check if starts with "Resized_"
            # If so, move file based on that format
            # If no integer where expected, try to move to "Unknown Date"
            # If already exists in "Unknown Date", move to "Potential Duplicates"
            # If exists in "Potential Duplicates", continue to next file
            except ValueError as e:
                if file.name.startswith("Resized"):
                    try:
                        year = int(file.name[8:12])
                        month = convert_month(file.name[12:14])
                        new_dir = f"{directory}/{year}/{month}"
                        create_dir(new_dir)
                        file.rename(f"{new_dir}/{file.name}")
                    except:
                        new_dir = f"{directory}/Unknown Date"
                        create_dir(new_dir)
                        try:
                            file.rename(f"{new_dir}/{file.name}")
                        except FileExistsError as e:
                            try:
                                new_dir = f"{directory}/Potential Duplicates"
                                create_dir(new_dir)
                                file.rename(f"{new_dir}/{file.name}")
                            except:
                                continue

            # If file alerady exists in the target directory, move to "Potential Duplicates"
            # If the file already exists in "Potential Duplicates", continue to next file
            except FileExistsError as e:
                try:
                    new_dir = f"{directory}/Potential Duplicates"
                    create_dir(new_dir)
                    file.rename(f"{new_dir}/{file.name}")
                except:
                    continue