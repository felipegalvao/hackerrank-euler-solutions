args = input().split()
people = int(args[0])
topics = int(args[1])
teams = 0
max_topics = 0
matrix = []
two_person_team = []
topics_team = 0

for i in range(0,people):
    person = input().split()
    matrix.append(person)

for i in range(0,people):
    line1 = matrix[i]
    for j in range(0,people):
        if i < j:
            line2 = matrix[j]
            bit1 = int(line1[0], 2)
            bit2 = int(line2[0], 2)
            or_result = bit1 | bit2
            current_topics = bin(or_result).count('1')
            if current_topics > max_topics:
                max_topics = current_topics
                teams = 1
            elif current_topics == max_topics:
                teams += 1
print(max_topics)
print(teams)
