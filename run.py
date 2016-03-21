from tea_wiki import app, db
import os

if __name__ == '__main__':
    if not os.path.exists('/tmp/test.db'):
        db.create_all()
    app.run(host = '0.0.0.0', debug = True)
