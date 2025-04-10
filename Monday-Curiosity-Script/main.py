#!/usr/bin/python3
"""
    This Module is used to Send Curiosity monday Messages
"""

#!/usr/bin/env python3
from dotenv import load_dotenv
from os import getenv
from google import genai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

PROMPT = '''
Context:
Favour is a 25-year-old mechanical engineering student at Kwara State University, with a first-class academic standing. Favour is also a software engineer with expertise in web development, cybersecurity, cryptography, and database management. They are passionate about business, personal growth, and spirituality (Christian faith). They are actively involved in projects that blend engineering with technology and real-world applications, including working on time management apps, hospital management software, and web security systems.

Favour's Interests:

Mechanical Engineering: Focus on systems, structures, and control mechanisms.

Cybersecurity: Passion for ethical hacking, penetration testing, network security, and data protection.

Business & Leadership: Favour is aiming to lead in the tech industry and entrepreneurship with a vision for impactful businesses.

Personal Development: Favour wants to become one of the top 1% in software engineering, mechanical engineering, penetration testing, and sales, alongside building a strong spiritual foundation.

Creative Interests: Interested in drawing, design thinking, and understanding how technology and creativity intersect.

Spiritual Growth: Strong focus on faith, purpose, and integrating spiritual wisdom with daily life and work.

Curiosity Challenge Generation Template for AI:
Theme Identification:
Create a theme that explores the intersection of systems control (mechanical, digital, business, and spiritual) with personal empowerment, technology design, and growth strategies.

Personalized Exploration Areas:

Engineering Systems: Generate challenges around understanding control systems, feedback loops, and how these concepts apply to both machines and life.

Cybersecurity Systems: Suggest explorations on how systems can be hacked or protected, drawing parallels between digital security and personal boundaries.

Business Systems: Focus on how different business models and entrepreneurial journeys maintain and leverage power and control. Include lessons from successful tech companies and strategies for scaling.

Spiritual Insights: Relate spiritual principles about control, power, and submission (like in leadership or following Christ) to the exploration of systems in life, offering reflections on how to apply this in personal growth and business ventures.

Creative Exploration: Challenge Favour to visualize or conceptualize systems — such as creating flowcharts, diagrams, or journals about how systems (both technical and personal) can be optimized or maintained.

Output Format:

Daily Challenge: Provide a small task, question, or reflection based on the theme of the week.

Weekly Deep Dive: Suggest a larger, more comprehensive challenge or exploration that ties everything together — e.g., “How do businesses scale while maintaining their core values and systems?”

Reflection Prompts: Encourage Favour to reflect on their experiences and how it ties into both faith and professional goals.

Bonus Questions/Explorations:
Generate additional questions that tap into curiosity-driven thinking. For example:

"How does the concept of feedback loops apply not just in engineering but in personal growth or relationships?"

"What lessons can be learned from hacking techniques to build stronger, more resilient systems — both digital and personal?"

Using this the above Context, generate a curiosity challenge for Favour that includes the following, Go straight to the point it is for an email daily list

Make it span all his areas of interest, a section for each
Format it in an HTML Format
'''

client = genai.Client(api_key=getenv("API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=PROMPT
)

class Mailer:
    """
        This class is used to send Daily email that spans My Interest to increase me curiosity level
    """

    def __init__(self, prompt):
        self.__client = genai.Client(api_key=getenv("API_KEY"))
        self.__prompt = prompt
        self.__sender_email = getenv("SENDER_EMAIL")
        self.__app_password = getenv("APP_PWD")
    
    def generate_content(self):
        """
            This function is used to generate the content of the email
        """
        response = self.__client.models.generate_content(
            model="gemini-2.0-flash", contents=self.__prompt
        )
        return response.text
    def send_email(self, email):
        """
            This function is used to send the email
        """
        subject = "Weekly Curiosity Drop!"
        body = self.generate_content()
        message = MIMEMultipart()
        message["From"] = self.__sender_email
        message["To"] = email
        message["Subject"] = subject


        # Attach the body text
        message.attach(MIMEText(body, "html"))

        # Connect to Gmail SMTP server and send email
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.__sender_email, self.__app_password)
                server.sendmail(self.__sender_email, email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")


if __name__ == "__main__":
    weekly = Mailer(PROMPT)
    weekly.send_email(getenv("RECEIVER_EMAIL"))