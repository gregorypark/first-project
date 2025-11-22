import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lets_plot import *

#load dataset
college = pd.read_csv(
    "/Users/gregory/Documents/learn code/college/Most-Recent-Cohorts-Institution.csv"
)

#filtering colleges in Maryland
#college = college.loc[(college["STABBR"] == "MD")]

#finding dominant major and its percentage at each insitution
pcip_columns = [col for col in college.columns if col.startswith('PCIP')]
college['DOMINANT_MAJOR'] = college[pcip_columns].idxmax(axis=1)
college['DMAJOR_PCT'] = college[pcip_columns].max(axis=1)

#focusing on university name, state, and median earnings
college = college[["INSTNM", "STABBR", "DOMINANT_MAJOR","DMAJOR_PCT","MD_EARN_WNE_P10"]]
college = college.rename(columns={
    "INSTNM": "UNIVERISTY",
    "MD_EARN_WNE_P10": "MEDIAN_EARNINGS",
    "STABBR": "STATE"
})

#sorting descending by median earnings
college = college.sort_values("MEDIAN_EARNINGS", ascending=False)

# Create a dictionary mapping CIP codes to readable names
major_names = {
    'PCIP01': 'Agriculture',
    'PCIP03': 'Natural Resources',
    'PCIP04': 'Architecture',
    'PCIP05': 'Area/Ethnic/Cultural Studies',
    'PCIP09': 'Communication',
    'PCIP10': 'Communications Technologies',
    'PCIP11': 'Computer Science',
    'PCIP12': 'Personal & Culinary Services',
    'PCIP13': 'Education',
    'PCIP14': 'Engineering',
    'PCIP15': 'Engineering Technologies',
    'PCIP16': 'Foreign Languages',
    'PCIP19': 'Family & Consumer Sciences',
    'PCIP22': 'Legal Professions',
    'PCIP23': 'English',
    'PCIP24': 'Liberal Arts',
    'PCIP25': 'Library Science',
    'PCIP26': 'Biology',
    'PCIP27': 'Mathematics & Statistics',
    'PCIP29': 'Military Technologies',
    'PCIP30': 'Multi/Interdisciplinary Studies',
    'PCIP31': 'Parks & Recreation',
    'PCIP38': 'Philosophy & Religious Studies',
    'PCIP39': 'Theology',
    'PCIP40': 'Physical Sciences',
    'PCIP41': 'Science Technologies',
    'PCIP42': 'Psychology',
    'PCIP43': 'Security & Protective Services',
    'PCIP44': 'Public Administration',
    'PCIP45': 'Social Sciences',
    'PCIP46': 'Construction Trades',
    'PCIP47': 'Mechanics & Repair',
    'PCIP48': 'Precision Production',
    'PCIP49': 'Transportation',
    'PCIP50': 'Visual & Performing Arts',
    'PCIP51': 'Health Professions',
    'PCIP52': 'Business',
    'PCIP54': 'History'
}

# Apply the mapping
college['DOMINANT_MAJOR'] = college['DOMINANT_MAJOR'].map(major_names)

#removing missing rows in median earnings and major
college = college[college["MEDIAN_EARNINGS"].notna()]
college = college[college["DOMINANT_MAJOR"].notna()]

#if we remove specialist schools
college[college["DMAJOR_PCT"] != 1.0000]

LetsPlot.setup_html()
college.figure_size = (14, 8)

(ggplot(college, aes(x="UNIVERISTY", y="MEDIAN_EARNINGS", color="DOMINANT_MAJOR")) + geom_point())

