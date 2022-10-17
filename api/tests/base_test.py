from django.test import TestCase

from model_bakery import baker


class BaseTestCase(TestCase):
    # Data already been set up for subclasses
    def setUp(self):
        self.normal_school = baker.make(
            'api.School',
            capacity=500,
        )
        self.another_normal_school = baker.make(
            'api.School',
            capacity=500,
        )
        self.limited_capacity_school = baker.make(
            'api.School',
            capacity=5,
        )

        self.normal_students = baker.make(
            'api.Student',
            school=self.normal_school,
            _quantity=50
        )
        self.limited_students = baker.make(
            'api.Student',
            school=self.limited_capacity_school,
            _quantity=5
        )
