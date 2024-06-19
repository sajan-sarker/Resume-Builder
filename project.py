# Description: This file contains the code for the project.
from fpdf import FPDF

def create_resume(basic_details, skills, experience, education, projects):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Resume", ln=True, align="C")

    create_section("Basic Details", "")
    create_line()
    create_box("Name: " + basic_details["name"])
    create_box("Phone Number: " + basic_details["phone_number"])
    create_box("Email: " + basic_details["email"])
    create_box("Address: " + basic_details["address"])
    create_box("Motivation: " + basic_details["motivation"])

    create_section("Skills", "")
    create_line()
    for skill in skills:
        create_box(skill)

    create_section("Experience", "")
    create_line()
    for exp in experience:
        create_box("Company: " + exp["company"])
        create_box("Position: " + exp["position"])
        create_box("Description: " + exp["description"])

    create_section("Education", "")
    create_line()
    for edu in education:
        create_box("School/ University: " + edu["school"])
        create_box("Degree: " + edu["degree"])
        create_box("Major: " + edu["major"])
        create_box("CGPA: " + edu["cgpa"])

    create_section("Projects", "")
    create_line()
    for project in projects:
        create_box("Project: " + project["project"])
        create_box("Link: " + project["link"])
        create_box("Description: " + project["project_description"])

    pdf.output("resume.pdf")

def create_box(text):
    ...

def create_section(title, content):
    ...

def create_line():
    ...

def main():
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

    create_resume(basic_details, skills, experience, education, projects)

    return 0

if __name__ == "__main__":
    main()