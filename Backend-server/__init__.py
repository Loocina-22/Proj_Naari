import os
from . import db
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # Change this to a random value when deploying
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # a simple page that says hello
    #@app.route('/complain')
    #def complain():
    #    return 'File a Complain'
    
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import complain
    app.register_blueprint(complain.bp)
    app.add_url_rule('/complain', endpoint='complain')

    # Define static routes here (without blueprints)
    @app.route("/Gynec")
    def Gynec():
        return render_template('features/Gynec.html')

    @app.route("/Career")
    def Career():
        return render_template('features/Career.html')

    @app.route("/Memorial")
    def Memorial():
        return render_template('features/Memorial.html')

    @app.route("/Mensus")
    def Mensus():
        return render_template('features/Mensus.html')

    @app.route("/Ngo")
    def Ngo():
        return render_template('features/Ngo.html')

    @app.route("/Selfdefense")
    def Selfdefense():
        return render_template('features/Self-defense.html')

    @app.route("/laws")
    def laws():
        return render_template('features/laws.html')

    return app










