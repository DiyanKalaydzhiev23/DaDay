<h1>DaDay</h1> 
<p>A social network. Тhе main purpose is to share your emotions while you chat with a avatar. Your friends can see the way you feel by daily diagram. 
Users also can send text messages. The project uses Django and React JS.</p>

<h2>Getting started:</h2>

<h3>1. Clone this repository e.g.</h3>

    git clone https://github.com/DiyanKalaydzhiev23/DaDay.git
    
<h3>2. Navigate to the app folder</h3>
    
    cd server

<h3>3. Install requiremets</h3>

    pip install -r requirements.txt
    
<h3>4. Run migrations to update/create database</h3>

    python manage.py migrate
    
<h3>5. Start Redis</h3>

 - <h4>Using Docker:</h4>
  
       docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
    
 - <h4>Using Linux:</h4>
    
       sudo service redis-server start
    
 - <h4>Using Mac:</h4>
    
       brew services start redis
       
<h3>5. Start Celery</h3>

    celery -A server worker -l info -P gevent 

<h3>6. Run the Django development server</h3>

    python manage.py runserver
    
<h3>7. Navigate to client</h3>
    
    cd client
    
<h3>8. Install node_modules</h3>

    npm install
    
<h3>9. Start client</h3>

    npm start
