from distutils.debug import DEBUG


class ConectionMysql():
    DEBUG=True
    MYSQL_HOST='{$_HOST}'
    MYSQL_USER='{$_USER}'
    MYSQL_PASSWORD='{$_PASSWORD}'
    MYSQL_DB='{$_DATABASE}'

config={
    'connection':ConectionMysql
}