#https://leetcode.com/problems/rank-teams-by-votes/
def rankTeams(votes):
    """
    This function ranks a list of teams based on a list of votes.
    Each vote is a list of teams in order of preference, with the first team being the most preferred.
    The function returns a string of team names, sorted by their total score in descending order.
    If two teams have the same score, they are sorted alphabetically.
    """
    # Initialize a dictionary to store the scores of each team
    dict1 = {}
    
    # Get the number of teams
    n = len(votes[0])
    
    # Initialize the scores of each team to zero
    for c in votes[0]:
        dict1[c] = [0] * n
    
    # Calculate the score of each team for each vote
    for vote in votes:
        for j in range(len(vote)):
            dict1[vote[j]][j] += 1
    
    # Sort the teams by their total score and alphabetically
    result = sorted(
        votes[0],
        key=lambda team: (dict1[team], -ord(team)),
        reverse=True
    )
    
    # Return the sorted list of teams as a string
    return ''.join(result)