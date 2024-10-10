import tkinter as tk
from tkinter import messagebox,simpledialog
import json
import os

global pencSchool, penySchool, penc_debater_info, peny_debater_info, best_debater_name
best_debater_name = None
pencSchool = "Sekolah Pencadang"
penySchool = "Sekolah Penyanggah"
penc_debater_info = {}
peny_debater_info = {}
pencTotalScore = None
penyTotalScore = None

def roleSelect():
    global penc_names, penc_roles, penc_bonus, peny_names, peny_roles, peny_bonus
    global penc_debater_info, peny_debater_info  # Declare these as globals to use later

    # Initialize lists and dictionaries
    penc_names = []
    penc_roles = []
    penc_bonus = []
    peny_names = []
    peny_roles = []
    peny_bonus = []
    
    # Pencadang School Input
    global pencSchool
    pencSchool = simpledialog.askstring("Pencadang School", "Enter Pencadang School:")
    if pencSchool:
        messagebox.showinfo("Welcome", f"Selamat Datang, {pencSchool} selaku pihak Pencadang")
    else:
        messagebox.showerror("Error", "Invalid input.")
        return

    # Pencadang Debater Input
    while len(penc_names) < 3:
        pencName = simpledialog.askstring("Pencadang Debater", "Enter Pencadang Debater's name (Press Cancel to Finish):")
        if not pencName:
            break
        penc_names.append(pencName)
        
        # Main Role Input
        while True:
            pencRole = simpledialog.askstring("Main Role", f"Enter {pencName}'s main role (1, 2, 3):")
            if pencRole in ["1", "2", "3"] and penc_roles.count(pencRole) < 1:
                penc_roles.append(pencRole)
                break
            elif pencRole in ["1", "2", "3"]:
                messagebox.showwarning("Warning", f"Cannot assign {pencRole} because {penc_names[penc_roles.index(pencRole)]} has the role {pencRole}")
            else:
                messagebox.showerror("Error", "Invalid input.")
        
        # Secondary Role Input
        while True:
            pencBonus = simpledialog.askstring("Secondary Role", f"Enter {pencName}'s secondary role (HB1, HB2, P):")
            if pencBonus in ["HB1", "HB2", "P"] and penc_bonus.count(pencBonus) < 1:
                penc_bonus.append(pencBonus)
                break
            elif pencBonus in ["HB1", "HB2", "P"]:
                messagebox.showwarning("Warning", f"Cannot assign {pencBonus} because {penc_names[penc_bonus.index(pencBonus)]} has the role {pencBonus}")
            else:
                messagebox.showerror("Error", "Invalid input.")
        
        # Populate the Pencadang debater info dictionary
        penc_debater_info[pencName] = (pencRole, pencBonus)

    # Show Pencadang Debater Info
    debater_info = "\n".join(f"{x} is Pencadang {y}, and will do secondary role {z}" for x, y, z in zip(penc_names, penc_roles, penc_bonus))
    messagebox.showinfo("Pencadang Debater Info", f"Pihak Pencadang: {pencSchool}\n{debater_info}")

    # Penyanggah School Input
    global penySchool
    penySchool = simpledialog.askstring("Penyanggah School", "Enter Penyanggah School:")
    if penySchool:
        messagebox.showinfo("Welcome", f"Selamat Datang, {penySchool} selaku pihak Penyanggah")
    else:
        messagebox.showerror("Error", "Invalid input.")
        return

    # Penyanggah Debater Input
    while len(peny_names) < 3:
        penyName = simpledialog.askstring("Penyanggah Debater", "Enter Penyanggah Debater's name (Press Cancel to Finish):")
        if not penyName:
            break
        peny_names.append(penyName)

        # Main Role Input
        while True:
            penyRole = simpledialog.askstring("Main Role", f"Enter {penyName}'s main role (1, 2, 3):")
            if penyRole in ["1", "2", "3"] and peny_roles.count(penyRole) < 1:
                peny_roles.append(penyRole)
                break
            elif penyRole in ["1", "2", "3"]:
                messagebox.showwarning("Warning", f"Cannot assign {penyRole} because {peny_names[peny_roles.index(penyRole)]} has the role {penyRole}")
            else:
                messagebox.showerror("Error", "Invalid input.")

        # Secondary Role Input
        while True:
            penyBonus = simpledialog.askstring("Secondary Role", f"Enter {penyName}'s secondary role (HB1, HB2, P):")
            if penyBonus in ["HB1", "HB2", "P"] and peny_bonus.count(penyBonus) < 1:
                peny_bonus.append(penyBonus)
                break
            elif penyBonus in ["HB1", "HB2", "P"]:
                messagebox.showwarning("Warning", f"Cannot assign {penyBonus} because {peny_names[peny_bonus.index(penyBonus)]} has the role {penyBonus}")
            else:
                messagebox.showerror("Error", "Invalid input.")

        # Populate the Penyanggah debater info dictionary
        peny_debater_info[penyName] = (penyRole, penyBonus)

    # Show Penyanggah Debater Info
    debater_info = "\n".join(f"{x} is Penyanggah {y}, and will do secondary role {z}" for x, y, z in zip(peny_names, peny_roles, peny_bonus))
    messagebox.showinfo("Penyanggah Debater Info", f"Pihak Penyanggah: {penySchool}\n{debater_info}")

