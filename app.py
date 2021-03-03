from create_app import create_app


app = create_app('development')


@app.route('/')
def index():
    return 'JobNinja'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
