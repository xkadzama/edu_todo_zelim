from flask import Blueprint, render_template


task_bp = Blueprint('tasks', __name__, template_folder='templates')


tasks = {
    1: {'title': 'Купить хлеб', 'description': 'Магазин закроется в 23:00'},
    2: {'title': 'Сдать отчет', 'description': 'Дедлайн - завтра в 10:00'},
    3: {'title': 'Записаться к врачу', 'description': 'Терапевт, плановый осмотр'},
    4: {'title': 'Оплатить счета', 'description': 'Коммунальные услуги и интернет'},
    5: {'title': 'Позвонить родителям', 'description': 'Обсудить планы на выходные'},
    6: {'title': 'Подготовиться к встрече', 'description': 'Собрать документы и презентацию'},
    7: {'title': 'Заняться спортом', 'description': 'Тренировка 45 минут'},
    8: {'title': 'Прочитать книгу', 'description': 'Глава 5-6, психология'},
    9: {'title': 'Сделать резервную копию', 'description': 'Файлы с рабочего компьютера'},
    10: {'title': 'Заказать продукты', 'description': 'Онлайн-доставка на субботу'},
}


@task_bp.route('/')
def get_all_tasks():
    return render_template('all_tasks.html', tasks=tasks)


@task_bp.route('/read/<int:id>')
def detail(id):
    task = tasks.get(id)
    return render_template('detail.html', task=task)




# CRUD
# www.hh.ru/tasks/ -> Все задачи (READ) (Реализовано ✅)
# www.hh.ru/tasks/add -> Добавление задачи (CREATE)
# www.hh.ru/tasks/read/2 -> Отображение конкретно одной задачи (по ID) (READ) (Реализовано ✅)
# www.hh.ru/tasks/update/2 -> Обновление задачи (по ID) (UPDATE)
# www.hh.ru/tasks/delete/2 -> Удаление задачи (по ID) (DELETE)








