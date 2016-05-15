import sys
import uuid
from badminton import app
from models import db, User
from utils import SendGrid


def main():
    with app.app_context():
        print app.config['HOST_NAME']
        # users = User.query.order_by(User.firstname.asc()).all()
        #
        # for user in users:
        #     forgot_password_token = uuid.uuid1()
        #     user.forgotPasswordToken = str(forgot_password_token)
        #     db.session.commit()
        #
        #     subject = "Badminton: set password to access your account"
        #     message = 'Hi ' + user.firstname + ",\r\n\n" + \
        #               'In order to access your account on new Badminton website you need to click the below link' + \
        #               ' to set your password.\r\n\n' + \
        #               str(request.url_root) + "resetPassword?token=" + user.forgotPasswordToken + \
        #               SendGrid.send_email(user.email, "no-reply@sendgrid.me", subject, message)

if __name__ == '__main__':
    sys.exit(main())