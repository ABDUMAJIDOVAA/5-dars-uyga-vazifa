
# 1-decorator
def chek_javob(func):
    def wrapper(*args, **kwargs):
        a = int(input('Javobni top: 2*2=?'))
        if a == 4:
            func(*args, **kwargs)
        else:
            return False
    return wrapper

# 2-decorator
def chek_javob(func):
    def wrapper(*args, **kwargs):
        a = int(input('Javobni top: 2*2=?'))
        if a == 4:
            func(*args, **kwargs)
        else:
            raise ValueError("Son to'g'ri kiritilmadi")
    return wrapper

# 3-decorator
def chek_sth(func):
    def wrapper(*args, **kwargs):
        if True:
            start = time.time()
            result =  func(*args, **kwargs)
            stop = time.time()
            print(f"Result {round(stop-start)}")
            if round(stop-start) < 5:
                return result
    return wrapper

# 4-decorator
def chek_sth(func):
    def wrapper(*args, **kwargs):
        if True:
            start = time.time()
            result =  func(*args, **kwargs)
            stop = time.time()
            print(f"Result {round(result)}")
            if round(stop-start):
                return result
    return wrapper


"""echo "# 5-dars-uyga-vazifa" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ABDUMAJIDOVAA/5-dars-uyga-vazifa.git
git push -u origin main
"""