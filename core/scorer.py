def keyword_score(resume_text, jd_text):
    jd_words = jd_text.split()
    resume_words = resume_text.split()

    matched = 0
    for word in set(jd_words):
        if word in resume_words:
            matched += 1

    if len(set(jd_words)) == 0:
        return 0

    return round((matched / len(set(jd_words))) * 100, 2)


def final_score(similarity, keyword_match):
    return round((0.5 * similarity) + (0.5 * keyword_match), 2)