def roleEdit():
    global penySchool, pencSchool
    global penc_debater_info, peny_debater_info

    # Print the dictionaries before the edit options
    current_info = "\nCurrent Pencadang Debater Info:\n" + "\n".join(f"{name}: Role: {role} and {bonus}" for name, (role, bonus) in penc_debater_info.items())
    current_info += "\n\nCurrent Penyanggah Debater Info:\n" + "\n".join(f"{name}: Role: {role} and {bonus}" for name, (role, bonus) in peny_debater_info.items())
    messagebox.showinfo("Current Debater Info", current_info)

    while True:
        editWhat = simpledialog.askstring("Edit Options", "What would you like to edit?\n1. School Name\n2. Debater Name\n3. Debater Main Role\n4. Debater Secondary Role\n5. Return to Menu:")
        
        if editWhat == "1":
            while True:
                oldSch = simpledialog.askstring("Select School", "Which School?\n1. Pencadang\n2. Penyanggah:")
                if oldSch == "1":
                    newSch = simpledialog.askstring("New Pencadang School Name", f"Enter new name to replace {pencSchool}:")
                    pencSchool = newSch
                    messagebox.showinfo("Info", f"Side Pencadang is now {pencSchool}")
                    break
                elif oldSch == "2":
                    newSch = simpledialog.askstring("New Penyanggah School Name", f"Enter new name to replace {penySchool}:")
                    penySchool = newSch
                    messagebox.showinfo("Info", f"Side Penyanggah is now {penySchool}")
                    break
                else:
                    messagebox.showerror("Error", "Invalid Input.")
                    continue
            continue

        elif editWhat == "2":
            totalList = penc_names + peny_names
            debater_list = "\n".join(f"{i+1}. {name}" for i, name in enumerate(totalList))
            oldName = simpledialog.askstring("Edit Debater Name", f"Listing all Debaters:\n{debater_list}\nWhich name? Press Enter to exit")
            
            while True:
                if oldName in penc_names:
                    newName = simpledialog.askstring("Replace Name", "Who is replacing them?")
                    penc_names[penc_names.index(oldName)] = newName
                    penc_debater_info[newName] = penc_debater_info.pop(oldName)  # Update dictionary
                    messagebox.showinfo("Info", f"Pencadang {newName} is now in {penc_debater_info[newName][0]} and {penc_debater_info[newName][1]}")
                    break
                elif oldName in peny_names:
                    newName = simpledialog.askstring("Replace Name", "Who is replacing them?")
                    peny_names[peny_names.index(oldName)] = newName
                    peny_debater_info[newName] = peny_debater_info.pop(oldName)  # Update dictionary
                    messagebox.showinfo("Info", f"Penyanggah {newName} is now in {peny_debater_info[newName][0]} and {peny_debater_info[newName][1]}")
                    break
                else:
                    messagebox.showerror("Error", "Name not found.")
                    oldName = simpledialog.askstring("Edit Debater Name", f"Which name? Press Enter to exit")
            continue

        elif editWhat == "3":
            oldName = simpledialog.askstring("Edit Main Role", f"Listing all Debaters:\n{debater_list}\nWhich name? Press Enter to exit")
            if oldName in penc_names:
                newRole = simpledialog.askstring("New Role", f"Enter new main role for {oldName} (1, 2, 3):")
                penc_debater_info[oldName] = (newRole, penc_debater_info[oldName][1])  # Update only role
                messagebox.showinfo("Info", f"{oldName}'s role is now {newRole}.")
            elif oldName in peny_names:
                newRole = simpledialog.askstring("New Role", f"Enter new main role for {oldName} (1, 2, 3):")
                peny_debater_info[oldName] = (newRole, peny_debater_info[oldName][1])  # Update only role
                messagebox.showinfo("Info", f"{oldName}'s role is now {newRole}.")
            else:
                messagebox.showerror("Error", "Debater not found.")
            continue

        elif editWhat == "4":
            oldName = simpledialog.askstring("Edit Secondary Role", "Enter Debater's Name:")
            if oldName in penc_names:
                newRole = simpledialog.askstring("New Secondary Role", f"Enter new secondary role for {oldName} (HB1, HB2, P):")
                penc_debater_info[oldName] = (penc_debater_info[oldName][0], newRole)  # Update only bonus
                messagebox.showinfo("Info", f"{oldName}'s secondary role is now {newRole}.")
            elif oldName in peny_names:
                newRole = simpledialog.askstring("New Secondary Role", f"Enter new secondary role for {oldName} (HB1, HB2, P):")
                peny_debater_info[oldName] = (peny_debater_info[oldName][0], newRole)  # Update only bonus
                messagebox.showinfo("Info", f"{oldName}'s secondary role is now {newRole}.")
            else:
                messagebox.showerror("Error", "Debater not found.")
            continue

        elif editWhat == "5":
            break  # Exit the loop and return to the main menu
        else:
            messagebox.showerror("Error", "Invalid input.")

