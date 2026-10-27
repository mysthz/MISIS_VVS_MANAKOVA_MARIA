class WorkLifeBalance:

    def __init__(self, work_hours, sleep_hours, commute_hours):
        self.work_hours = work_hours
        self.sleep_hours = sleep_hours
        self.commute_hours = commute_hours
        self.personal_hours= 24-(self.work_hours+self.sleep_hours+self.commute_hours)

    def calculate_balance_score(self):
        work_percent = (self.work_hours/24)*100
        ideal_percent = (8/24)*100
        score = 100- (abs(work_percent - ideal_percent))*2
        score = max(0, score)
        return round(score, 1)

class AdvancedWorkLifeBalance(WorkLifeBalance):

    def get_recommendation(self):
        score = self.calculate_balance_score()
        if self.sleep_hours <= 6.5:
            return "Вы слишком мало спите! Постарайтесь увлеичить количество часов сна."
        elif self.personal_hours < 2:
            return "У вас почти нет личного времени. Риск выгорания."
        if score >= 80:
            return "Отличный баланс между работой и личной жизнью!"
        elif score >= 60:
            return "Баланс неплохой, но есть куда стремиться."
        return "Слишком много времени уходит на работу."

work = float(input("Сколько часов в день вы работаете? "))
sleep = float(input("Сколько часов вы спите? "))
commute = float(input("Сколько часов уходит на дорогу? "))

person = AdvancedWorkLifeBalance(work, sleep, commute)

print(f"Личное время: {person.personal_hours} ч.")
print(f"Баланс: {person.calculate_balance_score()} баллов")
print(person.get_recommendation())
