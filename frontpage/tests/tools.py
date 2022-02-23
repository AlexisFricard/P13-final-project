""" TOOLS FOR TESTS """
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from frontpage.models import Actuality
from testimony.models import Testimony
from ourstudent.models import Promotion
from association.models import MemberOffice
from presentation.models import Team
from collabspace.models import Link, Faq


def create_user(name):
    if name == "student":
        staff = 0
    else:
        staff = True
    try:
        user = User.objects.get(username=name)

    except ObjectDoesNotExist:
        User.objects.create_user(
            username=name,
            email=f"{name}@test.fr",
            password="azerty123",
            is_staff=staff,
            is_superuser=staff,
        )
        user = User.objects.get(username=name)
    return user


def delete_user(name):
    User.objects.get(username=name).delete()


def create_faq():
    Faq.objects.create(
        question='test',
        response='test'
    )
    return Faq.objects.get(question='test')


def create_link():
    Link.objects.create(
        title='test',
        link='test'
    )
    return Link.objects.get(title='test')


def create_member(type, nom):
    if type == "office":
        MemberOffice.objects.create(
            name=nom,
        )
        return MemberOffice.objects.get(name=nom)
    if type == "team":
        Team.objects.create(
            name=nom,
            grade=nom,
            img_link='https://test.fr'
        )
        return Team.objects.get(name=nom)


def create_actuality(*args):
    if args:
        title_ = args
    else:
        title_ = 'test'
    Actuality.objects.create(
        title=title_,
        date='2023-01-01',
        stop_date='2023-01-01',
        article='x',
        short_desc='x',
        img_title='x',
        format=0,
        external_link='0',
        state=1
    )
    return Actuality.objects.get(title=title_)


def create_testimony():
    Testimony.objects.create(
            text="test1",
            sector='sectortest1',
            author='testauthor1',
            promotion='promotion test1',
            job='testjob1',
    )
    return Testimony.objects.get(sector='sectortest1')


def create_promotion():
    Promotion.objects.create(
        img_link="testpromo",
        formation='testpromo',
        date='testpromo',
        col1={'title': 'x', 'students': 'x'},
        col2={'title': 'x', 'students': 'x'},
        col3={'title': 'x', 'students': 'x'},
    )
    return Promotion.objects.get(formation='testpromo')


def initialize_user():
    try:
        User.objects.get(username='student').delete()
    except ObjectDoesNotExist:
        pass

    try:
        User.objects.get(username='admin').delete()
    except ObjectDoesNotExist:
        pass

    try:
        User.objects.get(username='nametest').delete()
    except ObjectDoesNotExist:
        pass