def save_results(winner, best_debater, best_debater_score):
    folder_path = "/Users/kamalashraf/Library/Mobile Documents/com~apple~CloudDocs/Law School/LawTech/Bahas 4PY/Debates"
    file_name = f"{pencSchool} lwn {penySchool}.txt"
    file_path = folder_path + "/" + file_name
    # Create a serialized name for the debate
    serialized_name = f"{pencSchool} lwn {penySchool}.txt"
    
    # Prepare the data to save
    results = (
        f"Winner: {winner}\n"
        f"Best Debater: {best_debater} with a score of {best_debater_score}\n\n"
        f"Scoresheet:\n"
        f"Pencadang:\n"
        f"  Total Score: {pencTotalScore}\n"
        f"  Individual Scores:\n"
        + "\n".join([f"    {name}: {score} points" for name, score in pencIndivScores.items()]) +
        "\n\nPenyanggah:\n"
        f"  Total Score: {penyTotalScore}\n"
        f"  Individual Scores:\n"
        + "\n".join([f"    {name}: {score} points" for name, score in penyIndivScores.items()])
    )

    # Save the results to a text file
    with open(file_path, 'w') as text_file:
        text_file.write(results)

    messagebox.showinfo("Save Results", f"Results saved as {serialized_name}")

def view_verdict():
    global winnerSchool, bestDebater

    if bestDebater:
        best_debater_name, best_debater_score = list(bestDebater.items())[0]
    else:
        best_debater_name = "None"
        best_debater_score = "No score available"

    messagebox.showinfo("Verdict", f"Winner is {winnerSchool}, Best Debater is {best_debater_name} with a score of {best_debater_score}.")
    
    # Save results with the correct parameters
    save_results(winnerSchool, best_debater_name, best_debater_score)

