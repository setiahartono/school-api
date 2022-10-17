from api.models import School, Student
from api.tests.base_test import BaseTestCase


HOST_URL = "http://127.0.0.1:8000/api"

class BaseViewTestCase(BaseTestCase):
    model = None
    resource = ""

    def get_index_url(self, **kwargs):
        return f"{HOST_URL}/{self.resource}/"

    def get_create_url(self, **kwargs):
        return self.get_index_url(**kwargs)

    def get_put_url(self, **kwargs):
        if 'identity' not in kwargs:
            identity = self.model.objects.first().id
        else:
            identity = kwargs['identity']
        return f"{HOST_URL}/{self.resource}/{identity}/"

    def get_delete_url(self, **kwargs):
        return self.get_put_url(**kwargs)

    def base_test_validation_create(
            self,
            data,
            expected_status_code,
            valid_expected=True,
        ):
        old_count = self.model.objects.count()

        response = self.client.post(
            self.get_create_url(),
            data=data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, expected_status_code)

        if valid_expected:
            self.assertEqual(self.model.objects.count(), old_count + 1)
        else:
            self.assertEqual(self.model.objects.count(), old_count)

    def base_test_validation_update(
        self, instance, data, fields_to_check,
        identifier='id', valid_expected=True
    ):
        old_value = {}
        for field in fields_to_check:
            old_value[field] = instance.__dict__[field]

        identity = instance.__dict__[identifier]
        res = self.client.put(
            self.get_put_url(identity=identity),
            data=data,
            content_type="application/json"
        )
        print(res.content)
        new_instance = self.model.objects.get(**{identifier: identity})

        # If update fails, expect field will remains the same
        assertion = self.assertNotEqual

        if valid_expected is False:
            assertion = self.assertEqual

        for field in fields_to_check:
            assertion(old_value[field], new_instance.__dict__[field])

    def test_index_loads_properly(self):
        if self.model is not None:
            response = self.client.get(self.get_index_url())
            self.assertEqual(response.status_code, 200)

    def test_delete(self):
        if self.model is not None:
            old_count = self.model.objects.count()
            instance = self.model.objects.first()
            self.client.delete(
                self.get_delete_url(identity=instance.id)
            )
            new_count = self.model.objects.count()

            self.assertEqual(old_count - 1, new_count)


class SchoolViewTestCase(BaseViewTestCase):
    resource = "schools"
    model = School

    def test_create_successful(self):
        data = {
            "name": "Red High School",
            "capacity": 500,
            "address": "47th Fire Red Street",
            "phone_number": "6282828288",
        }
        self.base_test_validation_create(data=data, expected_status_code=201)

    def test_create_failed(self):
        data = [
            # Invalid capacity (negative value)
            {
                "name": "Red High School",
                "capacity": -1,
                "address": "47th Fire Red Street",
                "phone_number": "6282828288",
            },
            # Invalid capacity (zero value)
            {
                "name": "Red High School",
                "capacity": 0,
                "address": "47th Fire Red Street",
                "phone_number": "6282828288",
            }
        ]

        for row in data:
            self.base_test_validation_create(
                data=row,
                expected_status_code=400,
                valid_expected=False
            )

    def test_update(self):
        instance = self.normal_school
        fields = ['name', 'capacity', 'address', 'phone_number']

        data = {
            "name": "Red High School",
            "capacity": 1000,
            "address": "48th Fire Red Street",
            "phone_number": "628282228288",
        }

        self.base_test_validation_update(
            instance=instance, data=data,
            fields_to_check=fields, identifier='id'
        )
    
    def test_update_failed(self):
        instance = School.objects.first()
        fields = ['name', 'capacity', 'address', 'phone_number']
        data = [
            # Invalid capacity (negative value)
            {
                "name": "Red High School",
                "capacity": -1,
                "address": "47th Fire Red Street",
                "phone_number": "6282828288",
            },
            # Invalid capacity (zero value)
            {
                "name": "Red High School",
                "capacity": 0,
                "address": "47th Fire Red Street",
                "phone_number": "6282828288",
            }
        ]

        for row in data:
            self.base_test_validation_update(
                instance=instance, data=row,
                fields_to_check=fields, identifier='id',
                valid_expected=False
            )


class StudentViewTestCase(BaseViewTestCase):
    resource = "students"
    model = Student

    def test_create_successful(self):
        data = {
            "first_name": "Mark",
            "last_name": "White",
            "school": self.normal_school.id
        }
        self.base_test_validation_create(data=data, expected_status_code=201)

    def test_create_failed(self):
        data = [
            # Already reached full capacity
            {
                "first_name": "Mark",
                "last_name": "White",
                "school": self.limited_capacity_school.id
            }
        ]

        for row in data:
            self.base_test_validation_create(
                data=row,
                expected_status_code=400,
                valid_expected=False
            )

    def test_update(self):
        instance = self.normal_students[0]
        fields = ['first_name', 'last_name']

        data = {
            "first_name": "Mark",
            "last_name": "White",
            "school": self.another_normal_school.id
        }

        self.base_test_validation_update(
            instance=instance, data=data,
            fields_to_check=fields, identifier='id'
        )
    
    def test_update_failed(self):
        instance = self.normal_students[0]
        fields = ['first_name', 'last_name']
        data = [
            # Trying to move to school with full capacity
            {
                "first_name": "Mark",
                "last_name": "White",
                "school": self.limited_capacity_school.id
            }
        ]

        for row in data:
            self.base_test_validation_update(
                instance=instance, data=row,
                fields_to_check=fields, identifier='id',
                valid_expected=False
            )


class SSViewsetTestCaseSuccess(StudentViewTestCase):
    def get_index_url(self, **kwargs):
        school_id = self.normal_school.id
        return f"{HOST_URL}/schools/{school_id}/students/"
    
    def get_put_url(self, **kwargs):
        prefix = self.get_index_url()
        student_id = self.normal_students[0].id
        return f"{prefix}{student_id}/"

    def test_create_failed(self):
        print("Bypass")

    def test_update_failed(self):
        print("Bypass")
