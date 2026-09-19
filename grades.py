def calculate_grade(score, extra_credit=0):
    final_score = score+extra_credit
    if final_score > 100:
        final_score = 100

    if final_score < 60:
        letter = "F"
        return final_score, letter
    elif final_score >= 60 and final_score < 70:
        letter = "D"
        return final_score, letter
    elif final_score >= 70 and final_score < 80:
        letter = "C"
        return final_score, letter
    elif final_score >= 80 and final_score < 90:
        letter = "B"
        return final_score, letter
    elif final_score >= 90 and final_score <=100:
        letter = "A"
        return final_score, letter
    else:
        return None
    
final_score, letter = calculate_grade(90, 5)
print(f"Score is {final_score}, with a grade {letter}")
final_score2, letter2 = calculate_grade(75)
print(f"Score is {final_score2}, with a grade {letter2}")
final_score3, letter3 = calculate_grade(98, 5)
print(f"Score is {final_score3}, with a grade {letter3}")