def view_scoresheet():
    # Generate the Pencadang scoresheet
    penc_scores = "\n".join([f"{name}: {score} points" for name, score in pencIndivScores.items()])
    
    # Generate the Penyanggah scoresheet
    peny_scores = "\n".join([f"{name}: {score} points" for name, score in penyIndivScores.items()])
    
    # Combine the scores into a single string for the scoresheet
    scoresheet = f"Scoresheet:\n\nPencadang:\n{pencTotalScore}\n{penc_scores}\n\nPenyanggah:\n{penyTotalScore}\n{peny_scores}\n"
    
    # Show the scoresheet in the message box
    messagebox.showinfo("Scoresheet", scoresheet)

    # Call the save_results function to save the scoresheet
    save_results(pencSchool, penySchool, scoresheet)

def readytoScore():

    def check_no_repeats(penc_debater_info):
        # Step 1: Flatten the roles and bonuses into two separate lists
        roles = [info[0] for info in penc_debater_info.values()]  # Extract roles
        bonuses = [info[1] for info in penc_debater_info.values()]  # Extract bonuses

        # Step 2: Use sets to check for duplicates
        unique_roles = set(roles)
        unique_bonuses = set(bonuses)

        # Step 3: Compare lengths
        roles_duplicate = len(roles) != len(unique_roles)
        bonuses_duplicate = len(bonuses) != len(unique_bonuses)

        # Step 4: Print results
        if not roles_duplicate and not bonuses_duplicate:
            print("No duplicates found in roles or bonuses.")
            return True
        else:
            if roles_duplicate:
                print("Duplicates found in roles.")
            if bonuses_duplicate:
                print("Duplicates found in bonuses.")
            return False
    
    print("\nCurrent Pencadang Debater Info:")
    for name, (role, bonus) in penc_debater_info.items():
        print(f"{name}: Role: {role} and {bonus}")
    
    print("\nCurrent Penyanggah Debater Info:")
    for name, (role, bonus) in peny_debater_info.items():
        print(f"{name}: Role: {role} and {bonus}")

    if len(penc_debater_info.keys()) == 3 and len(peny_debater_info.keys()) == 3:
        numDebaters = True
    else:
        numDebaters = False
    if check_no_repeats(penc_debater_info) == False:
        print("Duplicates found in Pencadang")
    if check_no_repeats(peny_debater_info) == False:
        print("Duplicates found in Penyanggah")
    if check_no_repeats(penc_debater_info) == True and check_no_repeats(peny_debater_info) == True:
        valuesGood = True
    else:
        valuesGood = False

    if numDebaters and valuesGood:
        return True
    else:
        return False

