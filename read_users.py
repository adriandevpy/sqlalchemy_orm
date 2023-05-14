from models import Session, User


def main():
    session = Session()

    query = session.query(User).filter(User.salary > 9000)
    # print(query)
    for lp, user in enumerate(query.limit(10)):
        print(lp + 1, user.first_name, user.last_name, user.email)


if __name__ == '__main__':
    main()
