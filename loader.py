from db import get_engine, get_session_maker
import config

engine = get_engine(config.DATABASE_URL)
sm = get_session_maker(engine)