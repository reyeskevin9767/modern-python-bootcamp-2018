
# * Extract Full Name
def extract_full_name(names):
    return list(' '.join(x) for x in zip(list(map(lambda x: x['first'], names)),
                                         list(map(lambda x: x['last'], names))))
