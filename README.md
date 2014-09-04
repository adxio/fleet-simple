Simple Fleet Monitoring
============

This is one simple modul of any particular modul on current project.


To stop service
<br/>supervisorctl stop name
<br/>example :
<br/>supervisorctl stop nakamichikun_app

<br/><br/>To start service
<br/>supervisorctl start name
<br/>example :
<br/>supervisorctl start nakamichikun_app

<br/><br/>To restart service running
<br/>supervisorctl update

<br/><br/>To reload configuration file
<br/>supervisorctl reread

<br/><br/>Path of file runner on supervisor
<br/>/opt/apsi/nakamichikun_app/app_venv/bin/starter.sh

<br/><br/>Path of file configuration to supervisor
<br/>/etc/supervisor/conf.d/app_name.conf 
<br/>/etc/supervisor/conf.d/nakamichikun_app.conf 
