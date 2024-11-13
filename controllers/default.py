# -*- coding: utf-8 -*-

import requests

text = """
*[INFO] Tiene un nuevo mensaje de contacto*

Un usuario acaba de llenar el formulario de contacto ({lang})

Nombre: {name}
Email: {email}
Asunto: {subject}
Mensaje: {message}
"""

def index():
    return dict()

def prices():
    return dict()

@request.restful()
def api():    
    def POST(**kargs):
        response.view = 'generic.json'
        
        if 'name' in kargs and 'email' in kargs and 'subject' in kargs and 'message' in kargs:        
            payload = {
                    'chat_id': chat_id,
                    'text': text.format(
                        name = kargs['name'],
                        email = kargs['email'],
                        subject = kargs['subject'],
                        message = kargs['message'],
                        lang = session._lang
                        ),
                    'parse_mode': 'Markdown'
                    }        
            r = requests.post(url = f"https://api.telegram.org/bot{telegram_token}/sendMessage",json=payload)        
        return dict()    
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
