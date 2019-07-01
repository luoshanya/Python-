import numbers
import pymysql

class Filed:
    pass

class IntField(Filed):
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('this value attr must to int')
            elif min_value < 0:
                raise ValueError('this value must bigger than zero')
        elif max_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('this value attr must to int')
            elif min_value < 0:
                raise ValueError('this value must bigger than zero')
        elif min_value and max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')

    # 数据描述符
    def __get__(self, instance, owner):
        # 这里的self.value是set的
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('this value attr must be int')
        elif value < self.min_value or value > self.max_value:
            raise ValueError('value must between min_value and max_length')
        self._value = value

class CharField(Filed):
    def __init__(self, db_column, max_length=None):
        self.value = None
        self.max_length = max_length
        self.db_column = db_column
        if self.max_length is None:
            raise ValueError('max_length not must be None')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('this value attr must be str')
        elif len(value) > self.max_length:
            raise ValueError('value is length  must be smaller than max_length ')
        self._value = value

# 创建元类
class ModelMateClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'BasesModel':
            super().__new__(cls, name, bases, attrs, **kwargs)
        field = {}
        for key, value in attrs.items():
            #首先创建一个类来判断字段
            if isinstance(value, Filed):
                field[key] = value
        attr_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if db_table is not None:
            table = getattr(attr_meta, "db_table", None)
            if  table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['field'] = field
        # del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)

        # return super().__new__()

class BasesModel(metaclass=ModelMateClass):
    # 在传参不确定的情况下 使用*args **kwargs
    def __init__(self, *args, **kwargs):
        # 实例化
        # return super().__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        values = []
        for key, value in self.field.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            # 这里必须将value转str
            values.append(str(value))
        sql = 'insert into {table_name}({fields}) value("{name}",{age})'.format(table_name=self._meta['db_table'], fields=','.join(fields), name=",".join(values).split(',')[0], age=",".join(values).split(',')[1])
        dbparams = {
            'host': "127.0.0.1",
            'port': 3306,
            'db': "test",
            'user': "root",
            'password': "10130503",
            'charset': "utf8"
        }
        conn = pymysql.Connect(**dbparams)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


class User(BasesModel):#调用的话，继承的关系= 会直接找到父类
    # 本来这里是需要实例化来对应用户的操作 那就需要重新创建一个类来继承
    # def __init__(self):
    name = CharField(db_column='name', max_length=10)
    age = IntField(db_column='age', min_value=1, max_value=200)

    class Meta:
        db_table = 'user'

if __name__ == '__main__':
    user = User(name='猪', age=100)
    # user.name = 1
    # user.age = 300
    user.save()