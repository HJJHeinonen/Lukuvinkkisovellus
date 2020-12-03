import re

from application import db
from application.tips.models import Tip, Book, Video
from tests.util import make_soup


def test_initial_data(client):
    soup = make_soup(client.get("/tips").data)
    assert "Clean Code: A Handbook of Agile Software Craftsmanship" in soup.text


def test_tips_render_video(client):
    db.session().add(Video(
        title="test video",
        source="test source",
        comment="test comment",
        tags="Ohjelmointi, algoritmit"
    ))
    soup = make_soup(client.get("/tips").data)
    assert "test video" in soup.text
    assert "test source" in soup.text
    assert "test comment" in soup.text
    assert "Ohjelmointi, algoritmit" in soup.text
    #assert "Muokkaa tai poista" in soup.text

""" def test_edit_or_delete_button_exists(client):
    db.session().add(Video(
        title="test video",
        source="test source",
        comment="test comment",
        tags="Ohjelmointi, algoritmit"
    ))
    soup = make_soup(client.get("/tips").data)
    links = soup.findAll('a')
    exists = False
    for link in links:
        if link.text == 'Muokkaa tai poista':
            exists = True
            break
    assert exists == True """

def test_empty_db(client):
    db.session().query(Tip).delete()
    soup = make_soup(client.get("/tips").data)
    
    assert soup.find(class_="card mb-3") == None


def test_missing_field(client):
    db.session().add(Book(
        title="test title",
        author="test author",
    ))
    soup = make_soup(client.get("/tips").data)
    test_book = soup.find(string=re.compile("test title")).parent
    assert "ISBN" not in test_book.text


def test_missing_mandatory_field_book(client):
    resp = client.post("/tips/add-book", data={
        "title": "new book",
        "publication_year": 2020,
    })
    soup = make_soup(resp.data)
    author = soup.find(attrs={"id": "author"}).parent
    assert "This field is required" in author.text
    assert Book.query.filter_by(title="new book").count() == 0


def test_successful_post_book(client):
    resp = client.post("/tips/add-book", data={
        "title": "new book",
        "author": "some author",
        "publication_year": 2020,
    })
    assert resp.status_code == 302
    new_book = Book.query.filter_by(title="new book").all()
    assert len(new_book) == 1
    assert new_book[0].title == "new book"
    assert new_book[0].author == "some author"
    assert new_book[0].publication_year == 2020
    assert new_book[0].pages == None
    assert new_book[0].isbn == ""
    assert new_book[0].comment == ""
    assert new_book[0].related_courses == ""
    assert new_book[0].tags == ""


def test_missing_mandatory_field_video(client):
    resp = client.post("/tips/add-video", data={
        "title": "test title",
    })
    soup = make_soup(resp.data)
    source = soup.find(attrs={"id": "source"}).parent
    assert "This field is required" in source.text
    assert Video.query.filter_by(title="test title").count() == 0

def test_successful_post_video(client):
    resp = client.post("/tips/add-video", data={
        "title": "new video",
        "source": "www.test.com",
        "upload_date": '2020-12-01',
        "comment": "test comment"
    })
    assert resp.status_code == 302
    new_video = Video.query.filter_by(title="new video", source="www.test.com", upload_date='2020-12-01').all()
    assert len(new_video) == 1
    assert new_video[0].comment == 'test comment'
    assert new_video[0].related_courses == ''