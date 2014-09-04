fleet-simple
============

Simple Fleet Monitoring
This is one simple modul of any particular modul on current project.


To stop service
supervisorctl stop name
example :
supervisorctl stop nakamichikun_app

To start service
supervisorctl start name
example :
supervisorctl start nakamichikun_app

To restart service running
supervisorctl update

To reload configuration file
supervisorctl reread

Path of file runner on supervisor
/opt/apsi/nakamichikun_app/app_venv/bin/starter.sh

Path of file configuration to supervisor
/etc/supervisor/conf.d/app_name.conf 
/etc/supervisor/conf.d/nakamichikun_app.conf 
