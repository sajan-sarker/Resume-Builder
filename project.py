# Description: This file contains the code for the project.
from fpdf import FPDF
import os

pdf = FPDF()
pdf = FPDF(orientation="portrait", format="a4")
pdf.add_page()

def header(name):
    pdf.set_font("Arial", "B", 22)
    pdf.cell(0, 10, name, 0, 1, "C")

def sub_header(address):
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, address, 0, 0, "C")
    pdf.ln(8)

def contact(number, email, social_link):
    pdf.set_font("Arial", "", 10)
    pdf.set_fill_color(200,220,255)
    pdf.set_line_width(1)
    pdf.cell(0, 6, number +"                    "+ email +"                    "+ social_link, 0, 0, "C", True)
    pdf.ln(10)

def sec_header(header):
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 6, header, 0, 0, "L")
    pdf.ln(6)

def body_header(position, date):
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 6, position, 0, 0, "L")
    pdf.set_font("Arial", "", 9)
    pdf.cell(0, 0, date, 0, 0, "R")
    pdf.ln(5)

def body_sub_header(company):
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, company, 0, 0, "L")
    pdf.ln(9)

def print_body_sub_header(text):
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 0, text, 0, 0, "L")
    pdf.ln(6)

def print_bullet_point(details):
    pdf.set_font("Arial", "", 10)
    for detail in details:
        pdf.cell(0, 0, "- "+detail, 0, 0, "L")
        pdf.ln(6)

def paragraph(description):
    pdf.set_font("Arial", "", 10)
    if type(description) == str:
        pdf.multi_cell(0, 5, description)
    else:
        description = ", ".join(description)+"."
        pdf.multi_cell(0, 5, description)
    pdf.ln(8)

#def create_resume(basic_details, skills, experience, education, projects):
def create_resume(basic_details, skills, experiences, education, projects):
    header(basic_details["name"])
    sub_header(basic_details["address"])
    contact(basic_details["phone_number"], basic_details["email"], basic_details["social_link"])

    sec_header("Summery:")
    paragraph(basic_details["summery"])

    sec_header("Skills: ")
    paragraph(skills)

    sec_header("Experiences: ")
    for job in experiences:
        body_header(job["position"], "Year: "+job["date"])
        body_sub_header(job["company"])
        print_bullet_point(job["details"])

    sec_header("Education: ")
    for edu in education:
        body_header(edu["university"], "Year: "+edu["year"])
        body_sub_header(edu["degree"])
        print_body_sub_header("CGPA: "+edu["cgpa"])
    project = [{"name": "Eco Mart", "type": "Web app", "about": ["Used HTML, CSS, PHP, JavaScript, MySQL.",
                                                                 "It have admin panal, and employee panel, and basic user panel."]}]

    sec_header("Projects: ")
    for project in projects:
        body_header(project["name"], "")
        body_sub_header(project["type"])
        print_bullet_point(project["about"])

    pdf.output("Resume.pdf")

def main():
    # Get the basic details of the user to create the resume.
    print("Enter your contact information (required)*: ")
    name = input("Name: ")
    phone_number = input("Number: ")
    email = input("Email: ")
    address = input("Present Address: ")
    social_link = input("Github/LinkedIn: ")
    summery = input("Summery: ")
    basic_details = {"name": name, "phone_number": phone_number, "email": email, "address": address, "social_link": social_link, "summery": summery}
    os.system('clear')
    
    # Get the skills, experience, education and project details of the user to create the resume.
    skills = []
    print("Enter Skills More than 20 (enter 0 to finish) (required)**: ")
    while True:
        skill = input("Skill: ")
        if skill == "0":
            break
        skills.append(skill)
    os.system('clear')

    experience = []
    print("Enter Experience Details Minimum 2 (enter 0 to company name to finish) (required)**: ")
    while True:
        company = input("Company Name: ")
        if company == "0":
            break
        position = input("Position: ")
        date = input("Date: ")
        details = []
        print("Enter Details More than 4 (enter 0 to finish): ")
        while True:
            detail = input("Detail: ")
            if detail == "0":
                break
            details.append(detail)
        experience.append({"company": company, "position": position, "date": date, "details": details})
    os.system('clear')

    education = []
    print("Enter Education Details (enter 0 to degree to finish) (required)***: ")
    while True:
        degree = input("Degree: ")
        if degree == "0":
            break
        university = input("College/University: ")
        year = input("Year: ")
        cgpa = input("CGPA: ")
        education.append({"degree": degree, "university": university, "year": year, "cgpa": cgpa})
    os.system('clear')

    project = []
    print("Enter Project Details (enter 0 to project name to finish)(required)**: ")
    name = input("Project Name: ")
    type = input("Type: ")
    about = []
    print("Enter About More than 4 (enter 0 to finish): ")
    while True:
        about_detail = input("About: ")
        if about_detail == "0":
            break
        about.append(about_detail)
    project.append({"name": name, "type": type, "about": about})
    os.system('clear')


    create_resume(basic_details, skills, experience, education, project)
    return 0

if __name__ == "__main__":
    main()