for _ in range(int(input())):
    marks = input()
    score = 0
    for index, item in enumerate(marks):
        if item == "O":
            score += 1
            for x in range(index - 1, -1, -1):
                if marks[x] == "O":
                    score += 1
                else:
                    break

    print(score)
