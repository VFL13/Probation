from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_cors import CORS
import os
from datetime import datetime

DEBUG = True

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
    ''' Gamer Activity Model
       time -- datetime of measurement,
       gaze_x -- x-coordinate of the users gaze;
       gaze_y -- y-coordinate of the users gaze;
       keys -- multiset of buttons pressed on keyboard (with duplicates);
       mouse_dx -- mouse wheel delta along x coordinate (useless for majority of players);
       mouse_dy -- mouse wheel delta along y coordinate (useless for majority of players);
       mouse_keys -- multiset of buttons pressed on mouse  (with duplicates).
    '''
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


class Key(db.Model):
    ''' Keys -- multiset of buttons pressed on keyboard;
        key - button
        position - ordering
    '''
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), nullable=True)
    position = db.Column(db.Integer, nullable=False)


class MouseKey(db.Model):
    ''' MouseKey -- multiset of buttons pressed on mouse;
            mouse_key - button
            position - ordering
    '''
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
    ''' page - number of page pagination, default 1
        per_page - records per page, default 10
        start - start datetime, filter by time interval.
        end - end datetime, filter by time interval.
    '''
    page = 1 if request.args.get('page') is None else int(request.args.get('page'))
    per_page = 10 if request.args.get('per_page') is None else int(request.args.get('per_page'))
    start = request.args.get('start')
    end = request.args.get('end')
    all_actions = Activity.query.order_by(Activity.time, Activity.nanoseconds)
    if start:
        start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        all_actions = all_actions.filter(Activity.time >= start)
    if end:
        end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        all_actions = all_actions.filter(Activity.time <= end)
    actions = all_actions.paginate(page, per_page, error_out=False)
    activity_schema = ActivitySchema(many=True)
    result = {'actions': activity_schema.dump(actions.items),
              'page': page,
              "pages": actions.pages,
              "per_page": per_page,
              "total": actions.total}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
