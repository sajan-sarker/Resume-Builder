# Description: This file contains the code for the project.
from fpdf import FPDF

#def create_resume(basic_details, skills, experience, education, projects):

pdf = FPDF()
pdf = FPDF(orientation="portrait", format="a4")
pdf.add_page()
def header(name):
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, name, 0, 1, "C")
def sub_header(title):
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 10, title, 0, 0, "C")

def create_resume(basic_details):
    header(basic_details["name"])
    sub_header(basic_details["position"])
    pdf.output("Resume.pdf")


    #pdf.set_font("Arial","B", size=13)
    #pdf.cell(200, 10, basic_details[0], ln=True, align="C")
    """
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Resume", ln=True, align="C")

    create_section("Basic Details", "")
    create_line()
    create_box("Name: " + basic_details["name"])
    create_box("Phone Number: " + basic_details["phone_number"])
    create_box("Email: " + basic_details["email"])
    create_box("Address: " + basic_details["address"])
    create_box("Motivation: " + basic_details["motivation"])
    """


def create_box(text):
    ...

def create_section(title, content):
    ...

def create_line():
    ...

def main():
    """
    name = input("Name: ")
    phone_number = input("Number: ")
    email = input("Email: ")
    address = input("Present Address: ")
    motivation = input("Motivation: ")
    basic_details = {"name": name, "phone_number": phone_number, "email": email, "address": address, "motivation": motivation}

    skills = []
    print("Enter Skills (press 0 to finish): ")
    while True:
        skill = input("Skill: ")
        if skill == "0":
            break
        skills.append(skill)

    experience = []
    print("Enter Experience Details (press 0 to finish): ")
    while True:
        company = input("Company: ")
        if company == "0":
            break
        position = input("Position: ")
        description = input("Description: ")
        experience.append({"company": company, "position": position, "description": description})

    education = []
    print("Enter Education Details (press 0 to finish): ")
    while True:
        school = input("School/ University: ")
        if school == "0":
            break
        degree = input("Degree: ")
        major = input("Major: ")
        cgpa = input("CGPA: ")
        education.append({"school": school, "degree": degree, "major": major, "cgpa": cgpa})

    projects = []
    print("Enter Projects (press 0 to finish): ")
    while True:
        project = input("Project Title: ")
        if project == "0":
            break
        link = input("Link: ")
        project_description = input("Description: ")
        projects.append({"project": project, "link": link, "project_description": project_description})
    """
    #create_resume(basic_details, skills, experience, education, projects)
    basic_details = {
        "name": "John Doe",
        "position": "Python Developer",
        "phone_number": "123-456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main St, Anytown, USA",
        "motivation": "I am passionate about... etc."
    }
    create_resume(basic_details)

    return 0

if __name__ == "__main__":
    main()