# asgi to test localy
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa
from frontpage.models import (
    Actuality, Link, Faq,
    Testimony, Promotion,
    Ticket, AuthorMessageTicket
)
import os

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sessions.middleware import SessionMiddleware
from frontpage.views import (
    index, presentation, after,
    ourstudent, association,
    myspace, myaccount, ticket,
    actuality, log_out, manage,
    add_data, add_user, helpdashboard,
    error_400, error_403, error_404, error_500
)


# Method to return User object
def create_user(name):
    if name == "student":
        staff = False
    else:
        staff = True

    User.objects.create_user(
        username=name,
        email=f"{name}@test.fr",
        password="azerty123",
        is_staff=staff
    )
    return User.objects.get(username=name)


def delete_user(name):
    User.objects.get(username=name).delete()


# Method to return Ticket object
def create_ticket(name):
    Ticket.objects.create(
        title="ticket-test",
        state=1,
        author=name
        )

    ticket_obj = Ticket.objects.get(title="ticket-test")

    AuthorMessageTicket.objects.create(
        author=name,
        message="test",
        ticket_id=ticket_obj.id
    )
    return ticket_obj


def delete_ticket(_ticket_id):
    Ticket.objects.get(id=_ticket_id).delete()
    AuthorMessageTicket.objects.get(ticket_id=_ticket_id).delete()


class TemplateTest(TestCase):
    def test_index(self):
        request = RequestFactory().get("/index")
        view = index(request)
        assert view.status_code == 200

    def test_presentation(self):
        request = RequestFactory().get("/presentation")
        view = presentation(request)
        assert view.status_code == 200

    def test_after(self):
        request = RequestFactory().get("/after")
        view = after(request)
        assert view.status_code == 200

    def test_ourstudent(self):
        request = RequestFactory().get("/ourstudent")
        view = ourstudent(request)
        assert view.status_code == 200

    def test_association(self):
        request = RequestFactory().get("/association")
        view = association(request)
        assert view.status_code == 200

    def test_actuality(self):

        request = RequestFactory().get("/actuality?actuId=0")

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()
        request.user = AnonymousUser()

        view = actuality(request)
        assert view.status_code == 302
        assert view.url == "/"

        # TODO: Mock actu object

    def test_myspace(self):

        # Unconected User
        request = RequestFactory().get("/myspace")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()

        view = myspace(request)
        assert view.status_code == 200

        # Connect falseuser
        request = RequestFactory().post("/myspace")
        request.POST = {
            'username': "",
            'password': "",
        }
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = myspace(request)
        assert view.status_code == 200

    def test_manage(self):

        # Test anonymous
        request = RequestFactory().get("/manage")
        request.user = AnonymousUser()

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = manage(request)
        assert view.status_code == 302

    def test_myaccount(self):

        request = RequestFactory().get("/myaccount")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = myaccount(request)

        delete_user("student")

        assert view.status_code == 200

    def test_log_out(self):

        request = RequestFactory().post("/log_out")
        request.user = create_user("student")
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = log_out(request)

        delete_user("student")

        assert view.status_code == 302
        assert view.url == "/"


class TestStudent(TestCase):
    def test_manage_student(self):

        request = RequestFactory().get("/manage")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()

        view = manage(request)

        delete_user("student")

        assert view.status_code == 302
        assert view.url == "/monEspace"

    def test_myspace_student(self):

        request = RequestFactory().get("/myspace")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = myspace(request)

        delete_user("student")

        assert view.status_code == 200

    def test_helpdashboard_student(self):

        request = RequestFactory().get("/helpdashboard")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = helpdashboard(request)

        delete_user("student")

        assert view.status_code == 302
        assert view.url == "/monEspace"

    def test_ticket_student(self):

        # With user's ticket
        ticket_obj = create_ticket("student")
        request = RequestFactory().get(f"/ticket?id={ticket_obj.id}")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = ticket(request)

        delete_user("student")

        assert view.status_code == 200

        # With another user's ticket
        request = RequestFactory().get("/ticket?id=10")
        request.user = create_user("student")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = ticket(request)

        delete_user("student")
        delete_ticket(ticket_obj.id)

        assert view.status_code == 302


class TestStaff(TestCase):
    def test_manage_staff(self):

        request = RequestFactory().get("/manage")
        request.user = create_user("staff")

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()

        view = manage(request)

        delete_user("staff")

        assert view.status_code == 302
        assert view.url == "/monEspace"

    def test_helpdashboard_staff(self):

        request = RequestFactory().get("/helpdashboard")
        request.user = create_user("staff")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = helpdashboard(request)

        delete_user("staff")

        assert view.status_code == 200

    def test_ticket_staff(self):

        ticket_obj = create_ticket("student")
        request = RequestFactory().get(f"/ticket?id={ticket_obj.id}")
        request.user = create_user("staff")

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()

        view = ticket(request)

        delete_user("staff")
        delete_ticket(ticket_obj.id)

        assert view.status_code == 302


