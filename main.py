
# List of player options. Order irrelevant.
countryList = ["a", "b", "c", "d", "e", "f", "g"]

# List of player's preferences. Player order and preference order relevant. 
player0 = ["a", "b", "c"]
player1 = ["c", "b", "f"]
player2 = ["d", "g", "b"]
player3 = ["g", "c", "a"]
player4 = ["a", "f", "e"]
player5 = ["a", "d", "c"]
player6 = ["b", "f", "c"]

prefList = [player0, player1, player2, player3, player4, player5, player6]

def permutations(elements): # Iterate through all permutations of given set
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]

def satisfaction(preferences, assignment): # Compare assigned list to preference data
    sat = 0 # Satisfaction score
    i = 0
    for country in assignment: # Iterate through country assignments
        if(country in preferences[assignment.index(country)]): # If assignment for a given player is present in that player's preferences list
            sat+=(len(preferences[assignment.index(country)])-preferences[assignment.index(country)].index(country)) # Add inverse of preference index to satisfaction score
    return int(sat)

sat = 0
iterations = 0
solutions = []


for assignment in list(permutations(countryList)): 
    if satisfaction(prefList, assignment) > sat: # New max sat
        solutions.clear()
        solutions.append(assignment)
        
        sat = satisfaction(prefList, assignment)

    elif satisfaction(prefList, assignment) == sat: # Tied max sat
        solutions.append(assignment)
    
    iterations+=1


print(f"Checked {iterations} permutations. Found the following {len(solutions)} possibilities with satisfaction score {sat}/21:")
print(*solutions, sep="\n")

