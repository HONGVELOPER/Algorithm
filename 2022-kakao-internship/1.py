from collections import defaultdict


def solution(survey, choices):
    answer = ""
    dict = defaultdict(lambda: 0)
    for i in range(len(survey)):
        s1, s2 = survey[i][0], survey[i][1]
        if 1 <= choices[i] <= 3:
            dict[s1] += 4 - choices[i]
        elif 5 <= choices[i] <= 7:
            dict[s2] += choices[i] - 4
        else:
            continue
    if dict["R"] >= dict["T"]:
        answer += "R"
    else:
        answer += "T"
    if dict["C"] >= dict["F"]:
        answer += "C"
    else:
        answer += "F"

    if dict["J"] >= dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if dict["A"] >= dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # TCMA
