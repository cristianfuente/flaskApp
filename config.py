from distutils.debug import DEBUG


class ConectionMysql():
    DEBUG=True
    MYSQL_DATABASE_HOST='{$_HOST}'
    MYSQL_DATABASE_USER='{$_USER}'
    MYSQL_DATABASE_PASSWORD='{$_PASSWORD}'
    MYSQL_DATABASE_DB='{$_DATABASE}'
    #MYSQL_DATABASE_PORT={$_PORT}

config={
    'connection':ConectionMysql
}