# lecture 21
# vote
# using python's dictionary


def vote():
    votes = {}

    for k in range(10):
        print("Enter candidate:")
        name = input()

        if name not in votes:
            votes[name] = 1
        else:
            votes[name] += 1

    for name in votes:
        print(name, votes[name])


vote()
