import matplotlib.pyplot as plt

grades = "A+ A A- B+ B B- C+ C C- D+ D D- F"
grades = grades.split()
numbers = "10 9.5 9 8.7 8.5 8 7.7 7.5 7 6.7 6.5 6 5"
numbers = numbers.split()
numbers = [float(n) for n in numbers]
grader = dict((k,v) for k,v in zip(grades,numbers))

#AV Club

orphan_black_season1 = 'A- A- B A- B B+ C+ B+ A A-'
orphan_black_season2 = 'A B+ A- A B A- B+ C- A- B'

def get_scores(season):
    """

    :param season: string of grades
    :return: score
    """
    grades = season.split()
    score = 0
    scores = []
    for g in grades:
        score += grader[g]
        scores.append(grader[g])
    return score / len(grades),scores

s1 = get_scores(orphan_black_season1)
s2 = get_scores(orphan_black_season2)

plt.plot(s1[1])
plt.plot(s2[1])
plt.show()

