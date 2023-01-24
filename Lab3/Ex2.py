def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score


def calc_average_score(subject_score):
    return {i: "{:.2f}".format(sum(subject_score[i].values())/len(subject_score[i])) for i in subject_score}
