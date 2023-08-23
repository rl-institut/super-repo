# Test-Driven Development

The Test-Driven Development can be used for any code project. The following example shows how to implement the testing technique in a Django app.

When adding new functionality or features, write tests for them first before implementing them. This ensures that your changes don't affect existing functionality and that all functions work as expected.

You can run test in django by running:
`python manage.py test`

1 First, make sure you have an Django app that you want to test.

2 Next, write a test for a function or feature you want to implement. Let's say you want to implement a view that returns a list of objects from the database. You also need a model to represent the database table object. A possible test could look like this:

```python
from django.test import TestCase
from myapp.models import MyModel

class MyModelViewTestCase(TestCase):
    def test_list_view_displays_all_objects(self):
        MyModel.objects.create(name="object1")
        MyModel.objects.create(name="object2")
        response = self.client.get('/my-models/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "object1")
        self.assertContains(response, "object2")

```

3 Run the test to make sure it fails because the view has not been implemented yet.

4 Implement the model and view to make the test pass.

models.py

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

views.py

```python
from django.views.generic import ListView
from myapp.models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = "myapp/my_model_list.html"

```

5 Run the test again to make sure it passes.

6 Write additional tests to make sure the view works as expected.

```python
class MyModelViewTestCase(TestCase):
    def test_list_view_displays_all_objects(self):
        MyModel.objects.create(name="object1")
        MyModel.objects.create(name="object2")
        response = self.client.get('/my-models/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "object1")
        self.assertContains(response, "object2")

    def test_list_view_displays_empty_message(self):
        response = self.client.get('/my-models/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No objects found.")


```

7 Run all the tests to make sure they all pass.
