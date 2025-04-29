students =["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]
test_performances = [87, 90, 75, 100, 100, 70]

def dict_build(list1: list, list2: list):
    dict_builded = {}

    for i in range(min(len(list1), len(list2))):
        dict_builded[list1[i]] = list2[i]
    return dict_builded

print(dict_build(students, test_performances).values)
print(dict_build(students, test_performances).values())
test_performance = {
    "John" : 87, 
    "Lisa" : 90, 
    "Mary" : 75, 
    "Chris" : 100, 
    "Linda" : 100, 
    "Matt" : 70
}

scores = list(test_performance.values())

def bubble_sort():
    scores.sort(reverse=True)
    return scores

print(bubble_sort())

def avg_score():
    score_list = bubble_sort()
    print(len(score_list))
    print(sum(score_list))
    return sum(score_list) / (len(score_list))

print(avg_score())
