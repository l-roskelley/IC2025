import pandas as pd
import plotly.express as px

file = "new.csv"
with open(file, 'w') as handle:
                    rdr = PdfReader(handle)
                    if str(file).endswith('.pdf'):
                        for page in rdr.pages:
                            text = page.extract_text()
                        #Use a regular expression to look through the text of each PDF page for something that looks like a state abbreviation (two capital letters), followed by a single space, followed by a 5-digit zip code.
                            statecount = re.findall(r'\b[A-Z][A-Z] \d{5}\b', text)
                            for state in statecount:
                                print(state, file = f)