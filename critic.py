# creae a function that recieves output from agent doer 

def critic(doer_output):
    steps = doer_output["steps"]

    if len(steps) <2:
        return {
            "status": "OKLART",
            "feedback":" för få steg, lösningen är otydlig"
        }

    for step in steps:
        if "Steg" not in step:
            return {
           "status": "Oklart",
           "feedback": "Stegen är inte tydligt formulerade."
       }

        return {
            "status": "GRÖNT",
            "message": "Lösningen är godkänd"
        }
 

