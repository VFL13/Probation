# Probation Task
# Gamer Activity Dashboard

The datasets contain the following columns:
1. time -- datetime of measurement,
2. gaze_x -- x-coordinate of the users gaze;
3. gaze_y -- y-coordinate of the users gaze;
4. key -- multiset of buttons pressed on keyboard (with duplicates);
5. mouse_dx -- mouse wheel delta along x coordinate (useless for majority of players);
6. mouse_dy -- mouse wheel delta along y coordinate (useless for majority of players);
7. mouse_key -- multiset of buttons pressed on mouse  (with duplicates).



### Installation requirements
For backend
```sh
$ cd backend
$ pip -r requirements.txt
```

For frontend...

```sh
$ cd frontend/dashboard
$ npm install
```

### Start backend development server 
Start Flask app:
```sh
$ cd backend
$ python app.py
```

By default flask run on localhost and port - 5000.
If you use other startup options change **axios.defaults.baseURL** in **/frontend/dashboard/src/api.sevice.js**

### Start frontend development server 
Start Vue app:
```sh
$ cd frontend/dashboard
$ npm run serve
```

### Todos





