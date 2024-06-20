# Description: This file contains the code for the project.
from fpdf import FPDF

#def create_resume(basic_details, skills, experience, education, projects):

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
def contact(number, email, linkedin):
    pdf.set_font("Arial", "", 10)
    pdf.set_fill_color(200,220,255)
    pdf.set_line_width(1)
    pdf.cell(0, 6, number +"                    "+ email +"                    "+ linkedin, 0, 0, "C", True)
    pdf.ln(10)

def sec_header(header):
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 6, header, 0, 0, "L")
    pdf.ln(8)

def paragraph(description):
    pdf.set_font("Arial", "", 10)
    if type(description) == str:
        pdf.multi_cell(0, 5, description)
    else:
        description = ", ".join(description)+"."
        pdf.multi_cell(0, 5, description)


    pdf.ln(8)

def create_resume(basic_details, skills):
    header(basic_details["name"])
    sub_header(basic_details["address"])
    contact(basic_details["phone_number"], basic_details["email"], basic_details["linkedin"])
    sec_header("Description:")
    paragraph(basic_details["description"])
    sec_header("Skills: ")
    paragraph(skills)

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
        "phone_number": "123-456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main St, Anytown, USA",
        "description": "A Computer Science and Engineering (CSE) engineer is a professional who applies the principles of computer science and electrical engineering to design, develop, and maintain computer systems and software. They are skilled in programming languages, software development, algorithms, data structures, and hardware architecture. CSE engineers work on a wide range of technologies, including operating systems, databases, networks, and cybersecurity. They play a crucial role in advancing technology by creating innovative solutions for complex problems in various industries.",
        "linkedin": "https://www.linkedin.com/in/john-doe"
    }
    skills = ['Algorithms', 'Data Structures', 'Programming Languages (e.g., Python, C++, Java)', 'Software Development', 'Database Management', 'Operating Systems', 'Network Security', 'Machine Learning', 'Web Development', 'Cloud Computing']
    experience =

    create_resume(basic_details, skills)

    return 0

if __name__ == "__main__":
    main()