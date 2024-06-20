#
# Regular cron jobs for the django-template package.
#
0 4	* * *	root	[ -x /usr/bin/django-template_maintenance ] && /usr/bin/django-template_maintenance
