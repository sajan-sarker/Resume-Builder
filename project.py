# Description: This file contains the code for the project.
from fpdf import FPDF

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
    contact(basic_details["phone_number"], basic_details["email"], basic_details["linkedin"])

    sec_header("Description:")
    paragraph(basic_details["description"])

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
    """
    name = input("Name: ")
    phone_number = input("Number: ")
    email = input("Email: ")
    address = input("Present Address: ")
    description = input("Description: ")
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
    basic_details = {
        "name": "John Doe",
        "phone_number": "123-456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main St, Anytown, USA",
        "description": "A Computer Science and Engineering (CSE) engineer is a professional who applies the principles of computer science and electrical engineering to design, develop, and maintain computer systems and software. They are skilled in programming languages, software development, algorithms, data structures, and hardware architecture. CSE engineers work on a wide range of technologies, including operating systems, databases, networks, and cybersecurity. They play a crucial role in advancing technology by creating innovative solutions for complex problems in various industries.",
        "linkedin": "https://www.linkedin.com/in/john-doe"
    }
    skills = ['Algorithms', 'Data Structures', 'Programming Languages (e.g., Python, C++, Java)', 'Software Development', 'Database Management', 'Operating Systems', 'Network Security', 'Machine Learning', 'Web Development', 'Cloud Computing']
    experience = [{"position": "Software Engineer", "date": "09/2015 to 05/2019", "company": "Luna Software, New York",
                   'details': [
                       "Investigation, design, and implement scalable applications for data identification, analysis, retrieval, and indexing.",
                       "Software design and development while remaining concentrate on client needs.",
                       "Estimate interface between hardware and software."]},
                  {"position": "Junior Software Engineer", "date": "09/2014 to 05/2015",
                   "company": "AdsPro Software, New York", 'details': [
                      "Consulted regularly with customers on project status, proposals and technical issues.",
                      "Transformed existing software to correct errors, upgrade interfaces, and improve efficiency."]}]

    education = [{"degree": "Computer Science & Engineering", "university": "North South University", "year": "2024",
                  "cgpa": "3.99"}]
    project = [{"name": "Eco Mart", "type": "Web app", "about": ["Used HTML, CSS, PHP, JavaScript, MySQL.",
                                                                 "It have admin panal, and employee panel, and basic user panel."]}]

    create_resume(basic_details, skills, experience, education, project)

    return 0

if __name__ == "__main__":
    main()