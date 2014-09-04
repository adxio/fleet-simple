Simple Fleet Monitoring
============

This is one simple modul of any particular modul on current project.

##  Config

1.  Reload
    ```
    supervisorctl reread
    ```

2.  Path file runner
    ```
    /opt/apsi/nakamichikun_app/app_venv/bin/starter.sh
    ```

3.  File config supervisor
    ```
    /etc/supervisor/conf.d/app_name.conf 
    /etc/supervisor/conf.d/nakamichikun_app.conf 
    ```

##  Service

1.  Start
    supervisorctl start app_name
    example :
    ```
    supervisorctl start nakamichikun_app
    ```
  
2.  Stop
    supervisorctl stop app_name
    example :
    ```
    supervisorctl stop nakamichikun_app
    ```
  
3.  Restart
    ```
    supervisorctl update
    ```
