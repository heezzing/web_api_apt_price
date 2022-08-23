from flask import Flask, render_template
import mongodb

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello'

    @app.route('/mongo')
    def mongotest():
        COLLECTION_NAME = 'APT'
        HOST, USER, PASSWORD, DATABASE_NAME = mongodb.db_info()
        MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority'
        collection = mongodb.db_connect(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
        documents = collection.find()
        return render_template('mongo.html',data=documents)

    @app.route('/heezzing')
    def dashboard():
        return render_template('heezzing.html')

    return app