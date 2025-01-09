import os, sys, time, random, json
from flask import *

app = Flask('chat nafs')

user_log = []
cookies = []
chat = []
chat2 = {}
file = []
adm = []

class nafs:
    def __init__(self, ua):
        self.ua = ua
    def serial(self):
        hash = ''
        for i in range(0,4):
            hash += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        return hash
    def roomget(self, sen):
        global chat, chat2
        for i in chat:
            if i['ua'] == sen:
                for a in i['chatroom']:
                    if a['ua'] == self.ua:
                        return a['id']
                    else:
                        sr = self.serial()
                        i['chatroom'].append({'id': sr, 'ua': self.ua})
                        chat2[sr] = []
                        for z in chat:
                            if z['ua'] == self.ua:
                                z['chatroom'].append({'id': sr, 'ua': sen})
                        return sr
                     
    def chat(self, sender, txt, file=[]):
        rm = self.roomget(sender)
        scm = {'from': self.ua, 'file': file, 'time': '', 'txt': txt}
        scm[self.ua] = True
        scm[sender] = False
        chat2[rm].append(scm)
        return 'udah'
    
    def chatroom(self, sen, send, txt):
        global chat, chat2
        chat2[sen].append({'from': self.ua, 'file': file, 'time': '', 'txt': txt, self.ua: True, send: False})
        return True
    
def cekacc(ua):
    global user_log, cookies
    if ua in user_log and ua in cookies:
        return True
    else:return False

@app.route('/login')
def idindndn():
    if request.headers.get('User-Agent') in cookies:return redirect('/')
    else:
        if request.method == 'post':
            if request.headers.get('User-Agent') in user_log:
                a = request.headers.get('User-Agent')
                cookies.append(a)
        else:return """
<html><head><title>login</title></head><body>
<form action='/login' method='post'>
<input type='text'>no</input>
<button type='submit'>login</button>
</form>
</body></html>
"""

@app.route('/daftar')
def rhfhfefuer():
    if request.headers.get('User-Agent') in user_log:return redirect('/login')
    else:
        if request.method == 'post':
            global chat, chat2
            chat.append({'ua': request.headers.get('User-Agent'), 'chatroom': []})
            user_log.append(request.headers.get('User-Agent'))
            return redirect('/')
        else:return """
<html><head><title>daftr</title></head><body>
<form action='/daftar' method='post'>
<input type='text'>no</input>
<button type='submit'>login</button>
</form>
</body></html>
"""
@app.route('/to')
def dhhdghfdf():
    if cekacc(request.headers.get('User-Agent')):
        if request.method == 'post':
            pesan = request.form['msg']
            sndt = request.form['to']
            att = []
            conn = nafs(request.headers.get('User-Agent'))
            a = conn.chat(sndt, pesan, att)
            if a == 'udah':return redirect('/')
            else:return redirect('/to')
        else:
            tee = """
<html><head><title>to</title></head><body>
<form action='/to' method='post'>
<input type='text' name='msg'>message : </input>
<div class="form-group">
                <label for="choice">send to</label>
                <select class="form-control" id="mode" name="to" required>"""
            for i in user_log:
                tee +=f"""    <option value='{i}'>{i}</option>"""
            
            tee += """    </select>
            </div>
<button type='submit'>send</button>
</form>
</body></html>
"""
            return tee
    else:return redirect('/login')

@app.route('/')
def djdgg():
    global chat,chat2
    if cekacc(request.headers.get('User-Agent')):
        tot = """<html><head><title>to</title></head><body>"""
        tr = nafs(request.headers.get('User-Agent'))
        for i in chat:
            if i['ua'] == request.headers.get('User-Agent'):
                for v in i['chatroom']:
                    tot += f"<br><hr><a href='/room?id={v['id']}>{v['ua']}</a>"
        tot += "</body></html>"
        return tot
    else:return redirect('/login')




    
