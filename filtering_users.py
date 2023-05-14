from sqlalchemy import and_

from models import Session, User


def main():
    session = Session()
#filter, filter_by, order_by
    # query = session.query(User).filter(
    #     User.salary.between(1000, 2000))\
    #     .order_by(User.salary.desc()
    # )
    # print(query)
    # for user in query.limit(10):
    #     print(user.first_name, user.last_name, user.email)

    print("----------------------------")
# one, one_or_none, first, scalar
#     user = session.query(User).filter(
#         User.salary > 5000
#     ).scalar()
    # print(user)

    print("-------------------------------")

    # result = session.query(User).filter(
    #     User.first_name.like("%A")
    # ).all()
    #
    # print(result)
    print("------------------------------------")

    query = session.query(User.id, User.email,
                          User.creation_date).filter(
        User.salary.between(5000, 6000),
        User.first_name.like("J%")).order_by(
        User.salary.desc(),
        User.creation_date.asc()
    )
    for row in query:
        print(row)


if __name__ == '__main__':
    main()
