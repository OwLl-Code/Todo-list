import logging
import json
import requests
import configparser


class RestClient:
    def __init__(self, baseurl="http://localhost:3000"):
        self.baseurl = baseurl

    def taskget(self):
        """
        Осуществляет GET-запрос к серверу для получения списка задач.
        В случае успеха возвращает полученные задачи в формате JSON. Если запрос не удался,
        записывает сообщение об ошибке в лог
        """
        try:
            reply = requests.get(f"{self.baseurl}/tasks")
        except requests.exceptions.RequestException as e:
            logging.error(f"Communication error: {e}")
        else:
            if reply.status_code == requests.codes.ok:
                tasks = reply.json()
                return tasks
            else:
                logging.error("Server error")

    def taskput(self, taskid, updatedtask):
        """
        Осуществляет PUT-запрос к серверу для обновления задачи с указанным ID.
        В случае успеха записывает информацию об успешном обновлении задачи в лог.
        В случае ошибки записывает сообщение об ошибке в лог.
        """
        try:
            reply = requests.put(f"{self.baseurl}/tasks/{taskid}", json=updatedtask)
        except requests.exceptions.RequestException as e:
            logging.error(f"Communication error: {e}")
        else:
            if reply.status_code == requests.codes.ok:
                logging.info("Task updated successfully")
            else:
                logging.error("Server error")

    def taskdelete(self, taskid):
        """
        Осуществляет DELETE-запрос к серверу для удаления задачи с указанным ID.
        В случае успеха записывает информацию об успешном удалении задачи в лог.
        В случае ошибки записывает сообщение об ошибке в лог.
        """
        try:
            reply = requests.delete(f"{self.baseurl}/tasks/{taskid}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Communication error: {e}")
        else:
            if reply.status_code == requests.codes.ok:
                logging.info("Task deleted successfully")
            else:
                logging.error("Server error")

    def taskpost(self, newtask):
        """
        Осуществляет POST-запрос к серверу для создания новой задачи с переданными данными.
        В случае успеха записывает информацию об успешном создании задачи в лог.
        В случае ошибки записывает сообщение об ошибке в лог.
        """
        try:
            reply = requests.post(f"{self.baseurl}/tasks", json=newtask)
        except requests.exceptions.RequestException as e:
            logging.error(f"Communication error: {e}")
        else:
            if reply.status_code == requests.codes.ok:
                logging.info("Task created successfully")
            else:
                logging.error("Server error")


def show_menu():
    """
    Выводит меню действий для пользователя и возвращает выбор пользователя в виде введенного номера действия.
    """
    print("Меню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("0. Выход из программы")
    return input("Выберите действие (введите номер): ")


# создание экземпляра класса RestClient
rest_client = RestClient()


def main():
    # Цикл для обработки выбранных действий
    while True:
        choice = show_menu()

        if choice == "0":
            print("Программа завершена.")
            break

        elif choice == "1":
            tasks = rest_client.taskget()
            print(json.dumps(tasks, indent=2))

        elif choice == "2":
            new_task = {
                "name": input("Введите имя новой задачи: "),
                "priority": input("Введите приоритет задачи: "),
            }
            rest_client.taskpost(new_task)

        elif choice == "3":
            task_id = input("Введите ID задачи для обновления: ")
            updated_task = {
                "name": input("Введите имя задачи: "),
                "priority": input("Введите ID задачи: "),
            }
            rest_client.taskput(task_id, updated_task)

        elif choice == "4":
            task_id_to_delete = input("Введите ID задачи для удаления: ")
            rest_client.taskdelete(task_id_to_delete)

        else:
            print(
                "Неверный выбор действия. Пожалуйста, выберите существующую опцию из меню."
            )


if __name__ == "__main__":
    print("Запущено как самостоятельный модуль")
    main()
else:
    print("Запущено как импортируемый модуль")
