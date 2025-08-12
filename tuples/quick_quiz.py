def question_game() : 
    question_list = [('What is 2*2 ?','4'),('What is the capital of India ?','delhi'),('What is the common age in india to drive any vehicle ?','18')]
    money_per_answer = 0
    for question,correct_answer in question_list :
        print(question)
        users_ans = input("Write The answer : ").lower().strip()
        if(users_ans == correct_answer) :
            money_per_answer = money_per_answer+100
        else :
            print("wrong answer")
    return money_per_answer
total_money = question_game()
print(f"Total money won: ₹{total_money}")
