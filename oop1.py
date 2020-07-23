class TestRunBuilder:
    pass
    url_test_site = 'https://react-redux.realworld.io/#/?_k=tfjvzl'

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        if "@" and "." in user_email:
            self.email = user_email
        else:
            print("invalid email")



    def login_flow(self):
        print("Click on [Sign in] button")
        print(f"Enter user email {self.user_email}")
        print(f"Enter user password {self.user_password}")
        print("Click [Sign in] button")

    def registration_suite(self):
        print("registration______________________________________")
        print(f"Click on [Sign up] button")
        print(f"Enter username {self.user_name}")
        print(f"Enter user email as {self.user_email}")
        print(f"Enter password as {self.user_password}")
        print("Click on [Sign up] button")

    def create_article(self):
        print('------------------')
        self.login_flow()
        print('Click [New article] button')
        print('fill all fields as test data')
        print('Click [Publish] button')
    def test_run_smoke(self):
        self.login_flow()

    def test_run_sanity(self):
        self.create_article()

    def test_run_regression(self):
        self.registration_suite()
        self.login_flow()
        self.create_article()

test_run_smoke = TestRunBuilder('avatakedavra', 'harry@potter.com', '1111qqqq')
test_run_sanity = TestRunBuilder('sectumsempra', 'ron@vizli.com', 'qqqq1111')
test_run_regression = TestRunBuilder('patronus', 'hermy@greynd.com', '11qq11qq')

test_run_smoke.test_run_smoke()
test_run_sanity.test_run_sanity()
test_run_regression.test_run_regression()