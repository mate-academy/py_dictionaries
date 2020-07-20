def sum_values(dict):
    values = dict.values();
    sum = 0;
    for i in values:
        sum += i;

    return sum;

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

def sum_even_keys(dict):
    keys = dict.keys();
    values = list(dict.values());
    sum  = 0;
    j = 0;
    for i in keys:
        if i % 2 == 0:
            sum +=values[j];
        j += 1;

    return sum;

#Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

def add_ten(dict):
    keys = list(dict.keys());
    values = list(dict.values());

    j = 0;
    for i in keys:
        dict.update({i: values[j] + 10});
        j += 1;

    return dict;

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

def values_that_are_keys(dict):
    keys = list(dict.keys());
    values = list(dict.values());

    a = [];
    for i in keys:
        for j in values:
            if i == j:
                a.append(j);

    return a;

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

def max_key(dict):
    keys = list(dict.keys());
    values = list(dict.values());

    max = values[0];
    ind = 0;

    for i in values:
        if max < i:
            max = i;

    for j in values:
        if max == j:
            break;
        ind += 1;

    return keys[ind];

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

