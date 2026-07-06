import spacy 
import re 
from spacy.language import Language
from spacy.tokens import Doc 

from spacy.checkemail import get_emails

nlp = spacy.load('en_core_web_sm')

Doc.set_extension("Emails",default=[])

@Language.component("FetchEmails")

def FetchEmails(doc):

    doc._.Emails = get_emails(doc.text)

    return doc

nlp.add_pipe("FetchEmails",last=True)

text = """
Welcome to TechWorld Solutions. If you need technical support, contact
support@techworld.com or helpdesk@services.org. For sales-related queries,
email sales.team@company.co.in or marketing123@business.net.

Students can register using student01@college.edu or
computer.science@university.ac.in. HR department can be reached at
hr-department@mycompany.com, while finance queries should be sent to
finance.office@accounts.in.

For project discussions, contact john.doe@gmail.com,
priya_shah2026@yahoo.in, michael.johnson@outlook.com,
developer+python@opensource.dev, or admin@sub.domain.org.

Some invalid email addresses are also listed below and should NOT be matched:
invalid-email@com
user#gmail.com
support@.com

You may also contact training.team@academy.edu,
events2026@conference.org, and ceo.office@global-enterprise.co.uk
for additional information.
"""

doc = nlp(text)

print(doc._.Emails)


