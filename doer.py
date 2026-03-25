# Create function that recieves , solves and passes down 

def kontrollera_nätverk():
    return " Kontrollera att wifi är påslaget , symbol 📶 "

def doer(planner_output):
    classification= planner_output["classification"]

    if classification == "Nätverksproblem":
         steps = [
    "Steg 1: ⏻ Kontrollera att din dator är på.",
    "Steg 2: 📶 Kontrollera att WiFi är påslaget.",
    "Steg 3: 📡 Starta om routern.",
    "Steg 4: 📶 Testa anslutningen igen."
]

    elif classification == "Hårdvaruproblem":
         steps = [
              " Steg 1:Kontrollera att skärmen är på 🖥️",
              "Steg 2: Kontrollera att kablarna sitter i ordentligt 🔌",
              "Steg 3: Starta om datorn ⏻"
         ]
    
    else:
        steps = [
             "Steg 1: Jag är inte säker på problemet.",
             "Steg 2 : Kontakta supporten om problemet kvarstår  🎧"
        ]

    return {
        "steps": steps,
        "classification": classification 
    }




 