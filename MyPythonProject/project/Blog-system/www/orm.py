import asyncio,aiomysql

async def create_pool( loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
            logging.info('rows returned: %s' % len(rs))
            return rs

async def execute(sql, args):
    log(sql)
    global __pool
    async with __pool.acquire() as conn:
        try:
            async with conn.cursor() as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
        except BaseException as e:
            raise
        else:
            return affected

