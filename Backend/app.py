from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelSchema
from pprint import pprint

from flask_cors import CORS
import os
import csv
from datetime import datetime
# configuration
DEBUG = True
# first = Activity('2019-11-05 14:55:17.706068503', 0.3, 0.2, 'A', -1.3, -4.3, 'left')
app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)
path = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(path, 'mydb.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
db = SQLAlchemy(app)
ma = Marshmallow(app)

keys = db.Table('keys',
    db.Column('key_id', db.Integer, db.ForeignKey('key.id'), primary_key=True),
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'), primary_key=True)
)

mouse_keys = db.Table('mouse_keys',
    db.Column('mouse_key_id', db.Integer, db.ForeignKey('mouse_key.id'), primary_key=True),
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'), primary_key=True)
)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, unique=False, nullable=False)
    nanoseconds = db.Column(db.String(3), nullable=False)
    gaze_x = db.Column(db.Float, nullable=False)
    gaze_y = db.Column(db.Float, nullable=False)
    keys = db.relationship('Key', secondary=keys, backref=db.backref('activitys', lazy='dynamic'))
    mouse_dx = db.Column(db.Float, nullable=False)
    mouse_dy = db.Column(db.Float, nullable=False)
    mouse_keys = db.relationship('MouseKey', secondary=mouse_keys, backref=db.backref('mouse_activitys', lazy='dynamic'))

    def __init__(self, time, nanoseconds, gaze_x, gaze_y, mouse_dx, mouse_dy):
        self.time = time
        self.nanoseconds = nanoseconds
        self.gaze_x = gaze_x
        self.gaze_y = gaze_y
        self.mouse_dx = mouse_dx
        self.mouse_dy = mouse_dy


    # def __repr__(self):
    #     return f'<Action {self.time} {self.gaze_x} {self.gaze_y} {self.key} {self.mouse_dx} {self.mouse_dy} {self.mouse_key}>'


class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), nullable=True)
    position = db.Column(db.Integer, nullable=False)


class MouseKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mouse_key = db.Column(db.String(20), nullable=True)
    position = db.Column(db.Integer, nullable=False)


class KeySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Key


class MouseKeySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MouseKey


class ActivitySchema(ma.SQLAlchemyAutoSchema):
    keys = ma.Nested(KeySchema, many=True)
    mouse_keys = ma.Nested(MouseKeySchema, many=True)

    class Meta:
        model = Activity


@app.route('/', methods=['GET'])
def get_activity():
    page = 1 if request.args.get('page') is None else int(request.args.get('page'))
    per_page = 10 if request.args.get('per_page') is None else int(request.args.get('per_page'))
    all_actions = Activity.query.order_by(Activity.time, Activity.nanoseconds) #Activity.time.desc()
    actions = all_actions.paginate(page, per_page, error_out=False)
    activity_schema = ActivitySchema(many=True)
    result = {'actions': activity_schema.dump(actions.items),
              'page': page,
              "pages": actions.pages,
              "per_page": per_page,
              "total": actions.total}
    return jsonify(result)

# def initial_upload():
#     dir = "C:\git\Probation\Backend\static\\"
#     files = os.listdir(dir)
#     for file in files:
#         upload_to_db(file)
#
# def upload_to_db(filename):
#     with open(f'C:\git\Probation\Backend\static\{filename}', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=',',)
#         csv_headings = next(spamreader)
#         for row in spamreader:
#             if row != csv_headings:
#                 print(row[0][:-3])
#                 action_time = datetime.strptime(row[0][:-3], '%Y-%m-%d %H:%M:%S.%f')
#                 key = row[3].replace('{', '').replace('}', '').replace("'", '').split(',')
#                 mouse_key = row[6].replace('{', '').replace('}', '').replace("'", '').split(',')
#                 action = Activity(action_time, row[0][-3:], float(row[1]), float(row[2]), float(row[4]), float(row[5]),)
#                 keyObj_list = []
#                 for i in range(0, len(key)):
#                     keyObj = Key.query.filter_by(key=key[i], position=i).first()
#                     if keyObj is None:
#                         keyObj = Key(key=key[i], position=i)
#                         db.session.add(keyObj)
#                         db.session.commit()
#                         keyObj_list.append(keyObj)
#                     action.keys.append(keyObj)
#                 mouse_keyObj_list = []
#                 for i in range(0, len(mouse_key)):
#                     mouse_keyObj = MouseKey.query.filter_by(mouse_key=mouse_key[i], position=i).first()
#                     if mouse_keyObj is None:
#                         mouse_keyObj = MouseKey(mouse_key=mouse_key[i], position=i)
#                         db.session.add(mouse_keyObj)
#                         db.session.commit()
#                         mouse_keyObj_list.append(mouse_keyObj)
#                     action.mouse_keys.append(mouse_keyObj)
#                 db.session.add(action)
#                 db.session.commit()


if __name__ == '__main__':
    #initial_upload()
    app.run()
