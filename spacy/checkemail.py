import re 

def get_emails(text: str)-> list:

    email_pattern = r'''
        [a-zA-Z0-9._%+-]+      # Local part (username)
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # Domain name
        \.                     # Dot
        [a-zA-Z]{2,}           # Top-level domain
    '''
    
    emails = re.findall(email_pattern,text,re.IGNORECASE|re.VERBOSE)

    return emails

# if __name__=="__main__":
#     sample_text = """
# Welcome to TechWorld Solutions. If you need technical support, contact
# support@techworld.com or helpdesk@services.org. For sales-related queries,
# email sales.team@company.co.in or marketing123@business.net.

# Students can register using student01@college.edu or
# computer.science@university.ac.in. HR department can be reached at
# hr-department@mycompany.com, while finance queries should be sent to
# finance.office@accounts.in.

# For project discussions, contact john.doe@gmail.com,
# priya_shah2026@yahoo.in, michael.johnson@outlook.com,
# developer+python@opensource.dev, or admin@sub.domain.org.

# Some invalid email addresses are also listed below and should NOT be matched:
# invalid-email@com
# user#gmail.com
# support@.com

# You may also contact training.team@academy.edu,
# events2026@conference.org, and ceo.office@global-enterprise.co.uk
# for additional information.
# """

# result = get_emails(sample_text)

# print(result)
# for em in result:
#     print(em)