class TestSuperUser:
    def test_myspace_superuser(self):

        # Connect superuser
        request = RequestFactory().post("/myspace")
        request.POST = {
            'username': os.getenv('M2_SUPERUSER'),
            'password': os.getenv('M2_PASSWORD'),
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = myspace(request)
        assert view.status_code == 302
        assert view.url == "/monEspace"

    def test_manage_superuser(self):

        request = RequestFactory().get("/manage")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()

        view = manage(request)
        assert view.status_code == 200

    def test_adduser(self):

        # Create user
        request = RequestFactory().post("/add_user")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'firstname': "name",
            'lastname': "test",
            'email': "mail@test.io",
            'emailconfirm': "mail@test.io",
            "staff": "true"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_user(request)
        assert view.status_code == 200

        # Test exceptions
        # 1 - Empty Field
        request = RequestFactory().post("/add_user")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'firstname': "",
            'lastname': "test",
            'email': "mail@test.io",
            'emailconfirm': "mail@test.io",
            "staff": "true"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_user(request)
        assert view.status_code == 200

        # 2 - Not same email
        request = RequestFactory().post("/add_user")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'firstname': "name",
            'lastname': "test",
            'email': "mail@test.io",
            'emailconfirm': "mail@test.io",
            "staff": "true"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_user(request)
        assert view.status_code == 200

        # 3 - Allready exist
        request = RequestFactory().post("/add_user")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'firstname': "name",
            'lastname': "test",
            'email': "mail@test.io",
            'emailconfirm': "mail@test.io",
            "staff": "true"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_user(request)
        assert view.status_code == 200

        # Delete it
        user = User.objects.get(email="mail@test.io")
        user.delete()

    def test_adddata_actuality(self):

        # Actuality
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "name",
            'article': "#test",
            "box": "actuality",
            "start": "2021-08-19",
            "end": "2021-08-19",
            "link": "sdvsd"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "name",
            'article': "#test",
            "box": "actuality",
            "start": "",
            "end": "",
            "link": "sdvsd"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        # Create without title
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "",
            'article': "#test",
            "box": "actuality",
            "start": "",
            "end": "",
            "link": "sdvsd"
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        actu = Actuality.objects.get(title="name")
        actu.delete()

    def test_adddata_faq(self):

        # Faq
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'question': "name",
            'text': "test",
            'box': 'faq'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'question': "name",
            'text': "",
            'box': 'faq'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        faq = Faq.objects.get(question="name")
        faq.delete()

    def test_adddata_link(self):

        # link
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "name",
            'link': "test",
            'box': 'link'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "",
            'link': "test",
            'box': 'link'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        link = Link.objects.get(title="name")
        link.delete()

    def test_adddata_testimony(self):

        # testimony
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'text': "name",
            'author': "test",
            'sector': 'link',
            'box': 'testimony'
        }
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'text': "",
            'author': "test",
            'sector': 'link',
            'box': 'testimony'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        testi = Testimony.objects.get(text="name")
        testi.delete()

    def test_adddata_promotion(self):

        # promotion
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "name",
            'img_title': "test",
            'description': 'desc',
            'box': 'promotion'
        }
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "",
            'img_title': "test",
            'description': 'desc',
            'box': 'promotion'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        promo = Promotion.objects.get(title="name")
        promo.delete()

    def test_adddata_ticket(self):

        # ticket
        # Create
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "name",
            'text': "test",
            'box': 'ticket'
        }
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)

        assert view.status_code == 200

        # Create false
        request = RequestFactory().post("/add_data")
        request.user = User.objects.get(username=os.getenv('M2_SUPERUSER'))
        request.POST = {
            'title': "",
            'text': "test",
            'box': 'ticket'
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = add_data(request)
        assert view.status_code == 200

        ticket = Ticket.objects.get(title="name")
        auth_msg = AuthorMessageTicket.objects.get(ticket_id=ticket.id)
        ticket.delete()
        auth_msg.delete()


class TestError:
    def test_400(self):
        request = RequestFactory().get("")
        view = error_400(request, "exception")
        assert view.status_code == 200

    def test_403(self):
        request = RequestFactory().get("")
        view = error_403(request, "exception")
        assert view.status_code == 200

    def test_404(self):
        request = RequestFactory().get("/test404")
        view = error_404(request, "exception")
        assert view.status_code == 200

    def test_500(self):
        request = RequestFactory().get("")
        view = error_500(request)
        assert view.status_code == 200
