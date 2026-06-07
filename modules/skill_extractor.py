#Purpose: Extract skills from text
#Extract skills
#Find missing skills
    
SKILLS = [

# Programming
"python","java","c","c++","javascript",

# Frontend
"html","css","react","angular","bootstrap",

# Backend
"nodejs","express","spring boot","django","flask",

# Database
"mysql","postgresql","mongodb","sql",

# Cloud
"aws","azure","gcp",

# DevOps
"docker","kubernetes","jenkins","git","github",

# Data Science
"machine learning",
"deep learning",
"tensorflow",
"pytorch",
"nlp",
"data analysis",

# Analytics
"power bi",
"tableau",
"excel"

]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return list(set(found))