# demo use

from unsplash import Unsplash

sp = Unsplash()


def single_search():
    imgs = sp.query(search="horse")

    # dict imgs data of api
    return imgs


def multi_search():
    tags = ["hose","grass","green","sky"]

    t_imgs = sp.query(search=tags)

    # dict imgs data of api
    return t_imgs

def any_img():

    img = sp.any()

    # dict imgs data of api
    return img
