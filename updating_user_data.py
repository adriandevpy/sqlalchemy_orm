from models import Session, User
import random


def main():
    session = Session()
    user = session.query(User).all()

    lucky_user = random.choice(user)
    print(f"THe lucky user is {lucky_user} with id {lucky_user.id}")
    print(f"His salary before raise is {lucky_user.salary}")

    after_raise = lucky_user.salary * 1.15

    print(f"Salary after raise {after_raise}")

    session.add(lucky_user)
    session.commit()

    result = session.query(User).get(lucky_user.id)
    assert result.salary != after_raise


if __name__ == '__main__':
    main()
