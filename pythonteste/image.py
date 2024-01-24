def my_family(age):
    familY = {'Dad': range(40, 100),
              "Mom" :range(50),
              'child': range(0, 10)
    }
    for member, age_range in  familY.items():
        if age in age_range:
            return member

    return "unknowm"

print(my_family(45))
print(my_family(50))

print(my_family(18))



