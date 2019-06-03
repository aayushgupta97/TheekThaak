from .models import *

def get_dataset(*args, **kwargs):
    table=args[0]
    dataset = table.objects.filter(**kwargs)
    return dataset

def get_data(*args, **kwargs):
    table=args[0]
    dataset = table.objects.filter(**kwargs)
    if len(dataset)>0:
        return dataset
    else:
        return -1