from flask import Flask
from todo.routers import task_bp

app = Flask(__name__)


app.register_blueprint(task_bp, url_prefix='/tasks')


@app.route('/')
def index():
	return 'Главная страница!'


if __name__ == '__main__':
	app.run(debug=True)