# FoundProject

### Install Prolog

        git clone https://github.com/SWI-Prolog/swipl.git
        cd swipl
        ./configure --prefix=/usr --enable-shared
        make
        sudo make install

### Install Python Environment

        sudo apt-get install python2.7 python-pip
        sudo pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver