from planner import planner
from doer import doer 
from critic import critic

def main ():
    user_question = input ("Vad är ditt datorrelaterade problem?")

    # step 1 planner 
    planner_output = planner (user_question)
    print("\n [Planner]")
    print (planner_output)

    attempts = 0

    while attempts < 2:
        # Step 2: Doer
        doer_output = doer(planner_output)
        print("\n[Doer]")
        for step in doer_output["steps"]:
            print(step)


            # Step 3: Critic
        critic_output = critic(doer_output)
        print("\n[Critic]")
        print(critic_output)

        # If approved -> break 
        if critic_output["status"] == "GRÖNT":
            print ("\n Lösningen skickas till användaren")
            break 
        else :
            print("\n Lösningen var oklar, försöker igen ..")
            attempts += 1
        # Human-in-the-loop
        if attempts == 2: 
            print("\n🎧 Omdirigerar till mänsklig support...")


if __name__ == "__main__":
    main()
        

