import orm
from model import User, Blog, Comment
import asyncio,sys


async def test(loop,**kw):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await orm.destory_pool()

data = dict(name='aaa', email='1123221@qq.com', passwd='1111', image='about:blank')
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop, **data))
loop.close()
