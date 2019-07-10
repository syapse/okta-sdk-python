class UserProfile:

    types = {
        'login': str,
        'email': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'mobilePhone': str,
        'title': str,
        'manager': str,
        'mobilePhone': str,
        'department': str,
        'city':str,
        'state': str,
        'displayName':str,
        'userType':str,
    	'employeeNumber':str,
        'EmployeeStartDate':str,
        'costCenter':str,
        'ExpensifyAdmin':str
    }

    def __init__(self):

        self.login = None  # str

        self.email = None  # str

        self.secondEmail = None  # str

        self.firstName = None  # str

        self.lastName = None  # str

        self.mobilePhone = None  # str

        self.title = None

        self.manager = None

        self.department = None

        self.mobilePhone = None

        self.state = None

        self.city = None

        self.displayName = None

        self.userType = None

        self.employeeNumber = None

        self.EmployeeStartDate = None
        self.costCenter = None
        self.ExpensifyAdmin = None
