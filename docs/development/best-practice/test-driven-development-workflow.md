# Test-Driven Development

The Test-Driven Development can be used for any code project.

When adding new functionality or features, write tests for them first before implementing the new functionality. This ensures that your changes don't affect existing functionality and that all functions work as expected.

## Example: Implement a test case and functionality to test a django app

The following example shows how to implement the testing technique in a Django app.

!!! Info
    You can run all test in django by running:

    ```bash
    python manage.py test
    ```

    To tun specific test cases you have to provide the app name followed by the name of the test case.
    In the example below the command would look like this:

    ```bash
    python manage.py test app.MyModelViewTestCase
    ```

### 1. Step

First, make sure you have an Django app that you want to test.

### 2. Step

Next, write a test for a function or feature you want to implement. Let's say you want to implement a view that returns a list of objects from the database. You also need a model to represent the database table object. A possible test could look like this:

app/tests/my_test.py

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

### 3. Step

Run the test to make sure it fails because the view has not been implemented yet.

```bash
python manage.py test
```

### 4. Step

Implement the model and view to make the test pass.

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

### 5. Step

Run the test again to make sure it passes.

```bash
python manage.py test
```

### 6. Step

Write additional tests to make sure the view works as expected.

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

### 7. Step

Run all the tests to make sure they all pass.

```bash
python manage.py test
```
