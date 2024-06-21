# Description: This file contains the code for the project.
from fpdf import FPDF
import os

pdf = FPDF()    # Create a PDF object
pdf = FPDF(orientation="portrait", format="a4")   # Set the orientation and format of the page of the PDF file to be created.   
pdf.add_page()  # Add a page to the PDF file.

def header(name):
    """
    Add a header to the PDF document with the specified name.

    Parameters:
    - name (str): The name to be displayed in the header.

    Returns:
    None
    """
    pdf.set_font("Arial", "B", 22)
    pdf.cell(0, 10, name, 0, 1, "C")

def sub_header(address):
    """
    Displays a sub-header with the given address in the PDF document.

    Parameters:
    - address (str): The address to be displayed.

    Returns:
    - None
    """
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, address, 0, 0, "C")
    pdf.ln(8)

def contact(number, email, social_link):
    """
    Displays the contact information in the PDF in a box.

    Args:
        number (str): The phone number.
        email (str): The email address.
        social_link (str): The social media link.

    Returns:
        None
    """
    pdf.set_font("Arial", "", 10)
    pdf.set_fill_color(200,220,255)
    pdf.set_line_width(1)
    pdf.cell(0, 6, number +"                    "+ email +"                    "+ social_link, 0, 0, "C", True)
    pdf.ln(10)

def sec_header(header):
    """
    Sets the section header in the PDF document.

    Parameters:
    - header (str): The text to be displayed as the section header.

    Returns:
    - None
    """
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 6, header, 0, 0, "L")
    pdf.ln(6)

def body_header(name, data):
    """
    Adds a header to the body section of the resume.

    Parameters:
    - name (str): The name or title.
    - data (str): The data of employment or others.

    Returns:
    None
    """
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 6, name, 0, 0, "L")
    pdf.set_font("Arial", "", 9)
    pdf.cell(0, 0, data, 0, 0, "R")
    pdf.ln(5)

def body_sub_header(data):
    """
    Adds a sub-header to the body of the PDF document.

    Parameters:
    - data (str): The text to be displayed as the sub-header (Company or College name).

    Returns:
    - None
    """
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, data, 0, 0, "L")
    pdf.ln(9)

def print_body_sub_header(text):
    """
    Prints a sub-header in the body of the PDF document (show the cgpa).

    Parameters:
    text (str): The text to be printed as the sub-header.

    Returns:
    None
    """
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 0, text, 0, 0, "L")
    pdf.ln(6)

def print_bullet_point(details):
    """
    Prints a list of bullet points in a PDF document.

    Args:
        details (list): A list of strings representing the bullet points.

    Returns:
        None
    """
    pdf.set_font("Arial", "", 10)
    for detail in details:
        pdf.cell(0, 0, "- "+detail, 0, 0, "L")
        pdf.ln(6)

def paragraph(description):
    """
    Add a paragraph of text to the PDF document.

    Parameters:
    - description: str or list of str. The text to be added as a paragraph. If a list is provided, the elements will be joined with commas.

    Returns:
    None
    """
    pdf.set_font("Arial", "", 10)
    if type(description) == str:
        pdf.multi_cell(0, 5, description)
    else:
        description = ", ".join(description)+"."
        pdf.multi_cell(0, 5, description)
    pdf.ln(8)

def create_resume(basic_details, skills, experiences, education, projects):
    """
    Creates a resume PDF file based on the provided details.

    Args:
        basic_details (dict): A dictionary containing basic details such as name, address, phone number, email, and social link.
        skills (list): A list representing the skills section of the resume.
        experiences (list): A list of dictionaries representing the work experiences section of the resume.
        education (list): A list of dictionaries representing the education section of the resume.
        projects (list): A list of dictionaries representing the projects section of the resume.

    Returns:
        None

    Raises:
        None
    """
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
        body_header(project["name"], project["link"])
        body_sub_header(project["type"])
        print_bullet_point(project["about"])

    pdf.output("Resume.pdf")

def main():
    """
    The commented part of the code is the manual way to get the details of the user to create the resume.
    """
    """
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
    while True:
        name = input("Project Name: ")
        if name == "0":
            break
        type = input("Type: ")
        link = input("Link: ")
        about = []
        print("Enter About More than 4 (enter 0 to finish): ")
        while True:
            about_detail = input("About: ")
            if about_detail == "0":
                break
            about.append(about_detail)
        project.append({"name": name, "type": type, "about": about, "link": link})
    os.system('clear')
    """

    """
    Dummy data to create a resume.
    """
    basic_details = {
        "name": "Henry Ford",
        "phone_number": "123-456-7890",
        "email": "henry.ford@example.com",
        "address": "123 Main St, Anytown, USA",
        "summery": "Proficient junior engineer with 1 year of experience in designing, developing, and implementing software application. Utilize Java, C#, and Python to write scalable, secure code with a knack for problem-solving. Successfully optimized a software program resulting in a 30% efficiency increase.",
        "social_link": "https://www.linkedin.com/in/henry.ford/"
    }
    skills = ['Algorithms', 'Data Structures', 'Programming Languages (e.g., Python, C, C++, Java, C#, PHP, .NET, JavaScript)', 'Software Development', 
              'Database Management', 'Operating Systems', 'Network Security', 'Machine Learning', 'Web Development', 'Cloud Computing', 'Mobile Development', 
              'Agile Methodologies', 'DevOps', 'UI/UX Design', 'Project Management', 'Technical Support', 'Troubleshooting', 'Testing', 'Debugging', 'Documentation']

    experience = [{"position": "Software Engineer", "date": "06/2019 to Present", "company": "Tech Solutions, New York",
                   'details': [
                       "Design, develop, and implement software applications for data identification, analysis, retrieval, and indexing.",
                       "Collaborate with clients to understand requirements and provide technical support.",
                       "Optimize software programs to increase efficiency by 30%.",
                       "Create scalable applications that are optimized for the web."]},
                  {"position": "Software Engineer", "date": "09/2015 to 05/2019", "company": "Luna Software, New York",
                   'details': [
                       "Investigation, design, and implement scalable applications for data identification, analysis, retrieval, and indexing.",
                       "Software design and development while remaining concentrate on client needs.",
                       "Estimate interface between hardware and software.",
                       "Collaborate with clients to understand requirements and provide technical support."]},]
    
    education = [{"degree": "Bachelor of Science in Computer Science", "university": "New York University", "year": "2012 to 2016", "cgpa": "3.8"}]

    project = [{"name": "Eco Mart", "type": "Web app", "link": "https://ecomart.com/",
                "about": ["Used HTML, CSS, PHP, JavaScript, MySQL.",
                          "It have admin panal, and employee panel, and basic user panel.",
                          "It is a web application that allows users to buy and sell products online."]},
               {"name": "Social Media App", "type": "Mobile app", "link": "www.socialmediaapp.com",
                "about": ["Used Java, Android Studio, Firebase.",
                          "It is a mobile application that allows users to connect and share photos and videos.",
                          "Implemented push notifications and user authentication."]}]

    create_resume(basic_details, skills, experience, education, project)
    return 0

if __name__ == "__main__":
    main()