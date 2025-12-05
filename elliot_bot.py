#Класс Ошибок для бота
class ElliotBotError(Exception):
     def __init__(self, message="Возникла ошибка"):
        self.message = message
        super().__init__(self.message)

def __str__(self):
        return f"[ElliotBot Error] {self.message}"


class InvalidCommandError(ElliotBotError):
    def __init__(self, command):
        super().__init__(f"Неизвестная команда боту команда: '{command}'")

class NotFoundFunctionError(ElliotBotError):
      def __init__(self, function_num):
        super().__init__(f"Функция {function_num} не найдена")


class ValidationError(ElliotBotError):
    def __init__(self, value, expected):
        super().__init__(f"Написано некорректно: '{value}'. Ожидалось : {expected}")


#Основной код
print("Привет,я Бот Еллиот")

while True:
    try:
        рассказать_о_функциях = input("Рассказать о моих функциях (да/нет): ").strip().lower()
        
        if рассказать_о_функциях not in ['да', 'нет']:
            raise ValidationError(рассказать_о_функциях, "'да' или 'нет'")
        
        break
        
    except ValidationError as elliot_bot_error_1:
        print(f" {elliot_bot_error_1}")
        print("Пожалуйста, введите 'да' или 'нет'")

if рассказать_о_функциях.lower() == "нет":
    print("Тогда ладно")
    print("Но знай: я могу рассказать о функциях")
    print("/help - помощь с командами")


elif рассказать_о_функциях.lower() == "да":
    print("Сейчас же расскажу!")
    print("Вот мои функции:")
    print("1- Ответы на математические вопросы")
    print("2- Помощь с кодом(Python)")
    print("3- фишки для компьютера/ноутбука")
    print("4- фишки с командной строкой")
    print("5- установка windows/linux")



def функция_1():
    print("1- Ответы на математические вопросы")

def функция_2():
    print("2- Помощь с кодом(Python)")

def функция_3():
     print("3- фишки для компьютера/ноутбука")

def функция_4():
    print("4- фишки с командной строкой")

def функция_5():
    print("5- установка windows/linux")

while True:
    try:
        выбрать_функцию = input("Выбрать функцию 1-5:")

        if выбрать_функцию == "1":
            функция_1()
        elif выбрать_функцию == "2":
            функция_2()
        elif выбрать_функцию == "3":
            функция_3()
        elif выбрать_функцию == "4":
            функция_4()
        elif выбрать_функцию == "5":
             функция_5()
        else:
             raise NotFoundFunctionError(выбрать_функцию)

    except NotFoundFunctionError as elliot_bot_error_2:
        print(f"Ошибка произошла у бота: {elliot_bot_error_2}")
        print("Пожалуйста,выберите функцию 1-5")
        continue

while True:
    try:

        выбрать_функцию_ещё_раз = input("Выбрать функцию ещё раз(да/нет):").strip().lower()
        if выбрать_функцию_ещё_раз not in ['да', 'нет']:
         raise ValidationError(выбрать_функцию_ещё_раз, "'да' или 'нет'")

        break

    except ValidationError as elliot_bot_error_1:
            print(f" {elliot_bot_error_1}")
            print("Пожалуйста, введите 'да' или 'нет'")
    
    if выбрать_функцию_ещё_раз == "нет":
        print("Вы отказались от выбора функций.")
        break
