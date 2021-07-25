# Считаем кредит

name1 = input("Введите имя первого человека: ")
name2 = input("Введите имя второго человека: ")
name3 = input("Введите имя третьего человека: ")

salary1 = input("ЗП первого человека: ")
salary2 = input("ЗП второго человека: ")
salary3 = input("ЗП тертьего человека: ")

credit = input("Введите сумму кредита: ")
period = input("Введите срок в месяцах: ")
procent = input("Введите процент кредита: ")

pay_per_month = (int(credit) / int(period)) + (int(credit) / 100 * int(procent)) / 12
print("Ежемесячный платеж составит:" , pay_per_month, "рублей")

s1 = "ы"
s2 = "а"
print("у" , name1[-6:-1] + s1 , "после платежа по кредиту останется" , int(salary1) - int(pay_per_month) , "рублей")
print("у" , name2[-6:] + s2 , "после платежа по кредиту останется" , int(salary2) - int(pay_per_month) , "рублей")
print("у" , name3[-11:] + s2 , "после платежа по кредиту останется" , int(salary3) - int(pay_per_month) , "рублей")


