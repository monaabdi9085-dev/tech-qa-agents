# create a function that 

#takes the user’s question
#classifies the problem
#returns a simplified version

def planner(user_question):
    question= user_question.lower()

    if "wifi" in question or "internet" in question or "nät" in question  or "nätverk" in question  or "anslutning" in question:
        classification= "Nätverksproblem"
        rephrased = " Det låter som att du har problem med internet."
    elif "skärm" in question or "svart" in question or "bildskärm" or "slockna" in question:
        classification = "Hårdvaruproblem"
        rephrased = "Det låter som att du har problem med skärmen."
    elif "program" in question or "app" in question:
        classification = "Programvaruproblem"
        rephrased = " Det låter som att du har ett problem med ett program"
    else:
        classification= "Okänt problem"
        rephrased = "Jag förstår inte riktigt problemet ännu. "



    return {
        "original_question": user_question,
        "rephrased_problem": rephrased,
        "classification": classification

    }





