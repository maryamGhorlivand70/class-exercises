lesson_list = [
    {"name": "python", "unit": "3","teacher": "reza"},
    {"name": "java", "unit": "3","teacher": "ali"},
    {"name": "c++", "unit": "5","teacher": "ahmad"},
    {"name": "cpp", "unit": "2","teacher": "alireza"},
]

new_lesson_1 = {"name": "python", "unit": "3","teacher": "reza"}
new_lesson_2 = {"name": "geo", "unit": "2","teacher": "ahmad"}
new_lesson_3 = {"name": "farsi", "unit": "1","teacher": "alireza"}
new_lesson_4 = {"name": "math", "unit": "6","teacher": "seyed"}

student_list = []

def text_to_lesson(lesson):
    lesson_text = lesson["name"].lower()
    return lesson_text

result = list (map(text_to_lesson, lesson_list))
print(result)

def sort_lesson(lesson):
    return lesson["teacher"]

print(sorted(student_list, key=sort_lesson))

def add_price(lesson):
    if lesson["unit"] == 2:
        lesson["total"] = 1000
    elif lesson["unit"] == 3:
        lesson["total"] = 1200
    elif lesson["unit"] == 5:
        lesson["total"] = 1400
    return lesson

print(list(map(add_price, lesson_list)))
