# LETS TRY TO CONNECT TO MY DOCKER REDIS INSTANCE
#https://github.com/andymccurdy/redis-py

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_redis import FlaskRedis
import redis
from redis import StrictRedis

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secretkey123'
)

# pool = redis.ConnectionPool(host='192.168.99.100', port=32771, db=0, charset="utf-8", decode_responses=True)
# r = redis.Redis(connection_pool=pool)

r = redis.StrictRedis(host='192.168.99.100', port=32771, db=0, charset="utf-8", decode_responses=True)
pipe = r.pipeline()

pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
pipe.sadd('drug001', 'pt101','pt102','pt108','pt999').execute()
pipe.sadd('drug002', 'pt103','pt104','pt105','pt106','pt107','pt109','pt123','pt456','pt120').execute()
pipe.sadd('ae001', 'pt120','pt101','pt107','pt109','pt123','pt456').execute()
pipe.sadd('ae002', 'pt101','pt103','pt104').execute()
pipe.sinterstore('d1a1','drug001','ae001').sinterstore('d1a2','drug001','ae002').sinterstore('d2a1','drug002','ae001').sinterstore('d2a2','drug002','ae002').execute()

def percent(num1, num2):
    return '{0:.2%}'.format((num1 / num2))


# Index
@app.route('/')
def index():

    x=(r.smembers('drug001'))
    print('drug001 has ',x)
    x=(r.smembers('ae001'))
    print('ae001 has ',x)
    x=(r.smembers('test'))
    print('test has ',x)
    x=(r.hmget('aelist','ae001'))
    y=(r.hmget('aelist','ae002'))
    drug001=(r.scard('drug001'))
    drug002=(r.scard('drug002'))

    d1a1=r.scard('d1a1')," ({:.2%}".format((r.scard('d1a1')/r.scard('drug001')))
    d1a2=r.scard('d1a2')," ({:.2%}".format((r.scard('d1a2')/r.scard('drug001')))
    d2a1=r.scard('d2a1')," ({:.2%}".format((r.scard('d2a1')/r.scard('drug002')))
    d2a2=r.scard('d2a2')," ({:.2%}".format((r.scard('d2a2')/r.scard('drug002')))
    z=r.scard('d2a2'),percent(r.scard('d2a2'),r.scard('drug002'))
    print('test has ',z ,' elements')
    return render_template('home.html',x=x,y=y,z=z,drug001=drug001,drug002=drug002, d1a1=d1a1,d1a2=d1a2,d2a1=d2a1,d2a2=d2a2)

# {'attrs': ['a', 'b', 'c']}

# WORKS!
# import redis
# r = redis.StrictRedis(host='192.168.99.100', port=32770, db=0)
# r.set('foo', 'bar')
# print(r.get('foo'))

if __name__ == '__main__':
    app.run(debug=True)
