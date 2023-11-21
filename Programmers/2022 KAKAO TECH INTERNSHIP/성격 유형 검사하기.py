def solution(survey, choices):
    answer = ''
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    choices = [x-4 for x in choices]
    
    for idx, x in enumerate(survey):
        choice = choices[idx]
        if choice < 0:
            result[x[0]] += -choice
        elif choice > 0:
            result[x[1]] += choice
    
    
    answer += 'T' if result['R'] < result['T'] else 'R'
    answer += 'F' if result['C'] < result['F'] else 'C'
    answer += 'M' if result['J'] < result['M'] else 'J'
    answer += 'N' if result['A'] < result['N'] else 'A'
    
    
    return answer