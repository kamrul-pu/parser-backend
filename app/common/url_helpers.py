from django.urls import reverse


def get_url_by_name(name:str)->str:
    return reverse(name)


def get_detail_url_by_name_id(name:str,id:int)->str:
    return reverse(name, args=[id])
