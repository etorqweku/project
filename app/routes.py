from flask import render_template,flash,redirect,url_for,request
from app import app,db
from app.forms import LoginForm,AgentRegistrationForm,EditProfileForm,ClientRegistrationForm,UploadForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import Agent,Client,Post
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/')
def overview():
    return render_template('index.html')
@app.route('/index')
@login_required
def index():
    return render_template('agent/index.html')

@app.route('/agent-login',methods=['GET','POST'])
def agent_login():
    form =LoginForm()
    if form.validate_on_submit():
        agent=Agent.query.filter_by(username=form.username.data).first()
        if agent is None or not agent.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('agent_login'))
        login_user(agent,remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('agent/login.html',title='Sign In',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('overview'))

@app.route('/agent-register', methods=['GET', 'POST'])
def agent_register():
    form = AgentRegistrationForm()
    if form.validate_on_submit():
        agent = Agent(username=form.username.data, email=form.email.data,name=form.name.data,proffession=form.proffession.data)
        agent.set_password(form.password.data)
        db.session.add(agent)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('agent_login'))
    return render_template('agent/register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    agent = Agent.query.filter_by(username=username).first()
    posts = Post.query.filter_by(agent_username=username).first()

    return render_template('agent/user.html', agent=agent, posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.contact = form.contact.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.contact.data = current_user.contact
    return render_template('agent/edit_profile.html', title='Edit Profile',form=form)

@app.route('/upload',methods=['GET','POST'])
def upload():
    form = UploadForm()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.image.data
            post = Post(body=form.description.data,img_filename=file_name.filename,img_data=file_name.read(),agent_username=current_user.username)
            db.session.add(post)
            db.session.commit()
            flash("Done")
            return render_template('agent/upload.html',title='Upload',form=form)       
    return render_template('agent/upload.html',title='Upload',form=form)
    

@app.route('/client-login',methods=['GET','POST'])
def client_login():
    form =LoginForm()
    if form.validate_on_submit():
        client=Client.query.filter_by(username=form.username.data).first()
        if client is None or not client.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('client_login'))
        login_user(client,remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('client/login.html',title='Sign In',form=form)

@app.route('/client-register', methods=['GET', 'POST'])
def client_register():
    form = ClientRegistrationForm()
    if form.validate_on_submit():
        client = Client(username=form.username.data, email=form.email.data,name=form.name.data)
        client.set_password(form.password.data)
        db.session.add(client)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('client_login'))
    return render_template('client/register.html', title='Register', form=form)


@app.route('/home')
@login_required
def home():
    agents= Agent.query.all()
    return render_template('client/home.html',agents=agents)

@app.route('/mc')
@login_required
def mc():
    proffession='MC'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/mc.html',agents=agents)

@app.route('/dj')
@login_required
def dj():
    proffession='DJ'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/dj.html',agents=agents)

@app.route('/usher')
@login_required
def usher():
    proffession='Usher'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/usher.html',agents=agents)

@app.route('/caterer')
@login_required
def caterer():
    proffession='Caterer'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/caterer.html',agents=agents)

@app.route('/photographer')
@login_required
def photographers():
    proffession='Photographer'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/photographer.html',agents=agents)
    
@app.route('/event-organizer')
@login_required
def event_org():
    proffession='Event Organizer'
    agents=Agent.query.filter_by(proffession=proffession).all()
    return render_template('client/ev_org.html',agents=agents)
    
@app.route('/agent/<string:username>')
def client_view(username):
    agents=Agent.query.filter_by(username=username).first()
    return render_template('client/views.html',agents=agents)