def scoring():
    global pencIndivScores, penyIndivScores, pencTotalScore, penyTotalScore, bestDebater, winnerSchool
    pencIndivScores = {}
    penyIndivScores = {}
    pencTotalScore = None
    penyTotalScore = None
    bestDebater = {}
    winnerSchool = None

    # Function to get valid integer input within a range
    def get_valid_input(prompt, min_value, max_value):
        while True:
            try:
                value = int(simpledialog.askstring("Input", prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    messagebox.showerror("Invalid input", f"Please enter a number between {min_value} and {max_value}.")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer.")

    # Function to confirm the score
    def confirm_input(prompt):
        while True:
            choice = simpledialog.askstring("Confirm", prompt + "\n1. Yes\n2. No")
            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                messagebox.showerror("Invalid choice", "Please enter 1 or 2.")

    def collect_scores(debater_info, role_label):
        scores = {}
        for name, (role, bonus) in debater_info.items():
            while True:
                scoreA = get_valid_input(f"{role_label} {role}: Please score {name}'s Bahasa dan Gaya /10: ", 1, 10)
                scoreB = get_valid_input(f"{role_label} {role}: Please score {name}'s Isi /10: ", 1, 10)

                if bonus in ["HB1", "HB2"]:
                    scoreD = 0
                    scoreC = get_valid_input(f"{role_label} {bonus}: Please score {name}'s Hujahan Berapi /10: ", 1, 10)
                elif bonus == "P":
                    scoreC = 0
                    scoreD = get_valid_input(f"{role_label} {bonus}: Please score {name}'s Penggulung /10: ", 1, 10)

                indivScore = scoreA + scoreB + scoreC + scoreD
                if confirm_input(f"{name} has scored a total of {indivScore} points out of 30. Confirm score?"):
                    scores[name] = indivScore
                    break
        return scores

    # Collect scores for Pencadang and Penyanggah
    pencIndivScores = collect_scores(penc_debater_info, "Pencadang Pembahas")
    penyIndivScores = collect_scores(peny_debater_info, "Penyanggah Pembahas")

    # Strategy scores
    pencStrat = get_valid_input("Enter Pencadang's Strategi score /10: ", 1, 10)
    penyStrat = get_valid_input("Enter Penyanggah's Strategi score /10: ", 1, 10)

    pencTotalScore = sum(pencIndivScores.values()) + pencStrat
    penyTotalScore = sum(penyIndivScores.values()) + penyStrat
    messagebox.showinfo("Total Scores", f"Pencadang has scored {pencTotalScore} out of 100.\nPenyanggah has scored {penyTotalScore} out of 100.")

    # Function to handle tiebreakers
    def handle_tiebreakers(bestDebaters):
        if len(bestDebaters) > 1:
            messagebox.showinfo("Tie Found", f"Tie found between {', '.join(bestDebaters)}.")
            for index, debater in enumerate(bestDebaters, start=1):
                messagebox.showinfo("Debater Options", f"{index}. {debater}")

            tiebreakerIndex = get_valid_input("Enter the number of the debater to award the score boost: ", 1, len(bestDebaters))
            tiebreakerDebater = bestDebaters[tiebreakerIndex - 1]
            return tiebreakerDebater
        return bestDebaters[0]

    # Determine best debater within Pencadang
    bestPencScore = max(pencIndivScores.values())
    bestDebatersPenc = [name for name, score in pencIndivScores.items() if score == bestPencScore]
    bestDebaterPenc = handle_tiebreakers(bestDebatersPenc)
    pencIndivScores[bestDebaterPenc] += 1  # Boost score by 1 for the best debater

    # Determine best debater within Penyanggah
    bestPenyScore = max(penyIndivScores.values())
    bestDebatersPeny = [name for name, score in penyIndivScores.items() if score == bestPenyScore]
    bestDebaterPeny = handle_tiebreakers(bestDebatersPeny)
    penyIndivScores[bestDebaterPeny] += 1  # Boost score by 1 for the best debater

    # Compare best debaters across teams
    if pencIndivScores[bestDebaterPenc] > penyIndivScores[bestDebaterPeny]:
        messagebox.showinfo("Best Debater", f"Pencadang {bestDebaterPenc} is your Pembahas Terbaik, with a score of {pencIndivScores[bestDebaterPenc]}.")
        bestDebater[bestDebaterPenc] = pencIndivScores[bestDebaterPenc]
    elif pencIndivScores[bestDebaterPenc] < penyIndivScores[bestDebaterPeny]:
        messagebox.showinfo("Best Debater", f"Penyanggah {bestDebaterPeny} is your Pembahas Terbaik, with a score of {penyIndivScores[bestDebaterPeny]}.")
        bestDebater[bestDebaterPeny] = penyIndivScores[bestDebaterPeny]
    else:
        # Handle tie for best debater between teams
        messagebox.showinfo("Tie Found", f"Tie found between Pencadang {bestDebaterPenc} and Penyanggah {bestDebaterPeny}.")
        winnerChoice = get_valid_input("Select the winning team:\n1. Pencadang\n2. Penyanggah\nEnter 1 or 2: ", 1, 2)
        if winnerChoice == 1:
            messagebox.showinfo("Best Debater", f"Pencadang {bestDebaterPenc} is your Pembahas Terbaik, with a score of {pencIndivScores[bestDebaterPenc]}.")
            bestDebater[bestDebaterPenc] = pencIndivScores[bestDebaterPenc] + 1
        else:
            messagebox.showinfo("Best Debater", f"Penyanggah {bestDebaterPeny} is your Pembahas Terbaik, with a score of {penyIndivScores[bestDebaterPeny]}.")
            bestDebater[bestDebaterPeny] = penyIndivScores[bestDebaterPeny] + 1

    # Determine winning team
    if pencTotalScore > penyTotalScore:
        messagebox.showinfo("Winner", f"Your Winner is Pencadang with {pencTotalScore} to {penyTotalScore}.")
        winnerSchool = "Pencadang"
    elif pencTotalScore < penyTotalScore:
        messagebox.showinfo("Winner", f"Your Winner is Penyanggah with {penyTotalScore} to {pencTotalScore}.")
        winnerSchool = "Penyanggah"
    else:
        # Handle tie for winning team
        while True:
            tieBreaker = simpledialog.askstring("Tie Breaker", f"Total scores are tied at {pencTotalScore}. Which team is the winner? (Pencadang/Penyanggah): ")
            if tieBreaker.lower() == "pencadang":
                messagebox.showinfo("Winner", f"Your Winner is Pencadang with a score of {pencTotalScore}.")
                winnerSchool = "Pencadang"
                break
            elif tieBreaker.lower() == "penyanggah":
                messagebox.showinfo("Winner", f"Your Winner is Penyanggah with a score of {penyTotalScore}.")
                winnerSchool = "Penyanggah"
                break
            else:
                messagebox.showerror("Invalid input", "Please enter 'Pencadang' or 'Penyanggah'.")

    messagebox.showinfo("Info", "Scoring function executed.")

# GUI Class
class DebateApp:
    def __init__(self, master):
        self.master = master
        master.title(f"Welcome to Bahas 4PM")
        
        # Set background color
        master.configure(bg="#f0f0f0")  # Light gray background

        # Create a frame for the title
        title_frame = tk.Frame(master, bg="#f0f0f0")  # Same background color
        title_frame.pack(pady=10)
        
        # Title label
        self.title_label = tk.Label(title_frame, text=(f"{pencSchool} lwn {penySchool}"), font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333333")  # Dark gray text
        self.title_label.pack()

        # Buttons to trigger functions
        self.role_select_button = tk.Button(master, text="Setup Debate", command=self.roleSelect)
        self.role_select_button.pack(pady=10)

        self.role_edit_button = tk.Button(master, text="Edit Roles", command=roleEdit)
        self.role_edit_button.pack(pady=10)

        self.ready_to_score_button = tk.Button(master, text="Check Readiness to Score", command=self.check_ready_to_score)
        self.ready_to_score_button.pack(pady=10)

        self.scoring_button = tk.Button(master, text="Start Scoring", command=scoring)
        self.scoring_button.pack(pady=10)

        self.view_verdict_button = tk.Button(master, text="View Verdict", command=view_verdict)
        self.view_verdict_button.pack(pady=10)

        self.view_scoresheet_button = tk.Button(master, text="View Scoresheet", command=view_scoresheet)
        self.view_scoresheet_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)
    def roleSelect(self):
        global penc_names, penc_roles, penc_bonus, peny_names, peny_roles, peny_bonus
        global penc_debater_info, peny_debater_info  # Declare these as globals to use later

        # Initialize lists and dictionaries
        penc_names = []
        penc_roles = []
        penc_bonus = []
        peny_names = []
        peny_roles = []
        peny_bonus = []
        
        # Pencadang School Input
        global pencSchool
        pencSchool = simpledialog.askstring("Pencadang School", "Enter Pencadang School:")
        if pencSchool:
            messagebox.showinfo("Welcome", f"Selamat Datang, {pencSchool} selaku pihak Pencadang")
        else:
            messagebox.showerror("Error", "Invalid input.")
            return

        # Pencadang Debater Input
        while len(penc_names) < 3:
            pencName = simpledialog.askstring("Pencadang Debater", "Enter Pencadang Debater's name (Press Cancel to Finish):")
            if not pencName:
                break
            penc_names.append(pencName)
            
            # Main Role Input
            while True:
                pencRole = simpledialog.askstring("Main Role", f"Enter {pencName}'s main role (1, 2, 3):")
                if pencRole in ["1", "2", "3"] and penc_roles.count(pencRole) < 1:
                    penc_roles.append(pencRole)
                    break
                elif pencRole in ["1", "2", "3"]:
                    messagebox.showwarning("Warning", f"Cannot assign {pencRole} because {penc_names[penc_roles.index(pencRole)]} has the role {pencRole}")
                else:
                    messagebox.showerror("Error", "Invalid input.")
            
            # Secondary Role Input
            while True:
                pencBonus = simpledialog.askstring("Secondary Role", f"Enter {pencName}'s secondary role (HB1, HB2, P):")
                if pencBonus in ["HB1", "HB2", "P"] and penc_bonus.count(pencBonus) < 1:
                    penc_bonus.append(pencBonus)
                    break
                elif pencBonus in ["HB1", "HB2", "P"]:
                    messagebox.showwarning("Warning", f"Cannot assign {pencBonus} because {penc_names[penc_bonus.index(pencBonus)]} has the role {pencBonus}")
                else:
                    messagebox.showerror("Error", "Invalid input.")
            
            # Populate the Pencadang debater info dictionary
            penc_debater_info[pencName] = (pencRole, pencBonus)

        # Show Pencadang Debater Info
        debater_info = "\n".join(f"{x} is Pencadang {y}, and will do secondary role {z}" for x, y, z in zip(penc_names, penc_roles, penc_bonus))
        messagebox.showinfo("Pencadang Debater Info", f"Pihak Pencadang: {pencSchool}\n{debater_info}")

        # Penyanggah School Input
        global penySchool
        penySchool = simpledialog.askstring("Penyanggah School", "Enter Penyanggah School:")
        if penySchool:
            messagebox.showinfo("Welcome", f"Selamat Datang, {penySchool} selaku pihak Penyanggah")
        else:
            messagebox.showerror("Error", "Invalid input.")
            return

        # Penyanggah Debater Input
        while len(peny_names) < 3:
            penyName = simpledialog.askstring("Penyanggah Debater", "Enter Penyanggah Debater's name (Press Cancel to Finish):")
            if not penyName:
                break
            peny_names.append(penyName)

            # Main Role Input
            while True:
                penyRole = simpledialog.askstring("Main Role", f"Enter {penyName}'s main role (1, 2, 3):")
                if penyRole in ["1", "2", "3"] and peny_roles.count(penyRole) < 1:
                    peny_roles.append(penyRole)
                    break
                elif penyRole in ["1", "2", "3"]:
                    messagebox.showwarning("Warning", f"Cannot assign {penyRole} because {peny_names[peny_roles.index(penyRole)]} has the role {penyRole}")
                else:
                    messagebox.showerror("Error", "Invalid input.")

            # Secondary Role Input
            while True:
                penyBonus = simpledialog.askstring("Secondary Role", f"Enter {penyName}'s secondary role (HB1, HB2, P):")
                if penyBonus in ["HB1", "HB2", "P"] and peny_bonus.count(penyBonus) < 1:
                    peny_bonus.append(penyBonus)
                    break
                elif penyBonus in ["HB1", "HB2", "P"]:
                    messagebox.showwarning("Warning", f"Cannot assign {penyBonus} because {peny_names[peny_bonus.index(penyBonus)]} has the role {penyBonus}")
                else:
                    messagebox.showerror("Error", "Invalid input.")

            # Populate the Penyanggah debater info dictionary
            peny_debater_info[penyName] = (penyRole, penyBonus)

        # Show Penyanggah Debater Info
        debater_info = "\n".join(f"{x} is Penyanggah {y}, and will do secondary role {z}" for x, y, z in zip(peny_names, peny_roles, peny_bonus))
        messagebox.showinfo("Penyanggah Debater Info", f"Pihak Penyanggah: {penySchool}\n{debater_info}")
        self.pencSchool = pencSchool
        self.penySchool = penySchool
        self.master.title(f"Welcome to Bahas 4PM {self.pencSchool} lwn {self.penySchool}")
        self.title_label.config(text=f"{self.pencSchool} lwn {self.penySchool}")
        
    def check_ready_to_score(self):
        if readytoScore():
            messagebox.showinfo("Status", "Ready to Score!")
        else:
            messagebox.showwarning("Status", "Not ready to score!")

    def exit_app(self):
        # Confirm before exiting
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()  # Close the main window

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    app = DebateApp(root)
    root.mainloop()
