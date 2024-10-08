from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.test import TestCase

import pytest

from urlmapper.models import URLMap


class TestModels(TestCase):
    def setUp(self):
        self.url_map = URLMap.objects.create(key="test_3", url="/test/3/")
        self.invalid_url_map = URLMap.objects.create(key="test_1", url="/invalid/")

    def test_get_key_choices(self):
        assert set(self.url_map._meta.get_field(field_name="key").choices) == set(
            (("test_3", "test_3"), ("test_4", "test_4"), ("test_5", "test_5"))
        )

    def test_invalid_map_does_not_show(self):
        assert list(URLMap.objects.all()) == [self.url_map]

    def test_only_one_mapping_allowed(self):
        # No mapping
        map = URLMap(key="test_4")
        with self.assertRaises(ValidationError):
            map.full_clean()

        # More than one mapping
        map = URLMap(key="test_4", url="abc", content_type=ContentType.objects.first())
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", url="abc", object_id=1)
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", object_id=1, view_name="test")
        with self.assertRaises(ValidationError):
            map.full_clean()

    def test_only_valid_url_allowed(self):
        map = URLMap(key="test_4", url="/invalid/")
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", url="/test/")
        self.assertIsNone(map.full_clean())

    @pytest.mark.skip(reason="No get_absolute_url on user")
    def test_only_valid_object_allowed(self):
        # No get_absolute_url on site
        site = Site.objects.first()
        map = URLMap(key="test_4", content_object=site)
        with self.assertRaises(ValidationError):
            map.full_clean()

        # get_absolute_url on user
        user = User.objects.create_user("test")
        map = URLMap(key="test_4", content_object=user)
        self.assertIsNone(map.full_clean())

    def test_only_valid_view_allowed(self):
        map = URLMap(key="test_4", view_name="invalid")
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", view_name="test")
        self.assertIsNone(map.full_clean())

        map = URLMap(key="test_4", view_name="test", view_keywords="invalid")
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", view_name="test", view_keywords="still=invalid")
        with self.assertRaises(ValidationError):
            map.full_clean()

        map = URLMap(key="test_4", view_name="test", view_keywords="pk=12345")
        self.assertIsNone(map.full_clean())

        map = URLMap(key="test_4", view_name="test", view_keywords="slug=test-it-works")
        self.assertIsNone(map.full_clean())

    def test_get_url(self):
        assert self.url_map.get_url() == "/test/3/"

    def test_get_mapping_type(self):
        assert self.url_map.mapping_type() == "Direct"
