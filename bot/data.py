import time
import sqlite3

month_now = time.localtime(time.time())[1]

class MyDb:

    def __init__(self, database):
        #Подключаемся к БД и сохраняем курсор соединения
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def user_id_exists(self, user_id):
        #Проверяем, есть ли уже юзер в базе
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user_id(self, user_id):
        #Добавляем нового юзера
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `users` (`user_id`) VALUES({(user_id)})")

    def mn(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `money` = 0 WHERE `user_id` = {user_id}")

    def mn1(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `base_case` = 0 WHERE `user_id` = {user_id}")

    def mn2(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `boyar_case` = 0 WHERE `user_id` = {user_id}")

    def mn3(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `velmoj_case` = 0 WHERE `user_id` = {user_id}")

    def mn4(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `mecenat_case` = 0 WHERE `user_id` = {user_id}")

    def mn5(self, user_id):
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `time` = 0 WHERE `user_id` = {user_id}")

    def mn6(self, user_id):
        global month_now
        with self.connection:
          return self.cursor.execute(f"UPDATE `users` SET `month` = {month_now} WHERE `user_id` = {user_id}")

    def add_money(self, count, user_id):
        with self.connection:
            return self.cursor.execute(f"UPDATE `users` SET `money` = `money`+250 WHERE `user_id` = {user_id}")

    def reduce_money(self, count, user_id):
        result = self.cursor.execute('SELECT `money` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
        with self.connection:
            for el in result:
                for e in el:
                    if e >= count:
                       return self.cursor.execute(f"UPDATE `users` SET `money` = `money`-{count} WHERE `user_id` = {user_id}")
                    else:
                        pass

    def money_chek(self, count, user_id):
        result = self.cursor.execute('SELECT `money` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
        with self.connection:
            for el in result:
                for e in el:
                    if e >= count:
                        return True
                    else:
                        return False

    def insert_case(self, case_name, user_id):
            with self.connection:
                return self.cursor.execute(f"UPDATE `users` SET `{case_name}` = `{case_name}` +1 WHERE `user_id` = {user_id}")

    def money_chek2(self, user_id):
        result = self.cursor.execute('SELECT `money` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
        with self.connection:
            for el in result:
                for e in el:
                    if e >= 250 and e < 500:
                        return """
1 кейс за 250"""

                    elif e >= 500 and e < 1000:
                        return """
2 кейса по 250
1 кейс за 500"""

                    elif e >= 1000 and e < 2000:
                        return """
3 кейса по 250 (так как нельзя больше 3 открыть в день)
2 кейса по 500
1 кейс за 1000"""

                    elif e >= 2000:
                        return """
3 кейса по 250
3 кейса по 500
2 кейса за 1000
1 кейс за 2000"""

    def what_time(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for el in result:
                if el[2] + el[3] + el[4] + el[5] == 3:
                    return False
                else:
                    return True

    def add_time(self, user_id):
        time_now = time.localtime(time.time())[2] #Записываем сегодняшнее число
        month_now = time.localtime(time.time())[1] #Записываем месяц
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return self.cursor.execute(f"UPDATE `users` SET `time` = {time_now} WHERE `user_id` = {user_id}")
            for el in result:
                print(el[-2])
            for el in result:
                if el[-2] >= time_now:
                    return self.cursor.execute(f"UPDATE `users` SET `time` = {time_now} WHERE `user_id` = {user_id}")
                elif el[-2] < time_now:
                    return self.cursor.execute(f"UPDATE `users` SET `time` = 0 WHERE `user_id` = {user_id}")
                else:
                    pass

    def show_cases(self, user_id):
        cases = ""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for el in result:
                cases += "\n" + str(el[2]) + " - Базовый кейс\n"
                cases += str(el[3]) + " - Кейс для бояр\n"
                cases += str(el[4]) + " - Кейс для Вельмож\n"
                cases += str(el[5]) + " - Кейс для Меценатов"
            return cases

    def close(self):
        #Закрываем соединение с БД
        self.connection.close()