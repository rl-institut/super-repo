# Test-Driven Development

Test-Driven Development (TDD) is a software development methodology that
emphasizes writing tests before implementing the corresponding functionality.
This approach ensures that new changes do not unintentionally break existing
features and that all functions perform as expected.

## Code Coverage

Code coverage is a metric used in software testing that helps determine
the percentage of code that is exercised by tests.
It is an essential tool for assessing the effectiveness of your test suite.
High code coverage generally indicates that most of your code has been tested,
while lower coverage can suggest that some parts of the application may be
under-tested, potentially leading to hidden bugs or vulnerabilities.

[Codecov.io](https://codecov.io/) is a popular tool for tracking and
visualizing code coverage. It integrates with various CI/CD pipelines and
allows developers to upload their coverage reports. <br>
Once integrated, Codecov provides detailed insights into code coverage trends,
coverage gaps, and areas that require further testing.

To integrate Codecov with your project, follow these steps:

1. Install pytest <br>
    💻 `pip install pytest pytest-cov`

2. Add GitHub Action <br>
   📝 `.github/workflows/codecov.yml`

3. Create an account <br>
Create a Codecov account at [Codecov.io](https://about.codecov.io/) and link your repository.

4. Upload the Coverage Report <br>
After running your tests with coverage, upload the results to Codecov. <br>
This is  done automatically through the CI configuration.

5. View Coverage Reports <br>
Once your coverage report is uploaded, you can view detailed insights and trends
on the Codecov dashboard.

6. Code Coverage Badge <br>
A coverage badge provides a visual indication of the test coverage for the
📝 `README.rst` page. It is updated automatically as new reports are uploaded to Codecov.

While code coverage is a valuable metric for identifying untested code,
high coverage does not necessarily indicate high-quality tests.
It only measures the quantity of code exercised during testing, not the quality
or effectiveness of those tests. Tests can pass without actually verifying
correct behavior, and some areas of the code may be covered by trivial tests
that do not expose potential issues. Relying solely on coverage can lead to a
false sense of security and might divert attention from other important aspects
of testing, such as edge cases and integration scenarios.

## Example: Implementing Test Cases for a Django App

This example demonstrates the TDD approach within a Django app. <br>
You can run all tests in Django using the following command:

    💻 `python manage.py test`

To run specific test cases, you can provide the app name and the test case:

    💻 `python manage.py test app.MyModelViewTestCase`

This is a Step-by-Step Guide to TDD in Django:

### 1. Set Up the Django App

Ensure that you have a Django app in place that you wish to test.

### 2. Write a Test for the New Feature

Begin by writing a test for the functionality you intend to implement.
For example, if you need to create a view that returns a list of objects from
the database, and a corresponding model to represent the database table,
your test might look like this: <br>
    📝 `app/test/my_test.py`:

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

### 3. Run the Test

At this point, run the test to confirm it fails, as the view has not been implemented yet. <br>
    💻 `python manage.py test`

### 4. Implement the Model and View

Implement the model and view to make the test pass.

📝 `models.py`:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

📝 `views.py`:

```python
from django.views.generic import ListView
from myapp.models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = "myapp/my_model_list.html"

```

### 5. Run the Test Again

Run the tests again to ensure the changes pass the test. <br>
    💻 `python manage.py test`

### 6. Add Additional Tests

Write additional tests to verify that the view works as expected. <br>
For example, you can test for empty responses:

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

### 7. Run All Tests

Finally, run all the tests to ensure they pass successfully: <br>
    💻 `python manage.py test`

### Conclusion

TDD provides a structured approach to writing reliable, maintainable software.
By ensuring that tests are written before implementing functionality,
developers can be confident that new changes will not introduce unintended
side effects and that the codebase remains functional and robust over time.

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
