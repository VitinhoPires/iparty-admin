from flask import Flask, session, redirect, url_for, render_template
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sua_chave_super_secreta'

    # Importar e registrar o blueprint
    from .routes import bp
    app.register_blueprint(bp)

    # Registrar rotas automáticas para templates
    templates_path = os.path.join(app.root_path, 'templates')
    if os.path.exists(templates_path):
        for template in os.listdir(templates_path):
            if template.endswith('.html'):
                route = '/' + template

                def make_view(template_name):
                    def view():
                        if 'user' not in session:
                            return redirect(url_for('main.login'))
                        return render_template(template_name)
                    return view

                app.add_url_rule(route, endpoint=template, view_func=make_view(template))

    return app
