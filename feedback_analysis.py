def positive_feedback(ratings):
    rating45 = ratings.count(4) + ratings.count(5)
    percentage = (rating45 / len(ratings)) * 100
    return percentage

str_rating = input("Enter ratings: ")
str_list = str_rating.split(",")

list_rating = []
for x in str_list:
    x = x.strip()
    if x.isdigit():
        num = int(x)
        if 1 <= num <= 5:
            list_rating.append(num)

if len(list_rating) == 0:
    print("No valid ratings were provided.")
else:
    result = positive_feedback(list_rating)
    print("Positive Feedback: {result:.1f}%")