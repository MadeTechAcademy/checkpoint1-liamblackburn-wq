import os
import tkinter as tk
from tkhtmlview import HTMLLabel

duties_list = [
    {
        "name": "Bootcamp",
        "duties": [
            "Duty 1 - Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
            "Duty 2 - Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
            "Duty 3 - Engage in productive pair/mob programming to underpin the practice of peer review.",
            "Duty 4 - Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
            "Duty 13 - Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
            ]
    },

    {
        "name": "Automate!",
        "duties": [
            "Duty 5 - Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
            "Duty 7 - Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers). Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
            "Duty 10 - Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable."     
        ]
    },

    {
        "name": "Houston, Prepare to Launch",
        "duties": [
            "Duty 6 - Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
            "Duty 7 - Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers). Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
            "Duty 10 - Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
            "Duty 12 - Look to automate any manual tasks that are repeated, often using APIs."
        ]
    },

    {
        "name": "Going Deeper",
        "duties": [
            "Duty 11 - Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications."
        ]
    },

    {
        "name": "Assemble!",
        "duties": [
            "Duty 8 - Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance."
        ]
    },

    {
        "name": "Call Security",
        "duties": [
            "Duty 9 - Apply leading security practices throughout the Software Development Lifecycle (SDLC)."
        ]
    }
]

def display_duties_to_console():
    for duty in duties_list:
        print("{0}\n".format(duty))

def read_html(html_file):
    with open(html_file, "r", encoding="utf-8") as duties_file:
        return duties_file.read()
    
def save_duties_to_html(duties, filename="duties.html"):
    with open(filename, "w", encoding="utf-8") as duties_file:
        duties_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Apprentice Duties</title>\n</head>\n<body>\n")
        duties_file.write("  <header>\n")
        duties_file.write("    <h1>Apprentice Duties</h1>\n")
        duties_file.write("  </header>\n")

        for theme in duties:
            theme_name = theme["name"]
            duties_file.write(f"      <h2>{theme_name}</h2>")
            duties_file.write("\n        <ul>\n")
            for duty in theme["duties"]:
                duties_file.write(f"          <li>{duty}</li>\n")
            duties_file.write("        </ul>\n")
        duties_file.write("</body>\n</html>")

def save_theme_to_html(name, duties, filename=None):
    if filename is None:
        filename = f"{name}.html"

    with open(filename, "w", encoding="utf-8") as theme_file:
        theme_file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{name}</title>\n</head>\n<body>\n")
        theme_file.write("  <header>\n")
        theme_file.write(f"    <h1>{name}</h1>\n")
        theme_file.write("  </header>\n")
        theme_file.write("\n    <ul>\n")
        for duty in duties:
            theme_file.write(f"      <li>{duty}</li>\n")
        theme_file.write("    </ul>\n")
        theme_file.write("</body>\n</html>")        
                
def extract_themes_from_html(html_file, output_dir=None):
    current_theme = {}
    with open(html_file, "r", encoding="utf-8") as duties_file:
        for line in duties_file:
            if "<h2>" in line:
                theme_name = line.replace("<h2>", "").replace("</h2>", "").strip()
                current_theme[theme_name] = []
                active_theme = theme_name
            elif "<li>" in line:
                duty_text = line.replace("<li>", "").replace("</li>", "").strip()
                current_theme[active_theme].append(duty_text)
        for name, duties in current_theme.items():
            if output_dir:
                save_theme_to_html(name, duties, output_dir / f"{name}.html")
            else:
                save_theme_to_html(name, duties)
    return current_theme

# gui logic

root = tk.Tk()
root.title("Apprentice Duty Library")
root.geometry("1080x1920")

label = tk.Label(root, text="Welcome to your apprentice duty library!", font=("Arial", 16))
label.pack(pady=20)

html_label = HTMLLabel(root, html="<h1>Would you like to display or download your duties?</h1>")
html_label.pack(pady=20, fill="both")

def display_duties():
    save_duties_to_html(duties_list, "duties.html")
    with open("duties.html", "r", encoding="utf-8") as duties_file:
        html_content = duties_file.read()

    html_label.set_html(html_content)

button = tk.Button(root, text='Display Duties', command=display_duties)
button.pack(pady=10)

root.mainloop()

if __name__=="__main__":
    choice = input("""
    Welcome to apprentice themes!\n
    Press (1) to display the apprenticeship duties in the console.\n
    Press (2) to save duties to an HTML file.\n
    Press (3) to extract themes from generated HTML file and save each theme separately.\n
    Press (4) to save a single theme by name.\n
    Enter your choice:
    """)
    if choice == "1":
        display_duties_to_console()

    elif choice == "2":
        save_duties_to_html(duties_list)
        duties_file_created = True
        print("Duties saved to duties.html")

    elif choice == "3":
        if os.path.exists("duties.html"):
            themes = extract_themes_from_html("duties.html")
            print("Themes extracted and saved")
        else:
            print("Please generate duties first with option 2 before extracting themes")

    elif choice == "4":
        theme_name = input("Enter the theme name: ")
        for theme in duties_list:
            if theme["name"].lower() == theme_name.lower():
                save_theme_to_html(theme["name"], theme["duties"])
                print(f"Saved {theme['name']} to {theme['name']}.html")
                break
        else:
            print("Theme not found.")
    else:
        print("Invalid choice. Please select option 1, 2, 3 or 4")