import time
import collections

# 字典的构造方法
dict1 = {"name": "Alice", "age": 23, "email": "test@126.com"}
dict2 = dict(name="Alice", age=23, email="test@126.com")
dict3 = dict([("name", "Alice"), ("age", 23), ("email", "test@126.com")])
dict4 = dict(zip(["name", "age", "email"], ["Alice", 23, "test@126.com"]))
dict5 = dict({"email": "test@126.com", "age": 23, "name": "Alice"})

print(dict1 == dict2 == dict3 == dict4 == dict5)

# 示例一
dial_codes = [(86, 'China'), (91, 'India'), (1, 'Unit States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'),
              (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan')]
country_code1 = {country: code for code, country in dial_codes}
print(country_code1)
# 示例二
codes = [86, 91, 1, 62, 55, 92, 880, 234, 7, 81]
countries = ["China", "India", "Unit States", "Indonesia", "Brazil", "Pakistan", "Bangladesh", "Nigeria", "Russia",
             "Japan"]
country_code2 = {country: code for country in countries for code in codes}
country_code3 = [{country: code} for country in countries for code in codes]
print(country_code2)
print(country_code3)

# 从字典country_code1中搜索Korea对应的号码, 如果没有则赋值为99999
start_time = time.time()
if "Korea" not in country_code1:
    country_code1["Korea"] = 99999
    print((time.time() - start_time)*10000)

# 从字典country_code1中搜索Canada对应的号码, 如果没有则赋值为251
start_time = time.time()
country_code1.setdefault("Canada", 251)
print((time.time() - start_time)*10000)
print(country_code1)

# defaultdict的用法
dd = collections.defaultdict(tuple, **country_code1)
print(dd['China'])
print(dd.get("C"))
print(dd['C'])
print(dd['B'])
print(dd.get('B'))


# 自定义__missing__方法
class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
print(d.get('2'))
print(d.get(4))
print(d.get(1))
print(2 in d)
print(1 in d)
print(d[1])
