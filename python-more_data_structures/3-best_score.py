def best_score(a_dictionary):
    if not a_dictionary:
        return None

    sorted_items = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
    best_student, best_score = sorted_items[0]

    return best_student


