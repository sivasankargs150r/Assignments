# Candidate Names for Different Candidates
nominee_1 = input("Enter Nominee -1 Name: ")
nominee_2 = input("Enter Nominee -2 Name: ")
#### Votes for each Nominee
Candidate_1 = 0
Candidate_2 = 0
print("=========================================")
voters_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voters = len(voters_id)

while True:
    if not voters_id:
        print("Voting session is over: ")

        if Candidate_1 > Candidate_2:
            percentage = (Candidate_1/ num_of_voters) * 100
            print(nominee_1, "has won with", percentage, "% of Votes")
            break
        elif Candidate_2 > Candidate_1:
            percentage = (Candidate_2/ num_of_voters) * 100
            print(nominee_2, "has won with", percentage, "% of Votes")
            break
        else:
            print("There is Tie in the Elections")
            break

    voter = int(input("Enter your Voter Id"))
    if voter in voters_id:
        print("You are a Eligible Voting Candidate")
        voters_id.remove(voter)
        vote = int(input("Enter your Vote - 1 or 2 "))
        if vote == 1:
            Candidate_1+= 1
            print("=======================Thank you for Voting========================")
        elif vote == 2:
            Candidate_2+= 1
            print("=======================Thank you for Voting========================")
        elif vote > 2:
            print("Kindly enter 1 or 2 Only")
    else:
        print("You are not a voter Here or your Vote is over !!!!")