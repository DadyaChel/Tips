

def validate_importance(data):
    if data > 100:
        data = 100
        return data
    return data


print(validate_importance(999))