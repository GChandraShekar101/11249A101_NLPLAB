import spacy
nlp=spacy.load("en_core_web_sm")
text=input("Enter a sentence:")
doc=nlp(text)
print("\nNamed Entities")
for ent in doc.ents:
    print(f"Entity:{ent.text}")
    print(f"label:{ent.label_}")
   
