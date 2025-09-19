from database import SessionLocal
from models import User

session = SessionLocal()

# 데이터 삽입
new_user = User(name="김사랑", email="kim@example.com")
session.add(new_user)
session.commit()

# 조회
user = session.query(User).filter(User.name == "김사랑").first()
print(user.id, user.name, user.email, user.age)
