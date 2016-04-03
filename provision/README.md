# Provisioning

You can use the files contained in this directory to provision
your machine in order to make the project working.

To start quickly edit the ``ansible_deploy_inventory`` and ``ansible_deploy_variables``
files following your taste and then

    $ cd provision/
    $ bin/ansible -i ansible_deploy_inventory -v ansible_deploy_variables

BTW exists the ``requirements_maintainer.txt`` with packages necessary to deploy all of this.

## Supervisor

To manage the running state of ``teambot`` we are using a [supervisor](https://supervisord.readthedocs.org/en/latest/)
configuration script in ``/etc/supervisor/teambot.conf``.

It's possible to restart the app thanks to a ``sudo`` configuration that allows
certain commands on ``supervisorctl``.

    $ sudo /usr/bin/supervisorctl restart teambot



## Ansible

Use the 2.0+ version.

## Vagrant

Out of the box is available a Debian8 virtualbox configuration, you have
to do a simple

    $ vagrant up --provider virtualbox

If you want to login with the user

    $ ssh -i id_rsa_my_project my_project@127.0.0.1 -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no

If you want to copy something inside you can do

    $ scp -i id_rsa_my_project -P 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no foobar.py  my_project@127.0.0.1:app/
