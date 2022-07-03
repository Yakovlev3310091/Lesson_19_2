from lesson19_project_hard_source.dao.director import DirectorDAO
from lesson19_project_hard_source.dao.genre import GenreDAO
from lesson19_project_hard_source.dao.movie import MovieDAO
from lesson19_project_hard_source.dao.user import UserDAO
from lesson19_project_hard_source.service.auth import AuthService
from lesson19_project_hard_source.service.director import DirectorService
from lesson19_project_hard_source.service.genre import GenreService
from lesson19_project_hard_source.service.movie import MovieService
from lesson19_project_hard_source.service.user import UserService
from lesson19_project_hard_source.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
