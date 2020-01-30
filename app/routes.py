from app import app, db
from app.models import *
from flask import redirect, render_template, url_for, flash
from app.forms import *
from flask_login import current_user, login_user, login_required,logout_user
from app.models import Users, login_manager


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/lineup')
# def lineup():
#     return render_template('lineup.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html',name=current_user.username)


@app.route('/add', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        newuser = Users(email=form.email.data, username=form.username.data, password=hashed_password)

        db.session.add(newuser)
        db.session.commit()
        flash('Succesfully Registered')
        return redirect('/')

    return render_template('registration.html',register=form)



#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login=Login()
#
#     if not login.validate_on_submit():
#         user=Users.query.filter_by(username=login.username.data).first()
#         if user:
#             if user.password == login.password.data:
#                 user_login=True
#                 return redirect('addPlayer')
#         flash('Invalid Username or password')
#
#     return render_template('login.html',login=login)
#

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('user_profile'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/manageTeam', methods=['GET', 'POST'])
@login_required
def manageTeam():
    createTeam = TeamForm()
    addPlayer=PlayerForm()

    app.logger.debug(addPlayer.errors)

    if addPlayer.validate_on_submit():
        print("addPlayer.name.data", addPlayer.name.data)
        print("chooseTactic.tactic.data", createTeam.tactic.data)
        newTeam = Team(team_name=createTeam.team_name.data, tactic=createTeam.tactic.data,user=current_user)
        newPlayer = Players_db(name=addPlayer.name.data, number=addPlayer.number.data, position=addPlayer.position.data,
                               team=newTeam)

        db.session.add(newTeam)
        db.session.add(newPlayer)
        db.session.commit()
    else :
        print("addPlayer.errors", addPlayer.errors)
        # newConfig=Config()
        # db.session.add(newConfig)
        # db.session.commit()


    seePlayers = Players_db.query.all()

    return render_template('add_player.html',addPlayer=addPlayer,seePlayers=seePlayers,createTeam=createTeam)



# @app.route('/deleteplayer', methods=['GET', 'POST'])
# def deletePlayer():
#     deletePlayer=Player_delete()
#
#     if deletePlayer.validate_on_submit():
#         name=deletePlayer.name.data
#         number=deletePlayer.number.data
#         position=deletePlayer.position.data
#
#         deletePlayer = Players_db(name=name, number=number, position=position)
#         db.session.delete(deletePlayer)
#         db.session.commit()
#         return redirect('/')
#
#     return render_template('delete_player.html',deletePlayer=deletePlayer,seePlayers=seePlayers)